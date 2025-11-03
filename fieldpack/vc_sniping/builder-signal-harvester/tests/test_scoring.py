from builder_harvester.scoring import classify_angel_signal, calculate_operator_score
from builder_harvester.models import RawProfile
from unittest.mock import patch, Mock


def test_classify_angel_signal_auto_yes():
    """Test auto-yes heuristics for angel signals."""
    profile = RawProfile(
        source="github",
        source_id="test",
        name="Test User",
        bio="Angel investor writing $5k-$25k checks",
        profile_url="https://example.com",
    )

    result = classify_angel_signal(profile)
    assert result == "auto_yes"


def test_classify_angel_signal_auto_no():
    """Test auto-no heuristics."""
    profile = RawProfile(
        source="github",
        source_id="test",
        name="Test User",
        bio="Seeking investors for our startup! We're hiring engineers.",
        profile_url="https://example.com",
    )

    result = classify_angel_signal(profile)
    assert result == "auto_no"


def test_classify_angel_signal_borderline():
    """Test borderline cases that need LLM."""
    profile = RawProfile(
        source="github",
        source_id="test",
        name="Test User",
        bio="CTO @ BatteryCo. Open to advising early-stage teams.",
        profile_url="https://example.com",
    )

    result = classify_angel_signal(profile)
    assert result == "borderline"


def test_calculate_operator_score_high():
    """Test operator scoring for strong signal."""
    profile = RawProfile(
        source="github",
        source_id="test",
        name="Test User",
        profile_url="https://example.com",
        metadata={
            "repos": [
                {"name": "battery-monitor", "stars": 500, "topics": ["battery-management"]},
                {"name": "iot-platform", "stars": 300, "topics": ["iot"]},
            ]
        },
    )

    score = calculate_operator_score(profile)
    assert score >= 0.7


def test_batch_classify_with_llm():
    """Test LLM batch classification."""
    profiles = [
        RawProfile(
            source="github",
            source_id="user1",
            name="Test User",
            bio="CTO @ BatteryCo. Open to advising.",
            profile_url="https://example.com",
            metadata={"repos": [{"name": "battery-sys", "stars": 200}]},
        )
    ]

    mock_response = Mock()
    mock_response.content = [
        Mock(text='[{"source_id": "user1", "operator_score": 0.7, "angel_score": 0.5, "evidence": ["CTO role", "Advising hint"]}]')
    ]

    # Mock the Anthropic client and its methods
    with patch("builder_harvester.scoring.Anthropic") as mock_client_class:
        mock_client_instance = Mock()
        mock_client_instance.messages.create.return_value = mock_response
        mock_client_class.return_value = mock_client_instance

        from builder_harvester.scoring import batch_classify_with_llm
        results = batch_classify_with_llm(profiles)

        assert len(results) == 1
        assert results[0]["operator_score"] == 0.7
        assert results[0]["angel_score"] == 0.5
