# Playbook Update Architecture - Fixed

## The Problem You Identified

The playbook said "update this playbook when guardrails fail" but agents couldn't figure out how to actually do it due to:
1. Confusion about symlink restrictions
2. No explicit instructions on HOW to edit it
3. Theoretical concerns about sandbox/permissions

This broke the real-time learning loop - agents would discover issues but couldn't update the playbook, requiring manual intervention.

## What Was Fixed

### 1. Verified Edit Tool Works

Tested and confirmed: The Edit tool CAN write to `~/.agent-learnings/playbook.md` directly.

**Permissions**:
```bash
-rw-r--r-- /Users/amitrunchal/.agent-learnings/playbook.md
```
Normal read/write, no restrictions.

### 2. Added Explicit Instructions to Playbook

**Location**: `~/.agent-learnings/playbook.md` (section: "How to Update This Playbook")

New section includes:
- **Clear statement**: "You CAN and SHOULD update this playbook directly"
- **Exact syntax**: `Edit: /Users/amitrunchal/.agent-learnings/playbook.md`
- **When to update**: New failure modes, tool-specific issues, systematic gaps
- **How to commit**: `cd ~/.agent-learnings && git add playbook.md && git commit -m "..." && git push`
- **Why it works**: Symlinks propagate changes immediately to all projects

### 3. Updated Global Agent Configs

**Claude**: `~/.claude/CLAUDE.md`
**Codex**: `~/.codex/INSTRUCTIONS.md`

Both now include "Updating the Playbook" section with:
- Explicit permission to edit
- Exact Edit tool syntax
- Commit workflow
- Real-time learning explanation

## How It Works Now

### Agent Workflow (When Discovering New Failure Mode)

```
1. Agent encounters issue (e.g., dynamic range not tested)
   ↓
2. Logs in AGENT-EXCHANGE.md post-mortem
   ↓
3. Reads playbook section "How to Update This Playbook"
   ↓
4. Uses Edit tool on /Users/amitrunchal/.agent-learnings/playbook.md
   ↓
5. Adds to "Common Failure Modes" section (e.g., #14: ...)
   ↓
6. Commits and pushes:
   cd ~/.agent-learnings
   git add playbook.md
   git commit -m "Add failure mode #14: XYZ"
   git push
   ↓
7. Change instantly propagates to all projects via symlinks
   ↓
8. Future agent sessions in ANY project see the new guardrail
```

### Real-Time Learning Restored

**Before fix**:
- Agent discovers issue → documents in AGENT-EXCHANGE.md
- User notices → manually updates playbook
- Push to GitHub
- Other projects pull to get update
- **Delay**: Hours to days

**After fix**:
- Agent discovers issue → documents in AGENT-EXCHANGE.md
- Agent directly updates playbook → commits → pushes
- **Delay**: Seconds (instant via symlinks)

## Example: Adding Failure Mode #14

If an agent discovers a new systematic failure:

```bash
# Agent uses Edit tool
Edit: /Users/amitrunchal/.agent-learnings/playbook.md

# Adds to Common Failure Modes:
14. **Animation State Gaps** – Animations tested only at start/end states;
    mid-transition states cause layout breaks. Capture multiple animation
    frames with screenshot tool to verify all states.

# Commits
cd ~/.agent-learnings
git add playbook.md
git commit -m "Add failure mode #14: Animation State Gaps"
git push
```

Done. All projects instantly have the new guardrail.

## Technical Details

### Symlink Resolution

```
Project A: .agent/agent-collab-playbook.md → ~/.agent-learnings/playbook.md
Project B: .agent/agent-collab-playbook.md → ~/.agent-learnings/playbook.md
Project C: .agent/agent-collab-playbook.md → ~/.agent-learnings/playbook.md
                                              ↑
                                   All point to same file
                                   Edit once, change everywhere
```

### File Permissions

```bash
$ ls -la ~/.agent-learnings/playbook.md
-rw-r--r--  1 amitrunchal  staff  10585 Oct  9 11:11 playbook.md
           ↑
        User can write
```

No sandbox restrictions apply because:
- File is in user's home directory
- Standard file permissions (not read-only)
- Edit tool has necessary access

### Git Workflow

```bash
# Agents run this after updating playbook
cd ~/.agent-learnings
git add playbook.md
git commit -m "Add failure mode: [description]"
git push

# Pushes to: https://github.com/runchal/agent-learnings
# Other machines pull to sync
```

## Benefits

### 1. Real-Time Learning
- Issue discovered → Playbook updated → All projects benefit
- No manual intervention needed
- Learning propagates in seconds, not days

### 2. Distributed Intelligence
- Each agent session contributes to collective knowledge
- Failure modes from Project A prevent issues in Project B
- System gets smarter with every session

### 3. Reduced Toil
- User doesn't manually update playbook
- Agents handle documentation automatically
- Focus on reviewing/approving, not transcribing

### 4. Audit Trail
- All playbook changes in git history
- See what was learned and when
- Revert if needed

## What Changed

**Files Modified**:
1. `~/.agent-learnings/playbook.md` - Added "How to Update This Playbook"
2. `~/.claude/CLAUDE.md` - Added "Updating the Playbook" section
3. `~/.codex/INSTRUCTIONS.md` - Added "Updating the Playbook" section
4. `~/.agent-learnings/learnings.jsonl` - Logged the fix

**Commits**:
- Central repo: `8ef777c` - "Add explicit instructions for agents to update playbook directly"

## Verification

To test this works:

1. Start Claude in any dual-agent project
2. Ask: "Read the playbook section on how to update it"
3. Claude should respond with clear understanding it CAN edit the central file
4. Ask: "Add a test failure mode #99 to the playbook"
5. Claude should use Edit tool on `/Users/amitrunchal/.agent-learnings/playbook.md`
6. Verify change appears in all projects via symlinks

## Future Improvements

Potential enhancements (not critical):

1. **Validation**: Before pushing, validate playbook markdown syntax
2. **Review queue**: Optional pre-push review for playbook changes
3. **Categorization**: Auto-categorize learnings by type (failure mode, tool policy, etc.)
4. **Analytics**: Track which failure modes are added most often

But current system works - agents can learn in real-time without blocking on user approval.

## Bottom Line

**Before**: Broken instruction ("update playbook") with no mechanism to actually do it.
**After**: Clear instructions + verified tooling = real-time agent learning.

The local RL system now works as intended: agents learn from failures and immediately share that knowledge across all projects.
