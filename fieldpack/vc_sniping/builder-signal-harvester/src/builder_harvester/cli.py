"""Command-line interface for builder-signal-harvester."""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

from builder_harvester.harvesters.gh import GitHubHarvester
from builder_harvester.scoring import classify_angel_signal, calculate_operator_score, batch_classify_with_llm
from builder_harvester.merging import find_matches, merge_profiles
from builder_harvester.export import export_to_notion_csv
from builder_harvester.models import Person, Evidence


def harvest_gh(args):
    """Harvest from GitHub."""
    print(f"Harvesting GitHub for topics: {args.topics}")

    topics = args.topics.split(",")
    harvester = GitHubHarvester()
    profiles = harvester.harvest(topics=topics, min_stars=args.stars)

    # Save raw data
    os.makedirs("data/raw", exist_ok=True)
    output_file = f"data/raw/gh_{datetime.now().strftime('%Y-%m-%d')}.json"

    with open(output_file, "w") as f:
        json.dump([p.dict() for p in profiles], f, indent=2)

    print(f"Harvested {len(profiles)} GitHub profiles → {output_file}")


def run_pipeline(args):
    """Run full pipeline: harvest, score, merge, export."""
    print("Running full pipeline...")

    # Parse thresholds
    operator_threshold = float(args.threshold.split(",")[0].split(":")[1])
    angel_threshold = float(args.threshold.split(",")[1].split(":")[1])

    # Step 1: Harvest GitHub
    print("\n[1/5] Harvesting GitHub...")
    topics = ["battery-management", "iot-projects", "robotics", "embedded-systems"]
    gh_harvester = GitHubHarvester()
    raw_profiles = gh_harvester.harvest(topics=topics, min_stars=100)
    print(f"  Found {len(raw_profiles)} profiles")

    # Step 2: Score profiles
    print("\n[2/5] Scoring profiles...")
    people = []
    borderline = []

    for profile in raw_profiles:
        angel_signal = classify_angel_signal(profile)
        operator_score = calculate_operator_score(profile)

        if angel_signal == "auto_yes":
            angel_score = 0.9
        elif angel_signal == "borderline":
            borderline.append(profile)
            continue  # Will score with LLM
        else:
            angel_score = 0.1

        # Create Person object
        person = Person(
            person_id=f"gh_{profile.source_id}",
            name=profile.name,
            primary_url=profile.profile_url,
            sources=["github"],
            operator_score=operator_score,
            angel_score=angel_score,
            evidence=[Evidence(
                source="github",
                text=f"GitHub: {len(profile.metadata.get('repos', []))} repos",
                url=profile.profile_url,
                timestamp=datetime.now().isoformat(),
            )],
        )
        people.append(person)

    # Step 3: LLM classification for borderline cases
    if borderline:
        print(f"\n[3/5] Classifying {len(borderline)} borderline profiles with LLM...")
        llm_results = batch_classify_with_llm(borderline)

        for profile, result in zip(borderline, llm_results):
            person = Person(
                person_id=f"gh_{profile.source_id}",
                name=profile.name,
                primary_url=profile.profile_url,
                sources=["github"],
                operator_score=result["operator_score"],
                angel_score=result["angel_score"],
                evidence=[Evidence(
                    source="llm",
                    text="; ".join(result["evidence"]),
                    url=profile.profile_url,
                    timestamp=datetime.now().isoformat(),
                )],
            )
            people.append(person)
    else:
        print("\n[3/5] No borderline cases, skipping LLM")

    # Step 4: Merge duplicates (placeholder, only GitHub for now)
    print(f"\n[4/5] Checking for duplicates...")
    matches = find_matches(people)
    print(f"  Found {len(matches)} potential duplicates")

    # Step 5: Filter and export
    print(f"\n[5/5] Filtering and exporting...")
    qualified = [
        p for p in people
        if p.operator_score >= operator_threshold or p.angel_score >= angel_threshold
    ]

    os.makedirs("out", exist_ok=True)
    output_file = f"out/notion_import_{datetime.now().strftime('%Y-%m-%d')}.csv"
    export_to_notion_csv(qualified, output_file)

    print(f"\n✅ Done! Exported {len(qualified)} leads → {output_file}")
    print(f"   Operator threshold: {operator_threshold}")
    print(f"   Angel threshold: {angel_threshold}")


def main():
    """Main CLI entry point."""
    ap = argparse.ArgumentParser(prog="builder-harvester")
    sub = ap.add_subparsers(dest="cmd", required=True)

    # Harvest GitHub
    p_gh = sub.add_parser("harvest_gh")
    p_gh.add_argument("--topics", default="battery-management,iot-projects")
    p_gh.add_argument("--stars", type=int, default=100)
    p_gh.set_defaults(func=harvest_gh)

    # Run full pipeline
    p_run = sub.add_parser("run")
    p_run.add_argument("--threshold", default="operator:0.6,angel:0.7")
    p_run.set_defaults(func=run_pipeline)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
