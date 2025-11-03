import pytest
from builder_harvester.merging import normalize_name, find_matches, merge_profiles
from builder_harvester.models import Person, Evidence, SocialLinks


def test_normalize_name():
    """Test name normalization."""
    assert normalize_name("Jane R. Smith") == "jane smith"
    assert normalize_name("JANE SMITH") == "jane smith"
    assert normalize_name("  Jane   Smith  ") == "jane smith"


def test_find_matches_by_social_links():
    """Test matching profiles by social links."""
    p1 = Person(
        person_id="gh_jane",
        name="Jane Smith",
        primary_url="https://github.com/janesmith",
        sources=["github"],
        operator_score=0.8,
        angel_score=0.3,
        social_links=SocialLinks(linkedin="https://linkedin.com/in/janesmith"),
    )
    p2 = Person(
        person_id="ph_jane",
        name="Jane R Smith",
        primary_url="https://producthunt.com/@janesmith",
        sources=["producthunt"],
        operator_score=0.6,
        angel_score=0.5,
        social_links=SocialLinks(linkedin="https://linkedin.com/in/janesmith"),
    )

    matches = find_matches([p1, p2])
    assert len(matches) == 1
    assert set(matches[0]) == {"gh_jane", "ph_jane"}


def test_merge_profiles():
    """Test merging matched profiles."""
    p1 = Person(
        person_id="gh_jane",
        name="Jane Smith",
        primary_url="https://github.com/janesmith",
        sources=["github"],
        operator_score=0.8,
        angel_score=0.3,
        evidence=[Evidence(source="github", text="500 stars", url="https://github.com/repo", timestamp="2025-01-01")],
    )
    p2 = Person(
        person_id="ph_jane",
        name="Jane R Smith",
        primary_url="https://producthunt.com/@janesmith",
        sources=["producthunt"],
        operator_score=0.6,
        angel_score=0.5,
        evidence=[Evidence(source="producthunt", text="Launched product", url="https://producthunt.com/product", timestamp="2025-01-15")],
    )

    merged = merge_profiles([p1, p2])
    assert merged.name == "Jane Smith"
    assert set(merged.sources) == {"github", "producthunt"}
    # Max of both with 10% cross-platform boost: 0.8 * 1.1 = 0.88
    assert merged.operator_score == pytest.approx(0.88)
    # Max of both with 10% cross-platform boost: 0.5 * 1.1 = 0.55
    assert merged.angel_score == pytest.approx(0.55)
    assert len(merged.evidence) == 2
