# Dual Agent - Local RL for Agent Collaboration

A system for enabling Claude Code and OpenAI Codex to collaborate across multiple projects with shared learnings.

## Problem Solved

When working on multiple apps, each agent session operates in isolation. Learnings from one project (failure modes, guardrails, best practices) don't propagate to other projects. This is essentially building **local reinforcement learning** where agents learn from their collective experiences across all your projects.

## Architecture

```
~/.agent-learnings/              # Central knowledge repository (git-tracked)
├── playbook.md                  # Canonical collaboration playbook
├── learnings.jsonl              # Structured logs of all learnings
├── claude-init.md               # Context injected into Claude sessions
└── codex-init.md                # Context injected into Codex sessions

~/bin/dual_agent                 # CLI orchestration tool

~/.zshrc                         # Shell wrappers for seamless integration

Per-project structure:
/apps/your-project/
├── .agent/
│   ├── agent-collab-playbook.md@    # Symlink → ~/.agent-learnings/playbook.md
│   ├── AGENT-EXCHANGE.md            # Project-specific agent collaboration log
│   └── session-context.json         # Current session metadata
└── CLAUDE.md                        # Project instructions (auto-updated)
```

## How It Works

### Transparent Initialization

When you run `claude` or `codex` in any directory:

1. **Shell wrapper** intercepts the command
2. **dual_agent init** runs automatically if `.agent/` doesn't exist
3. Creates project structure with symlinks to central knowledge
4. Injects dual-agent context into `CLAUDE.md` or Codex config
5. Launches the actual agent with full context

### Both Agents Are Aware

Each agent automatically knows:
- **Peer agent**: Who the other agent is and how to call them
- **Playbook**: All collaboration guardrails and workflows
- **History**: Learnings from all previous projects
- **Role**: Whether they're Primary (implement) or Secondary (advise/test)

### Knowledge Propagation

When agents discover something new:
1. Document in project's `AGENT-EXCHANGE.md`
2. Run `dual_agent learn "description"` to log to central repo
3. Future projects automatically see these learnings via symlinked playbook

## Usage

### Basic Commands

```bash
# Initialize dual-agent mode (usually automatic via shell wrapper)
dual_agent init claude
dual_agent init codex

# Check current project status
dual_agent status

# Log a new learning to central repository
dual_agent learn "Always validate numeric bounds before processing"

# Sync learnings from current project (TODO: full implementation)
dual_agent sync

# Show help
dual_agent help
```

### Shell Wrappers (Auto-configured)

Your `~/.zshrc` now has wrappers that make this seamless:

```bash
# Just use claude/codex as normal - dual_agent initializes automatically
cd /apps/new-project
claude               # Automatically sets up dual-agent mode
codex                # Automatically aware of Claude as peer
```

### Workflow Example

```bash
# Start Claude in a new project
cd /apps/my-new-app
claude

# Claude automatically:
# - Reads ~/.agent-learnings/playbook.md
# - Sees learnings from all your previous projects
# - Knows Codex is available as peer
# - Creates .agent/AGENT-EXCHANGE.md for this project

# Later, call Codex for review
codex "Review the implementation in src/api.ts"

# Codex automatically:
# - Reads same central playbook
# - Knows Claude is primary agent
# - Reviews Claude's work
# - Documents response in AGENT-EXCHANGE.md
```

## Central Knowledge Repository

The `~/.agent-learnings/` directory is git-tracked so you can:

- **Version control** your agent learnings
- **Backup** to remote repository
- **Share** across machines via git
- **Review** what agents have learned over time

```bash
cd ~/.agent-learnings
git log               # See learning evolution
git remote add origin <your-repo>
git push              # Backup learnings
```

## Key Features

### 1. Automatic Context Injection

Every agent session gets:
- Full collaboration playbook
- Historical learnings from all projects
- Awareness of peer agent
- Structured logging template

### 2. Symlinked Playbook

All projects link to the same central `playbook.md`:
- Update once, affects all projects
- No playbook drift between projects
- Single source of truth

### 3. Structured Learning Format

`learnings.jsonl` uses JSONL format:
```json
{"timestamp":"2025-10-09T17:00:00Z","source":"ocr_engine","type":"failure_mode","message":"Visual validation fails on rotated PDFs"}
{"timestamp":"2025-10-09T17:05:00Z","source":"fieldpack","type":"guardrail","message":"Always test RTL layouts for localization"}
```

### 4. Project Isolation with Shared Knowledge

Each project has its own `AGENT-EXCHANGE.md` log, but all share:
- Same guardrails
- Same failure modes
- Same best practices

## Agent-Exchange Template

Projects get a v2.0 template with YAML front matter:

```yaml
---
id: AEX-001
status: drafting
primary_agent: claude
secondary_agent: codex
priority: medium
timebox_hours: 4
risk: low
consensus_cycles: 0
files_write_scope:
  - "src/**/*.ts"
---
```

## Current Limitations & TODOs

- [ ] Full `dual_agent sync` implementation (currently manual)
- [ ] Automatic extraction of learnings from AGENT-EXCHANGE.md
- [ ] Conflict detection when multiple agents work in same repo
- [ ] Dashboard/UI for viewing all learnings
- [ ] Structured failure mode categories/tags
- [ ] Performance metrics tracking

## Implementation Status

✅ Central knowledge repository
✅ CLI tool (`dual_agent`)
✅ Shell wrappers for transparent init
✅ Context injection into CLAUDE.md
✅ Symlinked playbook
✅ AGENT-EXCHANGE.md template
✅ Session metadata tracking
⚠️ Learning extraction (basic, needs enhancement)
⚠️ Codex config injection (basic, may need tuning)

## Files Created

```
~/.agent-learnings/
├── playbook.md              # Full collaboration playbook
├── claude-init.md           # Claude session context
├── codex-init.md            # Codex session context
└── learnings.jsonl          # Structured learning log

~/bin/dual_agent             # CLI tool (executable)

~/.zshrc                     # Updated with shell wrappers
```

## Next Steps

1. **Test the system** - Open a new terminal and try `claude` in various directories
2. **Source .zshrc** - Run `source ~/.zshrc` to activate wrappers in current shell
3. **Backup learnings** - Consider pushing `~/.agent-learnings/` to a private git repo
4. **Enhance sync** - Implement full learning extraction from AGENT-EXCHANGE.md
5. **Monitor evolution** - Watch how the playbook evolves across projects

## Meta-Analysis Notes

This system implements:
- **Federated learning**: Knowledge from multiple "clients" (projects) to central "server" (learnings repo)
- **Reinforcement learning**: Agents improve via post-mortems and failure mode documentation
- **Context persistence**: Learnings survive across sessions and projects
- **Transparency**: All agent collaboration is logged and auditable

The playbook's "Common Failure Modes" section (12 items) will grow as agents discover new edge cases across your projects.
