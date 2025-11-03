"""Export functionality for Notion and other formats."""

import pandas as pd
from builder_harvester.models import Person


def export_to_notion_csv(people: list[Person], output_path: str):
    """
    Export Person records to Notion-compatible CSV.

    Args:
        people: List of Person objects to export
        output_path: Path to output CSV file
    """
    rows = []

    for person in people:
        # Build evidence summary (1-2 sentences)
        evidence_parts = []
        for ev in person.evidence[:3]:  # Max 3 pieces of evidence
            evidence_parts.append(ev.text)
        evidence_summary = ". ".join(evidence_parts)

        rows.append({
            "Name": person.name,
            "Primary URL": str(person.primary_url),
            "Operator Score": round(person.operator_score, 2),
            "Angel Score": round(person.angel_score, 2),
            "Evidence Summary": evidence_summary,
            "Last Activity": person.last_activity or "",
        })

    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)
