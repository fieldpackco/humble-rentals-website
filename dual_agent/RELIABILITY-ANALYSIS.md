# Dual Agent - Reliability Analysis & Hardening

## Critical Failure Modes

### 1. **Symlink Breakage**
**Risk**: Symlinks to central playbook break if ~/.agent-learnings moved/deleted
**Impact**: Projects lose access to canonical playbook
**Likelihood**: Medium (user might reorganize, delete accidentally)

**Current State**: No validation
**Fix Needed**: Health checks, auto-repair

### 2. **Concurrent File Access**
**Risk**: Multiple agents writing to learnings.jsonl simultaneously
**Impact**: File corruption, malformed JSON, lost learnings
**Likelihood**: High (user runs multiple sessions across projects)

**Current State**: No locking mechanism
**Fix Needed**: File locking, atomic writes

### 3. **Non-Atomic Append Operations**
**Risk**: Process killed mid-append to learnings.jsonl
**Impact**: Partial JSON lines, corrupted file
**Likelihood**: Medium (user ctrl-c, system crash)

**Current State**: Direct append with `>>`
**Fix Needed**: Write to temp file, atomic rename

### 4. **Silent Initialization Failures**
**Risk**: Shell wrapper suppresses errors with `2>/dev/null || true`
**Impact**: Agent launches without dual-agent context, work not logged
**Likelihood**: High (permission issues, missing files)

**Current State**: Errors hidden
**Fix Needed**: Log failures, alert user

### 5. **CLAUDE.md Injection Conflicts**
**Risk**: Multiple init calls append context repeatedly
**Impact**: Duplicate sections in CLAUDE.md
**Likelihood**: Medium (re-running init, multiple shells)

**Current State**: Grep check exists but could race
**Fix Needed**: Idempotency markers, checksums

### 6. **Git Repository Corruption**
**Risk**: ~/.agent-learnings/.git gets corrupted
**Impact**: Can't track history, can't push/pull
**Likelihood**: Low (but catastrophic)

**Current State**: No validation
**Fix Needed**: Git health checks, auto-repair

### 7. **Cross-Machine Merge Conflicts**
**Risk**: Using repo on multiple machines without syncing
**Impact**: Merge conflicts in playbook.md or learnings.jsonl
**Likelihood**: High (if user has multiple machines)

**Current State**: No conflict detection
**Fix Needed**: Pre-session pull, conflict detection

### 8. **Shell Wrapper Shadowing**
**Risk**: User already has `claude` or `codex` functions defined
**Impact**: Wrapper doesn't run, dual_agent never initializes
**Likelihood**: Low

**Current State**: Silently overwrites
**Fix Needed**: Detect existing functions, warn user

### 9. **Path Assumptions**
**Risk**: Hard-coded paths like `~/bin`, `~/.agent-learnings`
**Impact**: Breaks if user has custom setup
**Likelihood**: Medium

**Current State**: Hard-coded
**Fix Needed**: Config file, environment variables

### 10. **Malformed JSONL**
**Risk**: Invalid JSON appended to learnings.jsonl
**Impact**: Can't parse learnings, breaks tooling
**Likelihood**: Medium (manual edits, bugs)

**Current State**: No validation
**Fix Needed**: Validate JSON before append, validate on read

### 11. **Session Context Staleness**
**Risk**: session-context.json not updated if session crashes
**Impact**: Stale session IDs, wrong agent metadata
**Likelihood**: Medium

**Current State**: Written once, never cleaned up
**Fix Needed**: Session cleanup, expiry timestamps

### 12. **Git Push Failures**
**Risk**: Network issues, auth failures during push
**Impact**: Learnings not backed up, data loss risk
**Likelihood**: Medium

**Current State**: No retry, no notification
**Fix Needed**: Retry logic, user notification

### 13. **AGENT-EXCHANGE.md Template Drift**
**Risk**: Template format changes break parsing
**Impact**: Can't extract learnings, validation fails
**Likelihood**: Low

**Current State**: No versioning
**Fix Needed**: Schema version in template

### 14. **Disk Space Exhaustion**
**Risk**: learnings.jsonl grows unbounded
**Impact**: Disk full, can't write
**Likelihood**: Low (but eventual)

**Current State**: No rotation
**Fix Needed**: Log rotation, archival

### 15. **Permission Errors**
**Risk**: Files created with wrong permissions
**Impact**: Can't read/write in future sessions
**Likelihood**: Low

**Current State**: Uses default umask
**Fix Needed**: Explicit permission setting

---

## Reliability Hardening Roadmap

### Phase 1: Critical (Do Now)
1. **Atomic JSONL writes** - Prevent corruption
2. **Health check command** - Validate system state
3. **Init error reporting** - Stop hiding failures
4. **Symlink validation** - Auto-repair broken links
5. **JSONL validation** - Catch malformed entries

### Phase 2: Important (Do Soon)
6. **File locking** - Prevent concurrent access issues
7. **Git health checks** - Detect/repair repo issues
8. **Idempotent init** - Safe to run multiple times
9. **Backup/restore** - Disaster recovery
10. **Pre-session git pull** - Sync multi-machine usage

### Phase 3: Nice-to-Have
11. **Config file support** - Flexible paths
12. **Session cleanup** - Remove stale sessions
13. **Log rotation** - Prevent unbounded growth
14. **Conflict detection** - Warn about merge conflicts
15. **Retry logic for git ops** - Handle transient failures

---

## Implementation Details

### Atomic JSONL Writes
```bash
log_learning_atomic() {
    local message="$1"
    local temp_file="$LEARNINGS_DIR/learnings.tmp.$$"
    local target_file="$LEARNINGS_DIR/learnings.jsonl"

    # Write to temp file
    echo "$json_line" > "$temp_file"

    # Validate JSON
    if ! jq empty "$temp_file" 2>/dev/null; then
        rm "$temp_file"
        log_error "Invalid JSON, not appending"
        exit 1
    fi

    # Atomic append (file locking)
    (
        flock -x 200
        cat "$temp_file" >> "$target_file"
        rm "$temp_file"
    ) 200>"$LEARNINGS_DIR/.learnings.lock"
}
```

### Health Check Command
```bash
dual_agent health
# Checks:
# - ~/.agent-learnings exists and is git repo
# - Symlinks are valid
# - learnings.jsonl is valid JSON
# - Git repo is clean (no uncommitted changes)
# - Can connect to remote (if configured)
# - ~/bin/dual_agent is executable
# - Shell wrappers are loaded
```

### Init Error Reporting
```bash
# In shell wrapper, instead of:
dual_agent init claude 2>/dev/null || true

# Do:
if ! dual_agent init claude 2>&1 | tee ~/.agent-learnings/init.log; then
    echo "⚠️  dual_agent init failed - check ~/.agent-learnings/init.log"
fi
```

### Symlink Auto-Repair
```bash
validate_and_repair_symlinks() {
    local playbook_link="$AGENT_DIR/agent-collab-playbook.md"

    if [[ -L "$playbook_link" ]]; then
        if [[ ! -e "$playbook_link" ]]; then
            log_warn "Broken symlink detected, repairing..."
            rm "$playbook_link"
            ln -s "$LEARNINGS_DIR/playbook.md" "$playbook_link"
            log_success "Symlink repaired"
        fi
    fi
}
```

### JSONL Validation
```bash
validate_learnings_file() {
    local file="$LEARNINGS_DIR/learnings.jsonl"
    local line_num=0

    while IFS= read -r line; do
        ((line_num++))
        if ! echo "$line" | jq empty 2>/dev/null; then
            log_error "Invalid JSON at line $line_num: $line"
            return 1
        fi
    done < "$file"

    log_success "learnings.jsonl validated ($line_num lines)"
}
```

---

## Monitoring & Alerts

### What to Monitor
1. **Symlink health** - Run on every init
2. **Git sync status** - Warn if unpushed commits > 1 week
3. **JSONL integrity** - Validate on read
4. **Disk usage** - Alert if learnings.jsonl > 100MB
5. **Session age** - Cleanup sessions > 7 days old

### Alert Mechanisms
- Terminal warnings on `dual_agent status`
- Log file: `~/.agent-learnings/health.log`
- Optional: Desktop notification for critical issues

---

## Recovery Procedures

### Corrupted learnings.jsonl
```bash
dual_agent restore learnings --from-git
# OR
dual_agent validate learnings --repair
# Removes invalid lines, backs up to learnings.jsonl.bak
```

### Broken Git Repo
```bash
dual_agent repair git
# Validates .git, runs git fsck, offers to re-clone if broken
```

### Lost Symlinks
```bash
dual_agent repair symlinks [--all]
# Scans all project .agent/ dirs, repairs broken symlinks
```

### Complete Reset
```bash
dual_agent reset --confirm
# Nukes local state, re-clones from GitHub
# Preserves local AGENT-EXCHANGE.md files
```

---

## Testing Strategy

### Unit Tests (Shell)
- Test atomic writes under concurrent access
- Test symlink repair logic
- Test JSONL validation with malformed input
- Test git health checks

### Integration Tests
- Simulate multi-machine usage with conflicts
- Test init in various states (clean, partial, corrupted)
- Test error conditions (no space, no permissions)

### Chaos Testing
- Kill processes mid-write
- Corrupt files and validate recovery
- Delete ~/.agent-learnings and test rebuild
- Simulate network failures during git push

---

## Metrics to Track

1. **Initialization success rate** - % of inits that succeed
2. **Symlink repair frequency** - How often auto-repair runs
3. **JSONL corruption rate** - Invalid entries / total entries
4. **Git sync lag** - Time since last push
5. **Session cleanup rate** - Stale sessions removed / total sessions

Log these to `~/.agent-learnings/metrics.jsonl` for analysis.
