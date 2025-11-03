"""Identity resolution and profile merging."""

import re
from collections import defaultdict
from builder_harvester.models import Person


def normalize_name(name: str) -> str:
    """Normalize name for matching: lowercase, remove middle initials, strip spaces."""
    name = name.lower().strip()
    # Remove middle initials (single letter with optional period)
    name = re.sub(r'\b[a-z]\.?\s+', ' ', name)
    # Collapse multiple spaces
    name = re.sub(r'\s+', ' ', name)
    return name


def find_matches(people: list[Person]) -> list[set[str]]:
    """
    Find matching profiles based on ≥2 matching fields.

    Returns:
        List of sets, each containing person_ids that should be merged
    """
    # Build index by matching fields
    by_name = defaultdict(list)
    by_linkedin = defaultdict(list)
    by_twitter = defaultdict(list)
    by_website = defaultdict(list)

    for person in people:
        norm_name = normalize_name(person.name)
        by_name[norm_name].append(person.person_id)

        if person.social_links:
            if person.social_links.linkedin:
                by_linkedin[str(person.social_links.linkedin).lower()].append(person.person_id)
            if person.social_links.twitter:
                by_twitter[str(person.social_links.twitter).lower()].append(person.person_id)
            if person.social_links.website:
                by_website[str(person.social_links.website).lower()].append(person.person_id)

    # Find pairs with ≥2 matching fields
    match_counts = defaultdict(int)

    for index in [by_name, by_linkedin, by_twitter, by_website]:
        for ids in index.values():
            if len(ids) > 1:
                for i, id1 in enumerate(ids):
                    for id2 in ids[i+1:]:
                        pair = tuple(sorted([id1, id2]))
                        match_counts[pair] += 1

    # Extract matches with ≥2 fields
    match_groups = []
    processed = set()

    for pair, count in match_counts.items():
        if count >= 2:
            id1, id2 = pair
            if id1 not in processed and id2 not in processed:
                match_groups.append({id1, id2})
                processed.update([id1, id2])

    return match_groups


def merge_profiles(people: list[Person]) -> Person:
    """
    Merge multiple Person profiles into one canonical profile.

    Takes max scores, combines evidence, uses first name found.
    """
    if len(people) == 1:
        return people[0]

    # Use first person as base
    merged = people[0].model_copy(deep=True)

    # Combine sources
    all_sources = set(merged.sources)
    for p in people[1:]:
        all_sources.update(p.sources)
    merged.sources = sorted(all_sources)

    # Take max scores + cross-platform boost
    merged.operator_score = max(p.operator_score for p in people)
    merged.angel_score = max(p.angel_score for p in people)

    # Apply cross-platform boost if from multiple sources
    if len(all_sources) > 1:
        merged.operator_score = min(merged.operator_score * 1.1, 1.0)
        merged.angel_score = min(merged.angel_score * 1.1, 1.0)

    # Combine evidence
    all_evidence = []
    for p in people:
        all_evidence.extend(p.evidence)
    merged.evidence = all_evidence

    # Merge social links
    if not merged.social_links:
        merged.social_links = people[1].social_links if len(people) > 1 else None
    else:
        for p in people[1:]:
            if p.social_links:
                merged.social_links.linkedin = merged.social_links.linkedin or p.social_links.linkedin
                merged.social_links.twitter = merged.social_links.twitter or p.social_links.twitter
                merged.social_links.website = merged.social_links.website or p.social_links.website

    # Set canonical_id
    merged.canonical_id = merged.person_id

    return merged
