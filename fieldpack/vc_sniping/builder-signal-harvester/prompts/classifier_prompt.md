# Builder→Angel Classification

You are analyzing technical profiles to identify potential angel investors in deep tech/battery/IoT/robotics/energy.

For each profile, determine:
1. **operator_score** (0.0-1.0): How strong is their technical operator background in relevant domains?
2. **angel_score** (0.0-1.0): How likely are they to make angel investments?
3. **evidence**: Key signals supporting your scores (2-3 bullet points)

## Scoring Guidelines

**Operator Score:**
- 0.8-1.0: Senior technical leader at relevant company, multiple successful projects
- 0.5-0.7: Active technical contributor, domain expertise visible
- 0.2-0.4: Some technical activity, less clear relevance
- 0.0-0.1: No technical signals

**Angel Score:**
- 0.8-1.0: Explicit mention of investing, advisor with checks, portfolio visible
- 0.5-0.7: "Open to advising", "helping founders", implicit investment hints
- 0.2-0.4: General advisory mentions, unclear if invests
- 0.0-0.1: No investment signals

## Input Format

You'll receive an array of profiles with: name, bio, repos/products, social links.

## Output Format

Return valid JSON array:
```json
[
  {
    "source_id": "username",
    "operator_score": 0.8,
    "angel_score": 0.4,
    "evidence": [
      "Maintains battery-monitor repo (500 stars) with recent commits",
      "Bio mentions 'CTO @ BatteryCo'",
      "Topics: battery-management, IoT, embedded-systems"
    ]
  }
]
```
