# Auto-Loading Playbook - Configuration

## What Changed

Added automatic playbook loading to global CLI configurations so both Claude and Codex read the collaboration playbook on session start (if present).

## Files Updated

### 1. Global Claude Config
**File**: `~/.claude/CLAUDE.md`

Added auto-initialization section:
```markdown
## 🤖 Dual-Agent Auto-Initialization

**IMPORTANT:** At the start of every session, check if `.agent/agent-collab-playbook.md` exists in the current directory.

If it exists:
1. Read `.agent/agent-collab-playbook.md` immediately
2. Read `.agent/AGENT-EXCHANGE.md` to check your role (Primary or Secondary)
3. Follow all playbook guidelines for dual-agent collaboration
4. Document all work in AGENT-EXCHANGE.md with YAML front matter

If it doesn't exist:
- Continue with normal operation
- The playbook will be auto-created when you or Codex are invoked via shell wrapper
```

### 2. Global Codex Config
**File**: `~/.codex/INSTRUCTIONS.md` (newly created)

Created global instructions file with:
- Auto-initialization protocol
- Collaboration guidelines with Claude
- Central knowledge repository awareness

## How It Works Now

### Session Start Flow

```
User runs: claude (or codex)
    ↓
Shell wrapper: dual_agent init claude
    ↓
Creates .agent/ with playbook symlink
    ↓
Agent launches and reads global config
    ↓
Global config: "Check if .agent/agent-collab-playbook.md exists"
    ↓
YES → Auto-read playbook + AGENT-EXCHANGE.md
NO  → Continue normal operation
```

### Example Session

```bash
# New project
cd /apps/new-project

# Start Claude
claude

# Automatic sequence:
# 1. Shell wrapper runs: dual_agent init claude
# 2. Creates .agent/agent-collab-playbook.md symlink
# 3. Claude reads ~/.claude/CLAUDE.md
# 4. Sees: "Check if .agent/agent-collab-playbook.md exists"
# 5. It exists! Auto-reads playbook
# 6. Checks AGENT-EXCHANGE.md for role
# 7. Ready for dual-agent collaboration
```

## Benefits

### Before Auto-Loading
- ❌ User had to explicitly ask: "Read .agent/agent-collab-playbook.md"
- ❌ Easy to forget playbook exists
- ❌ Inconsistent collaboration practices
- ❌ Manual context loading every session

### After Auto-Loading
- ✅ Playbook automatically in context when needed
- ✅ Consistent collaboration practices
- ✅ Zero manual steps
- ✅ Agents know their role immediately

## Performance Considerations

**Concern**: Loading playbook adds ~7.7 KB to every session

**Mitigation**: Conditional loading
- Only loads if `.agent/` directory exists
- Most personal projects won't have it
- Only dual-agent projects pay the cost

**Typical Usage**:
- 90% of sessions: No `.agent/` → No playbook load → Fast
- 10% of sessions: Dual-agent project → Auto-load → Worth it

## Verification

Test that auto-loading works:

```bash
# 1. Create test directory
mkdir -p /tmp/test-autoload
cd /tmp/test-autoload

# 2. Manually init (to create .agent/)
dual_agent init claude

# 3. Start Claude
claude

# 4. First message:
# "What's in .agent/agent-collab-playbook.md?"
# Claude should already know (auto-read it)

# Expected: Claude describes playbook contents without reading it again
```

## Codex Compatibility

**Note**: Codex may not automatically read `~/.codex/INSTRUCTIONS.md` depending on its implementation.

**Fallback**: Per-project `.codex/instructions.md` files are still injected by `dual_agent init codex`

**Testing needed**: Verify Codex picks up global INSTRUCTIONS.md file

## Configuration Files Summary

| Agent | Global Config | Per-Project Config | Auto-Read? |
|-------|---------------|-------------------|------------|
| Claude | `~/.claude/CLAUDE.md` | `CLAUDE.md` | ✅ Yes (both) |
| Codex | `~/.codex/INSTRUCTIONS.md` | `.codex/instructions.md` | ❓ TBD |

## Future Improvements

1. **Lazy loading**: Only read playbook when dual-agent commands used
2. **Cache playbook**: Load once per session, not every message
3. **Playbook versioning**: Track which version each agent has read
4. **Analytics**: Log how often auto-loading is used vs skipped

## Rollback

If auto-loading causes issues:

```bash
# Remove auto-load section from global Claude config
# Edit ~/.claude/CLAUDE.md
# Delete lines 3-15 (Dual-Agent Auto-Initialization section)

# Remove Codex global instructions
rm ~/.codex/INSTRUCTIONS.md

# Per-project playbooks still work via explicit reading
```

## Updated Documentation

This change affects:
- ✅ `~/.claude/CLAUDE.md` - Updated
- ✅ `~/.codex/INSTRUCTIONS.md` - Created
- ✅ Central learnings - Logged
- ⏳ README.md - Should document this feature
- ⏳ BULLETPROOF-SUMMARY.md - Should mention auto-loading
