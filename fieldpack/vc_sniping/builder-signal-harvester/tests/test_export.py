import pandas as pd
from builder_harvester.export import export_to_notion_csv
from builder_harvester.models import Person, Evidence


def test_export_to_notion_csv(tmp_path):
    """Test CSV export for Notion."""
    people = [
        Person(
            person_id="test1",
            name="Jane Smith",
            primary_url="https://github.com/janesmith",
            sources=["github"],
            operator_score=0.85,
            angel_score=0.40,
            evidence=[
                Evidence(source="github", text="500 stars on battery-monitor", url="https://github.com/repo", timestamp="2025-01-01")
            ],
            last_activity="2025-01-15",
        ),
        Person(
            person_id="test2",
            name="John Doe",
            primary_url="https://producthunt.com/@johndoe",
            sources=["producthunt"],
            operator_score=0.65,
            angel_score=0.75,
            evidence=[
                Evidence(source="producthunt", text="Launched IoT product #3 daily", url="https://producthunt.com/product", timestamp="2025-02-01")
            ],
            last_activity="2025-02-01",
        ),
    ]

    output_file = tmp_path / "notion_export.csv"
    export_to_notion_csv(people, str(output_file))

    # Verify CSV contents
    df = pd.read_csv(output_file)
    assert len(df) == 2
    assert list(df.columns) == ["Name", "Primary URL", "Operator Score", "Angel Score", "Evidence Summary", "Last Activity"]
    assert df.iloc[0]["Name"] == "Jane Smith"
    assert df.iloc[0]["Operator Score"] == 0.85
    assert "500 stars" in df.iloc[0]["Evidence Summary"]
