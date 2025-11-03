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
    assert person.social_links.linkedin == "https://linkedin.com/in/janesmith"
