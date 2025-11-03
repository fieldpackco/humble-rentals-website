import pytest
from unittest.mock import Mock, patch
from builder_harvester.harvesters.gh import GitHubHarvester


@pytest.fixture
def mock_response():
    """Mock GitHub API response."""
    return {
        "items": [
            {
                "owner": {
                    "login": "janesmith",
                    "html_url": "https://github.com/janesmith",
                },
                "name": "battery-monitor",
                "description": "Battery monitoring system",
                "stargazers_count": 500,
                "topics": ["battery-management", "iot"],
                "html_url": "https://github.com/janesmith/battery-monitor",
            }
        ]
    }


def test_github_harvester_search_repos(mock_response):
    """Test GitHub repo search and owner extraction."""
    with patch("httpx.Client") as mock_client:
        mock_client.return_value.__enter__.return_value.get.return_value.json.return_value = mock_response

        harvester = GitHubHarvester(token="fake_token")
        results = harvester.harvest(topics=["battery-management"], min_stars=100)

        assert len(results) == 1
        assert results[0].name == "janesmith"
        assert results[0].source == "github"
        assert "battery-monitor" in results[0].metadata["repos"][0]["name"]
