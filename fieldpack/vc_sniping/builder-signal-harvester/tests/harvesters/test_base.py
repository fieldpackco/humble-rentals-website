from builder_harvester.harvesters.base import BaseHarvester
from builder_harvester.models import RawProfile


class MockHarvester(BaseHarvester):
    """Mock harvester for testing."""

    def harvest(self, **kwargs) -> list[RawProfile]:
        return [
            RawProfile(
                source="mock",
                source_id="user123",
                name="Test User",
                profile_url="https://example.com/user123",
            )
        ]


def test_base_harvester_interface():
    """Test that BaseHarvester can be subclassed."""
    harvester = MockHarvester()
    results = harvester.harvest()
    assert len(results) == 1
    assert results[0].name == "Test User"
    assert results[0].source == "mock"
