# builder-signal-harvester

**Goal:** Find technical operator-angels via Product Hunt/GitHub builder breadcrumbs.

**MVP I/O:** PH makers & GH users in → labeled leads out.

**Stack:** Python, httpx/requests, pandas; optional PH/GH APIs; LLM for angel-hint classification.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
```

Edit `.env`:
```
GITHUB_TOKEN=your_github_token_here
ANTHROPIC_API_KEY=your_anthropic_key_here
```

### 3. Run the Pipeline

```bash
# Full pipeline: harvest, score, merge, export
python -m builder_harvester.cli run --threshold operator:0.6,angel:0.7

# Harvest GitHub only
python -m builder_harvester.cli harvest_gh --topics battery-management,iot-projects --stars 100
```

### 4. Import to Notion

1. Open the generated CSV in `out/notion_import_YYYY-MM-DD.csv`
2. Import to your Notion database
3. Review and reach out to qualified leads

## Architecture

**Plugin-based harvesters:**
- `harvesters/gh.py` - GitHub repo owners and org members
- `harvesters/ph.py` - Product Hunt makers and commenters (TODO)

**Scoring:**
- Heuristic rules for auto-yes/auto-no angel signals
- LLM batch classification for borderline cases (Claude Haiku)
- Operator score based on repos, stars, domain relevance

**Identity resolution:**
- Match profiles across platforms using ≥2 fields
- Merge duplicates with cross-platform boost

**Export:**
- Notion CSV with minimal fields for manual review
- Audit logs for debugging missed leads

## Commands

```bash
# Harvest from Product Hunt (last 12 months)
python -m builder_harvester.cli harvest_ph --days 365

# Harvest from GitHub (by topics)
python -m builder_harvester.cli harvest_gh --topics battery-management,iot-projects,robotics

# Run all harvesters, score, merge, export
python -m builder_harvester.cli run --threshold operator:0.6,angel:0.7

# Export to Notion CSV
python -m builder_harvester.cli export --format notion --output out/notion_import.csv

# Debug a specific person
python -m builder_harvester.cli debug --name "John Doe"
```

## Configuration

**Environment variables (`.env`):**
- `GITHUB_TOKEN` - GitHub personal access token
- `PRODUCT_HUNT_TOKEN` - Product Hunt API token
- `ANTHROPIC_API_KEY` - Anthropic API key for Claude

**Thresholds:**
- `operator:0.6` - Minimum operator score to export
- `angel:0.7` - Minimum angel score to export
- Export if EITHER threshold is met (tiered approach)

## File Structure

```
builder-signal-harvester/
├── data/
│   ├── raw/          # API dumps (cached)
│   └── processed/    # Normalized records
├── docs/
│   └── plans/        # Design docs
├── out/              # Exports and logs
├── prompts/          # LLM prompts
├── src/
│   └── builder_harvester/
│       ├── harvesters/       # Plugin modules
│       ├── scoring.py        # Heuristics + LLM
│       ├── merging.py        # Deduplication
│       ├── export.py         # CSV generation
│       ├── models.py         # Pydantic schemas
│       └── cli.py            # CLI entry point
├── tests/            # Unit tests
└── requirements.txt
```

## Development

Run tests:
```bash
pytest tests/ -v
```

## Notes

- Start simple; bias toward precision over recall
- Store evidence snippets for all decisions
- Respect platform ToS and rate limits
- Public data only
