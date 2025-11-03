import pytest
from pydantic import ValidationError
from builder_harvester.models import Person, Evidence, SocialLinks


def test_person_model_basic():
    """Test Person model with minimal required fields."""
    person = Person(
        person_id="test_123",
        name="Jane Smith",
        primary_url="https://example.com/jane",
        sources=["github"],
        operator_score=0.8,
        angel_score=0.3,
    )
    assert person.name == "Jane Smith"
    assert person.operator_score == 0.8
    assert person.angel_score == 0.3


def test_person_model_with_evidence():
    """Test Person model with evidence and social links."""
    evidence = Evidence(
        source="github",
        text="Maintains battery-monitoring repo with 500 stars",
        url="https://github.com/jane/battery-monitor",
        timestamp="2025-10-01",
    )
    social = SocialLinks(
        linkedin="https://linkedin.com/in/janesmith",
        twitter="https://twitter.com/janesmith",
    )
    person = Person(
        person_id="test_123",
        name="Jane Smith",
        primary_url="https://github.com/janesmith",
        sources=["github"],
        operator_score=0.8,
        angel_score=0.3,
        evidence=[evidence],
        social_links=social,
    )
    assert len(person.evidence) == 1
    assert str(person.social_links.linkedin) == "https://linkedin.com/in/janesmith"


def test_invalid_url_in_social_links():
    """Test that invalid URLs in SocialLinks raise ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        SocialLinks(linkedin="not-a-valid-url")
    assert "linkedin" in str(exc_info.value)


def test_invalid_url_in_evidence():
    """Test that invalid URLs in Evidence raise ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        Evidence(
            source="github",
            text="Test evidence",
            url="not-a-valid-url",
            timestamp="2025-10-01",
        )
    assert "url" in str(exc_info.value)


def test_invalid_url_in_person_primary_url():
    """Test that invalid primary_url in Person raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        Person(
            person_id="test_123",
            name="Jane Smith",
            primary_url="not-a-valid-url",
            sources=["github"],
            operator_score=0.8,
            angel_score=0.3,
        )
    assert "primary_url" in str(exc_info.value)


def test_invalid_timestamp_format():
    """Test that invalid timestamp format raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        Evidence(
            source="github",
            text="Test evidence",
            url="https://github.com/test",
            timestamp="not-a-date",
        )
    assert "timestamp must be in ISO format" in str(exc_info.value)


def test_invalid_last_activity_format():
    """Test that invalid last_activity format raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        Person(
            person_id="test_123",
            name="Jane Smith",
            primary_url="https://example.com/jane",
            sources=["github"],
            operator_score=0.8,
            angel_score=0.3,
            last_activity="not-a-date",
        )
    assert "last_activity must be in ISO format" in str(exc_info.value)


def test_valid_iso_timestamp_formats():
    """Test that various valid ISO timestamp formats are accepted."""
    # Date only
    evidence1 = Evidence(
        source="github",
        text="Test",
        url="https://github.com/test",
        timestamp="2025-10-01",
    )
    assert evidence1.timestamp == "2025-10-01"

    # Date with time
    evidence2 = Evidence(
        source="github",
        text="Test",
        url="https://github.com/test",
        timestamp="2025-10-01T14:30:00",
    )
    assert evidence2.timestamp == "2025-10-01T14:30:00"

    # Date with time and timezone
    evidence3 = Evidence(
        source="github",
        text="Test",
        url="https://github.com/test",
        timestamp="2025-10-01T14:30:00+00:00",
    )
    assert evidence3.timestamp == "2025-10-01T14:30:00+00:00"

    # ISO format with Z (UTC)
    evidence4 = Evidence(
        source="github",
        text="Test",
        url="https://github.com/test",
        timestamp="2025-10-01T14:30:00Z",
    )
    assert evidence4.timestamp == "2025-10-01T14:30:00Z"
