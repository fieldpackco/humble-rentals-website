"""GitHub harvester plugin."""

import os
import httpx
from datetime import datetime
from builder_harvester.harvesters.base import BaseHarvester
from builder_harvester.models import RawProfile, SocialLinks


class GitHubHarvester(BaseHarvester):
    """Harvest operator-angels from GitHub."""

    def __init__(self, token: str = None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"

    def harvest(self, topics: list[str], min_stars: int = 100, **kwargs) -> list[RawProfile]:
        """
        Search GitHub repos by topics and extract owners.

        Args:
            topics: List of topic strings (e.g., ["battery-management", "iot"])
            min_stars: Minimum star count

        Returns:
            List of RawProfile objects for repo owners
        """
        profiles = {}

        with httpx.Client(timeout=30.0) as client:
            for topic in topics:
                # Search repos by topic
                url = f"{self.base_url}/search/repositories"
                params = {
                    "q": f"topic:{topic} stars:>={min_stars}",
                    "sort": "stars",
                    "per_page": 50,
                }
                headers = {
                    "Authorization": f"Bearer {self.token}",
                    "Accept": "application/vnd.github+json",
                }

                response = client.get(url, params=params, headers=headers)
                response.raise_for_status()
                data = response.json()

                # Extract repo owners
                for repo in data.get("items", []):
                    owner = repo["owner"]
                    username = owner["login"]

                    if username not in profiles:
                        profiles[username] = RawProfile(
                            source="github",
                            source_id=username,
                            name=username,
                            profile_url=owner["html_url"],
                            metadata={"repos": []},
                        )

                    # Add repo to metadata
                    profiles[username].metadata["repos"].append({
                        "name": repo["name"],
                        "description": repo.get("description", ""),
                        "stars": repo["stargazers_count"],
                        "topics": repo.get("topics", []),
                        "url": repo["html_url"],
                    })

        return list(profiles.values())
