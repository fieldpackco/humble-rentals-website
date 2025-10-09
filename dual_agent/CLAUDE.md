# Claude Code - Project Instructions

## 🤝 Dual-Agent Mode Active

You are operating in **dual-agent collaboration mode** with OpenAI Codex as your peer agent.

### Quick Reference
- **Peer Agent**: OpenAI Codex (invoke via `codex` command)
- **Collaboration Playbook**: `.agent/agent-collab-playbook.md` (read this first!)
- **Shared Log**: `.agent/AGENT-EXCHANGE.md` (document all work here)
- **Central Knowledge**: `~/.agent-learnings/` (learnings from all projects)

### Your Role
Check `.agent/AGENT-EXCHANGE.md` for the latest entry to determine if you are:
- **Primary** (implement code, make decisions, drive the work)
- **Secondary** (propose approach, write tests first, review diffs)

Roles can swap between entries. Always log your role in the YAML front matter.

### Key Principles
1. **Read the playbook first** - `.agent/agent-collab-playbook.md` has all guardrails
2. **Document everything** - Use AGENT-EXCHANGE.md with YAML front matter
3. **Test-first** - Secondary proposes failing tests, Primary makes them pass
4. **Stay in scope** - Respect `files_write_scope` declared in each entry
5. **Escalate disagreements** - Max 2 consensus cycles, then ask the user

### Cross-Agent Communication
To involve Codex:
```bash
# Call Codex directly from terminal
codex "Review the implementation in src/foo.ts"

# Or document request in AGENT-EXCHANGE.md and user will coordinate
```

### Learnings Propagation
When you discover a new failure mode, guardrail, or best practice:
1. Document it in the current AGENT-EXCHANGE entry
2. The system will sync it to `~/.agent-learnings/learnings.jsonl`
3. All future projects will benefit from this learning

---
*This context is automatically injected by dual_agent. Last updated: 2025-10-09*
