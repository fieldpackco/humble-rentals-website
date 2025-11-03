# Builder Signal Harvester - Design Document

**Date:** 2025-11-02
**Status:** Validated Design
**Project:** Fieldpack Fundraising - Operator-Angel Lead Generation

## Overview

Builder Signal Harvester is a lead generation system for finding technical operator-angels in the deep tech/battery/IoT/robotics/energy space for Fieldpack fundraising.

**Use Case:** Personal review of leads → Notion database → manual outreach. Run periodically/ad-hoc to discover emerging operator-angels.

**Target Personas:**
1. **Technical operator-angels** - Senior ICs/leaders at startups (CTOs, VPs Eng, founding engineers) in deep tech/IoT/energy who write angel checks
2. **Ecosystem influencers** - Writers, newsletter authors, community builders (like Packy McCormick) who invest and connect to operators

## System Architecture

### Core Workflow
1. **Harvest** - Pull data from Product Hunt and GitHub via APIs/scraping
2. **Score** - Classify operator strength and angel evidence separately using heuristics + LLM
3. **Merge** - Deduplicate people found on multiple platforms
4. **Export** - Push qualified leads to Notion for manual review and outreach

### Plugin Architecture
- Each data source is a harvester plugin (`harvester_ph.py`, `harvester_gh.py`) implementing a common interface
- Plugins use custom logic since each platform is different (PH GraphQL API vs GH REST API vs future Substack scraping)
- Easy to add new sources (Twitter/X, Substack, LinkedIn) without touching core logic

### Data Storage (Files-First)
- `data/raw/` - Raw JSON dumps from APIs (cached for replay/debugging)
- `data/processed/` - Normalized people records with scores and evidence
- `out/` - Final exports (CSV for Notion, audit logs)
- Only move to SQLite if file-based approach breaks

## Product Hunt Harvesting

### Triggers for Interesting Makers/Hunters
- **Makers** with ≥1 product launch tagged with hardware/IoT/robotics/devtools/climate in last 12 months
- Boost score significantly if product hit top-10 daily ranking
- **Active commenters** with ≥5 comments on relevant products in last 6 months

### Data Extracted
- Name, profile URL, bio
- Launched products (names, descriptions, rankings, dates)
- Comment history on relevant products
- Social links (Twitter, LinkedIn, personal website)

### Implementation
- Use Product Hunt GraphQL API (v2) at `api.producthunt.com/v2/api/graphql`
- Query for products by topic tags, extract makers and engaged commenters
- Filter by date ranges and engagement thresholds
- Cache raw responses in `data/raw/ph_YYYY-MM-DD.json`

### Privacy Note
API has commercial use restrictions, may need to contact PH if this scales beyond personal use.

## GitHub Harvesting

### Triggers for Interesting Developers
- **Repo owners** with ≥100 stars in relevant topics: `battery-management`, `lithium-ion-batteries`, `iot-projects`, `robotics`, `embedded-systems`, `power-management`, `energy-storage`
- **Organization members** at companies building in deep tech/hardware/IoT/energy (detected from org membership)
- **Active maintainers** with recent commits in last 6 months

### Data Extracted
- Name, username, profile URL, bio
- Owned repositories (names, descriptions, stars, topics, last update)
- Organization memberships
- Social links (Twitter, LinkedIn, blog/website from profile or repo homepages)
- Pinned repositories (often showcase best work)

### Implementation
- Use GitHub REST API for user profiles, repos, orgs, topics
- Search repositories by topics, extract owners and top contributors
- Query organization members for known IoT/robotics/energy companies
- Cache raw responses in `data/raw/gh_YYYY-MM-DD.json`

### Angel Signal Detection
- Scan bio for keywords: "angel", "investor", "investing in", "advisor", "checks", "$XkX"
- Check pinned repos for investment-related projects

## Scoring & Classification

### Two-Stage Filtering Approach

**Stage 1 - Heuristic Rules (fast, free):**
- **Auto-yes angel signals:** Bio contains "angel investor", "investing in", "advisor", "check size", "$Xk checks"
- **Auto-no signals:** Bio only contains "seeking investors", "looking for funding", "we're hiring" (fundraising, not investing)
- **Auto-no low quality:** No relevant domain activity, spam accounts
- **Borderline cases:** Send to LLM for classification

**Stage 2 - LLM Classification (batched):**
- Collect 10-20 borderline profiles
- Single prompt asking for JSON array of classifications
- Use GPT-4o-mini or Claude Haiku (cheap, fast enough)
- Extract: `operator_score` (0-1), `angel_score` (0-1), `evidence` snippets

### Scoring Components
- `operator_score` based on: launches/repos in domain, stars/rankings, recency, org affiliation
- `angel_score` based on: bio signals, investment mentions, advisory language
- `domain_match` bonus for battery/IoT/robotics/energy specificity
- `cross_platform_boost` if found on both PH and GH

### Export Criteria (Tiered)
- Export if `operator_score >= 0.6 OR angel_score >= 0.7`
- User manually prioritizes during Notion review based on which matters more for each lead

### Cost Estimate
Approximately $0.50-$2 per run for ~50-100 LLM classifications.

## Identity Resolution & Deduplication

### Matching Logic
- **Require ≥2 matching fields** to merge records (avoid false positives from common names)
- Matching fields: normalized name, email, LinkedIn URL, Twitter handle, personal website
- Normalize names: lowercase, remove middle initials, handle unicode

### Merge Strategy
When same person found on PH and GH:
- Create single canonical record with `canonical_id`
- Combine evidence from both sources
- Take max of individual scores, apply cross-platform boost
- Keep all source URLs for attribution

### Example
```
PH: "Jane Smith" | linkedin.com/in/janesmith | launched BatteryOS
GH: "Jane R Smith" | linkedin.com/in/janesmith | owns battery-monitoring repo (500 stars)
→ Merged: operator_score=0.8, angel_score=0.4, evidence from both platforms
```

## Error Checking & Debugging

### Audit Logging (Structured JSON Logs)
Every person considered gets logged with:
- `person_id`, `name`, `sources` (PH/GH/both)
- `operator_score`, `angel_score`, `final_decision` (exported/filtered)
- `evidence_snippets`, `filter_reasons`
- `timestamp`, `cost_estimate`

Logs saved to `out/audit_YYYY-MM-DD.jsonl` (newline-delimited JSON, easy to grep).

### All-Candidates CSV Export
Separate file `out/all_candidates_YYYY-MM-DD.csv` with everyone scored, even below threshold.

Columns: name, operator_score, angel_score, exported (yes/no), primary_url, evidence_summary

Allows manual searching: "Why didn't we find John Doe?"

### Reverse Lookup Workflow
1. Discover a missed lead manually
2. Search `all_candidates.csv` for their name
3. If found but low score → check evidence, adjust scoring weights
4. If not found at all → check raw data dumps, verify they match PH/GH triggers
5. Update heuristics/prompts based on findings

### Replay Capability
- Raw API dumps in `data/raw/` persist for 90 days
- Can re-run scoring with different thresholds without re-crawling
- Useful for tuning before going live

## Notion Export & Output Format

### Minimal Notion Fields
- **Name** - Full name
- **Primary URL** - Best link to profile (PH, GH, or personal site)
- **Operator Score** - 0.0 to 1.0
- **Angel Score** - 0.0 to 1.0
- **Evidence Summary** - 1-2 sentence summary of key signals
- **Last Activity** - Most recent PH launch or GH commit date

### Export Method
- Generate CSV file `out/notion_import_YYYY-MM-DD.csv`
- Manual import to Notion (copy/paste or CSV import)
- Simple, no API keys needed, user controls when leads appear

### Future Enhancement (Optional)
- Add Notion API integration for direct sync
- Would need Notion database ID and API token in `.env`
- Only build if manual CSV import becomes painful

### Evidence Summary Format
```
"Launched BatteryOS (PH #3 daily). Maintains battery-monitoring repo (500⭐). Bio: 'advisor to energy startups'"
```

## CLI Commands & Workflow

### Core Commands
```bash
# Harvest from Product Hunt (last 12 months)
python -m builder_harvester harvest --source ph --days 365

# Harvest from GitHub (by topics)
python -m builder_harvester harvest --source gh --topics battery-management,iot-projects,robotics

# Run all harvesters, score, merge, export
python -m builder_harvester run --threshold operator:0.6,angel:0.7

# Export to Notion CSV
python -m builder_harvester export --format notion --output out/notion_import.csv

# Debug a specific person
python -m builder_harvester debug --name "John Doe"
```

### Typical Workflow
1. Run `harvest --source ph` and `harvest --source gh` (can run separately or together)
2. System scores all candidates, applies heuristics + LLM classification
3. Deduplicates cross-platform matches
4. Exports qualified leads to CSV + audit logs
5. User imports CSV to Notion, reviews, and reaches out
6. If missed lead found, check `all_candidates.csv` and audit logs to improve

### Configuration
- `.env` file for API keys (PH token, GH token, OpenAI/Anthropic key)
- `config.yaml` for thresholds, topic lists, scoring weights (optional, can start with hardcoded defaults)

## Technical Stack

### Dependencies
- `httpx` - HTTP client for API calls
- `pandas` - Data processing and CSV export
- `pydantic` - Data validation and models
- `openai` or `anthropic` - LLM classification
- `python-dotenv` - Environment variable management

### File Structure
```
builder-signal-harvester/
├── data/
│   ├── raw/          # API dumps
│   └── processed/    # Normalized records
├── docs/
│   └── plans/        # Design docs
├── out/              # Exports and logs
├── prompts/          # LLM prompts
├── src/
│   └── builder_harvester/
│       ├── __init__.py
│       ├── cli.py
│       ├── harvesters/
│       │   ├── base.py       # Base harvester interface
│       │   ├── ph.py         # Product Hunt
│       │   └── gh.py         # GitHub
│       ├── scoring.py        # Heuristics + LLM classification
│       ├── merging.py        # Deduplication
│       ├── export.py         # Notion CSV generation
│       └── models.py         # Pydantic data models
├── tests/            # Unit tests
├── .env.example      # Example environment variables
├── requirements.txt
└── README.md
```

## Success Metrics

### Quality Metrics
- **Precision** - % of exported leads you'd actually reach out to
- **Recall** - % of known operator-angels in your domain that appear in results
- **Acceptance rate** - % of leads you contact after Notion review

### Operational Metrics
- **Cost per lead** - LLM + API costs per qualified lead
- **Time to results** - End-to-end runtime for a full harvest
- **Coverage** - Number of PH makers + GH developers analyzed per run

### Improvement Loop
- Track missed leads via reverse lookup
- Tune scoring thresholds based on Notion review feedback
- Update LLM prompts when classification errors found
- Add new data sources when operator-angel patterns emerge elsewhere

## Future Enhancements

### Data Sources (Extensible Plugin Architecture)
- Twitter/X - Track tech influencers, newsletter authors
- Substack - Find writers in deep tech/climate/energy
- LinkedIn - Enrich profiles with job history, connections
- Crunchbase - Cross-reference with known angel portfolios

### Automation
- Notion API direct sync
- Weekly scheduled runs with email digest
- Slack notifications for high-confidence leads
- Active learning loop for borderline cases

### Analytics
- Streamlit UI for review queue
- Score distribution analysis
- Domain clustering (IoT vs battery vs robotics)
- Network analysis (who knows who)

## Notes

- Start simple, bias toward precision over recall
- Store evidence snippets for all decisions
- Respect platform ToS and rate limits
- Public data only, offer opt-out mechanism
- YAGNI ruthlessly - build features when needed, not speculatively
