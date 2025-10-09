# Screenshot Tool - Now Available Globally

## What Was Done

Added the screenshot tool from Fieldpack to the central `~/.agent-learnings/` repository so it's available across all projects and all machines.

## Changes Made

### 1. Added to Central Repository
**Location**: `~/.agent-learnings/tools/`

Files added:
- `screenshot.js` - The actual screenshot tool (Playwright-based)
- `package.json` - Playwright dependency
- `README.md` - Complete documentation

### 2. Updated Playbook
**Location**: `~/.agent-learnings/playbook.md`

Added two new sections:

**a) Failure Mode #13 - Tool Over-Engineering**
```markdown
13. Tool Over-Engineering – Working simple solution replaced with complex CLI system;
    preference for "enterprise" patterns over pragmatic solutions. Validate actual
    requirements before adding abstraction layers.
```

**b) Tool-Specific Policies Section**

Complete policy documenting the Codex over-engineering incident:
- What happened (complex preset system, API errors, user rejection)
- The rule (environment variables ONLY, no CLI args)
- Why it matters (simplicity, avoiding API policy triggers)
- How to use it properly

### 3. Logged to Learnings
Added to `learnings.jsonl`:
```json
{"timestamp":"2025-10-09T18:11:48Z","source":"dual_agent","type":"manual","message":"Added screenshot tool to central repo and added Tool Over-Engineering (failure mode #13) to playbook"}
```

### 4. Pushed to GitHub
**Repository**: https://github.com/runchal/agent-learnings
**Commit**: `e48ecb2`

## How to Use Across All Projects

### Option 1: Use Directly from Central Location (Recommended)

```bash
cd ~/.agent-learnings/tools
npm install  # First time only
npm run install-browsers  # First time only

# Then use
URL=http://localhost:3000 COUNT=3 SESSION=debug node screenshot.js
```

### Option 2: Symlink to Project Directory

```bash
# From any project root
mkdir -p tools
ln -s ~/.agent-learnings/tools/screenshot.js tools/screenshot.js
ln -s ~/.agent-learnings/tools/package.json tools/package.json
ln -s ~/.agent-learnings/tools/README.md tools/README-screenshot.md

# Then use from project
cd tools
URL=http://localhost:3000 COUNT=3 SESSION=debug node screenshot.js
```

### Option 3: Use Absolute Path from Anywhere

```bash
# From anywhere
URL=http://localhost:3000 COUNT=3 SESSION=mobile-check node ~/.agent-learnings/tools/screenshot.js
```

## Cross-Machine Setup

When you clone `agent-learnings` on a new machine:

```bash
# Clone the repo
git clone https://github.com/runchal/agent-learnings.git ~/.agent-learnings

# Install screenshot tool dependencies
cd ~/.agent-learnings/tools
npm install
npm run install-browsers

# Test it works
URL=http://localhost:3000 COUNT=1 SESSION=test node screenshot.js
```

## Environment Variables

Available configuration (all optional):

| Variable | Default | Description |
|----------|---------|-------------|
| `URL` | `http://localhost:3001` | Target URL |
| `COUNT` | `5` | Number of screenshots |
| `DELAY` | `1000` | Delay between shots (ms) |
| `WAIT` | `2000` | Initial wait (ms) |
| `WIDTH` | `1440` | Viewport width |
| `HEIGHT` | `900` | Viewport height |
| `SESSION` | auto | Session name |
| `OUTPUT_DIR` | `tools/screenshots` | Output directory |
| `FULLPAGE` | `false` | Full page screenshot |

## Examples

```bash
# Mobile viewport
URL=http://localhost:3000 WIDTH=390 HEIGHT=844 SESSION=mobile node ~/.agent-learnings/tools/screenshot.js

# Desktop full page
URL=http://localhost:3000 WIDTH=1920 HEIGHT=1080 FULLPAGE=true SESSION=desktop node ~/.agent-learnings/tools/screenshot.js

# Animation debugging (multiple states)
URL=http://localhost:3000 COUNT=10 DELAY=500 WAIT=2000 SESSION=animation node ~/.agent-learnings/tools/screenshot.js

# Quick single shot
URL=http://localhost:3000 COUNT=1 SESSION=quick node ~/.agent-learnings/tools/screenshot.js
```

## What NOT to Do

❌ **Don't create CLI argument systems**:
```bash
# WRONG - Will trigger API policy errors
node screenshot.js --preset mobile --session test
npm run screenshot:stealth
```

✅ **Do use environment variables**:
```bash
# RIGHT - Simple and safe
URL=http://localhost:3000 WIDTH=390 SESSION=test node screenshot.js
```

## Benefits

**Before**:
- Tool existed only in Fieldpack project
- Had to copy/paste to other projects
- Different versions across projects
- Not available on new machines until copied

**After**:
- Single source of truth in `~/.agent-learnings/tools/`
- Available across all projects immediately
- Synced via GitHub across all machines
- Updated once, benefits everywhere
- Part of agent knowledge system

## Integration with Dual Agent

When agents work in any project, they can now:

1. Read playbook → see screenshot tool policy
2. Know tool is available at `~/.agent-learnings/tools/screenshot.js`
3. Use simple environment variable syntax
4. Never suggest complex CLI argument systems
5. Document visual changes with screenshots

The tool is now part of the central agent knowledge and automatically available everywhere!
