"""Scoring and classification logic."""

import re
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
