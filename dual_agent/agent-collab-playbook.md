# Dual-Agent Collaboration Playbook

## Overview
Portable operating guide for any repository where OpenAI Codex and Claude Code collaborate. Drop this file into the project root so both agents share the same guardrails, regardless of which CLI initiates the session. Pair it with the latest `AGENT-EXCHANGE.md` template (v2.0+) to capture every request.

## Setup Checklist
1. Copy `AGENT-EXCHANGE.md` (Template v2.0) into the repo and link it from contributor docs.
2. Commit automation helpers (`scripts/new-agent-entry.sh`, `scripts/agent.sh`) so either agent can bootstrap entries and cross-call the other CLI.
3. Define the command/tool allowlist and prohibited operations in `AGENTS.md` (include diff-size threshold and approval rules).
4. Capture environment parity: devcontainer/Docker tag, language runtimes, package manager versions, and OS notes.
5. Store reusable prompts and system messages under `prompts/` (version-controlled) for reproducibility.

## Role Principles
- Agents designate a **Primary** (implements) and **Secondary** (advises/tests) per entry; swap roles as needed, but log the primary in front matter.
- Secondary agents must not modify files outside the logged `files_write_scope`.
- Users remain the escalation point and final approver.

## Guardrails & Reproducibility
- Pin models, endpoints, temperature/top-p, toolchain versions, and YAML front-matter metadata (`id`, `status`, `priority`, `timebox`, `risk`, `consensus_cycles`, etc.) inside each entry.
- Record runtime image hashes or devcontainer tags so environments stay aligned.
- Archive the exact prompts/system modifiers used for planning and implementation.
- Adhere to the repository command allowlist; anything outside requires explicit user approval.
- Enumerate dynamic input variants (content length extremes, numeric bounds, asset sizes) and log them under `data_bounds` before implementation.
- Run guardrail checks for accessibility, performance, localization, and security during consensus and document outcomes.
- When guardrails fail, update this playbook and AGENTS.md with new checklists or tooling, and reference the post-mortem entry.

## Branching & File Locks
- Create a dedicated branch per entry: `agent/<primary>/<slug>`.
- Declare write scope globs to prevent accidental overlaps.
- Log conflicts when multiple entries touch the same paths and re-sequence work before merging.
- Reviews focus on diffs (`git diff`, PR view); avoid full-file rewrites unless justified in the log.

## Workflow Loop
1. **Log Request** – Open a new entry (status `drafting`) with YAML front matter and the user’s constraints.
2. **Secondary Proposal** – Secondary agent drafts approach, assumptions, acceptance criteria, and a failing/regression test plan.
3. **Primary Response** – Primary evaluates the plan, flags concerns, and begins by implementing or updating the failing test.
4. **Consensus Check** – Iterate proposal/response up to two cycles. Escalate unresolved ❌ disagreements to the user with pros/cons.
5. **Implement & Verify** – Primary commits code within scope, references tests, SBOM/secret-scan artifacts, and shares diff links. Secondary reviews the diff only.
6. **User Decision** – User records the final call once CI (lint/type/unit/e2e/secret-scan/license/sbom) passes. `[HOTFIX]` entries may defer some gates but must backfill within 24 hours.
7. **Post-Mortem Trigger** – If a defect slips past both agents, log a post-mortem (root cause, missed guardrail, how to prevent recurrence) directly in the entry’s 'Missed Scenario Review', and update this playbook/AGENTS.md if new guardrails are required.

## Testing & CI Expectations
- Acceptance criteria and initial failing tests originate from the secondary agent; the primary starts work by making the test meaningful.
- CI must cover linting, unit, e2e, secret scanning, licence compliance, and SBOM generation before approval.
- Flag diff-size overruns (set repo threshold) and document rationale before requesting review.
- Capture CI run URLs or artifact paths inside the entry for traceability.

## Security & Secrets
- Ban editing `.env*`, credential stores, or deploying unreviewed scripts.
- Run `gitleaks detect --no-git --staged` (or repo-specific secret scanner) plus license/SBOM checks on every branch prior to user approval.
- Record rollback plans, impact, and risk rating per entry; use `ci_backfill_deadline` for `[HOTFIX]` work.

## Escalation & Edge Cases
- **Timebox Enforcement**: Respect the `timebox_hours` field; set status to `timebox-exceeded` if overrun and renegotiate scope before continuing.
- **Prototype vs Production**: Mark `Code Location: prototype/<folder>`, populate `migrates_from`, and open a follow-up entry for production roll-out.
- **Hotfixes**: Add `[HOTFIX]` prefix, record `ci_backfill_deadline`, document post-facto CI, and schedule a retrospective.
- **Parallel Work**: When entries conflict, freeze lower-priority work until the primary finishes or expands the write scope explicitly.

## Tooling Shortcuts
- `./scripts/new-agent-entry.sh "Request Title"` – Prepends a v2.0 entry skeleton with YAML front matter (edit for specifics).
- `./scripts/agent.sh print "Prompt"` – Wrapper that calls whichever CLI is available (`CLAUDE_BIN`, `CODEX_BIN`) for quick feedback.
- `./scripts/validate-write-scope.sh AEX-###` – Verifies the current branch diff stays inside the declared `files_write_scope`.
- `./scripts/capture-doc-screens.sh [url]` – Uses `npx capture-website` to capture desktop/mobile screenshots into `docs/screens/`; run after local preview to document UI changes.
- Add project-specific helpers (e.g., `agent-plan.sh`, `agent-impl.sh`) for consistent plan/implementation prompts if needed.

## Archiving & Knowledge Transfer
- Move closed entries older than 90 days into `AGENT-EXCHANGE-ARCHIVE.md`, grouped by subsystem, and cross-link to ADRs.
- Retain prompt archives, CI artifacts, and SBOM reports referenced in entries for future audits.
- Summaries in release notes should reference corresponding entry IDs (`AEX-###`) for traceability.

## Common Failure Modes
1. **Dynamic Range Gaps** – Feature tested with a single content snapshot; mitigate by logging `data_bounds` and validating extremes.
2. **Accessibility Oversights** – Visual fixes lack keyboard/screen-reader verification; add specific acceptance criteria and tooling (e.g., axe, VoiceOver).
3. **Performance Regression** – Micro-optimizations ignore worst-case data size; profile with representative loads before approval.
4. **Localization Drift** – Copy lengths or RTL layouts untested; capture translations and layout bounds for validation.
5. **Security/Config Mismatch** – Environment assumptions deviate (API keys, feature flags, rate limits); document config expectations and test toggles.
6. **Data Freshness / Temporal Drift** – Fixes validated on stale datasets or missing future timestamps; test with current and forward-looking data.
7. **State Synchronization** – Frontend changes ignore backend/API state transitions (loading, error, retry); map state flow early.
8. **Feature Flag Leakage** – Work assumes default flag states; annotate required flags and test both on/off.
9. **Tooling Blind Spots** – Snapshot/visual regression tools not run; record outputs in Implementation & Evidence.
10. **User Journey Interruptions** – Specific segments (mobile, keyboard-only, RTL) untested; verify alternate platforms/inputs.
11. **Process Drift** – Hotfix or prototype shortcuts not backfilled; schedule follow-up entries and note deviations.
12. **Cross-Agent Miscommunication** – Consensus summaries omit unresolved concerns; ensure guardrail checklist mirrors every comment.