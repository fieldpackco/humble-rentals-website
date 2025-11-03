from builder_harvester.scoring import classify_angel_signal, calculate_operator_score
from builder_harvester.models import RawProfile


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
