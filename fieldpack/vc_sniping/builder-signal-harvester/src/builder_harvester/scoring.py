"""Scoring and classification logic."""

import re
import os
import json
from anthropic import Anthropic
from builder_harvester.models import RawProfile


# Angel signal keywords
ANGEL_YES_KEYWORDS = [
    "angel investor",
    "investing in",
    "advisor",
    "check size",
    r"\$\d+k.*check",  # Regex for "$5k checks"
]

ANGEL_NO_KEYWORDS = [
    "seeking investors",
    "looking for funding",
    "we're hiring",
    "join our team",
]


def classify_angel_signal(profile: RawProfile) -> str:
    """
    Classify angel investment signal using heuristics.

    Returns:
        "auto_yes", "auto_no", or "borderline"
    """
    bio = (profile.bio or "").lower()

    # Check auto-yes patterns
    for keyword in ANGEL_YES_KEYWORDS:
        if re.search(keyword, bio, re.IGNORECASE):
            return "auto_yes"

    # Check auto-no patterns
    for keyword in ANGEL_NO_KEYWORDS:
        if keyword in bio:
            return "auto_no"

    # No bio or unclear
    if not bio or len(bio) < 10:
        return "auto_no"

    # Check for advisory/mentorship hints (borderline)
    if any(word in bio for word in ["advisor", "advising", "mentor", "helping"]):
        return "borderline"

    return "auto_no"


def calculate_operator_score(profile: RawProfile) -> float:
    """
    Calculate operator strength score (0.0 to 1.0).

    Based on:
    - Number of relevant repos
    - Total stars
    - Relevance of topics
    """
    score = 0.0

    if profile.source == "github":
        repos = profile.metadata.get("repos", [])
        if not repos:
            return 0.0

        # Relevant topics (and partial matches)
        relevant_topics = {
            "battery-management", "lithium-ion-batteries", "battery",
            "iot-projects", "iot", "robotics", "embedded-systems", "embedded",
            "power-management", "energy-storage", "energy",
        }

        total_stars = 0
        relevant_repos = 0

        for repo in repos:
            stars = repo.get("stars", 0)
            topics = set(repo.get("topics", []))

            total_stars += stars

            # Check topic overlap (exact match or substring match)
            is_relevant = False
            for topic in topics:
                for relevant_topic in relevant_topics:
                    if relevant_topic in topic.lower() or topic.lower() in relevant_topic:
                        is_relevant = True
                        break
                if is_relevant:
                    break

            if is_relevant:
                relevant_repos += 1

        # Scoring formula
        star_score = min(total_stars / 1000, 1.0) * 0.5  # Max 0.5 from stars
        repo_score = min(relevant_repos / 3, 1.0) * 0.5  # Max 0.5 from repos

        score = star_score + repo_score

    return min(score, 1.0)


def batch_classify_with_llm(profiles: list[RawProfile], batch_size: int = 20) -> list[dict]:
    """
    Classify borderline profiles using LLM in batches.

    Args:
        profiles: List of RawProfile objects to classify
        batch_size: Number of profiles per batch

    Returns:
        List of dicts with source_id, operator_score, angel_score, evidence
    """
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # Load prompt template
    prompt_path = "prompts/classifier_prompt.md"
    with open(prompt_path, "r") as f:
        system_prompt = f.read()

    results = []

    # Process in batches
    for i in range(0, len(profiles), batch_size):
        batch = profiles[i:i + batch_size]

        # Format profiles for prompt
        profile_data = []
        for p in batch:
            profile_data.append({
                "source_id": p.source_id,
                "name": p.name,
                "bio": p.bio or "",
                "repos": p.metadata.get("repos", [])[:3],  # Top 3 repos
                "social_links": p.social_links.dict() if p.social_links else {},
            })

        # Call LLM
        user_message = f"Classify these {len(batch)} profiles:\n\n{json.dumps(profile_data, indent=2)}"

        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=4096,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )

        # Parse JSON response
        response_text = response.content[0].text
        batch_results = json.loads(response_text)
        results.extend(batch_results)

    return results
