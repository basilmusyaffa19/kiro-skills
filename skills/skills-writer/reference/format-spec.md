# SKILL.md Format Specification

Based on AgentSkills specification — portable across Claude Code, OpenClaw, Kiro, Cursor, Gemini CLI.

## Frontmatter Fields

### Required

| Field | Max | Format |
|-------|-----|--------|
| `name` | 64 chars | Kebab-case, lowercase, no spaces/underscores |
| `description` | 1024 chars | Trigger rule: when should agent activate |

### Optional

| Field | Type | Purpose |
|-------|------|---------|
| `metadata` | JSON | `{"clawdbot":{"emoji":"🔧","requires":{"anyBins":["tool"]},"os":["linux","darwin","win32"]}}` |
| `allowed-tools` | list | Tools allowed without permission prompt. E.g., `Read`, `Bash(pdftotext:*)` |
| `argument-hint` | string | Autocomplete hint. E.g., `[issue-number]` |
| `disable-model-invocation` | bool | `true` = manual only via `/name` |
| `user-invocable` | bool | `false` = hidden from menu, agent-only |
| `model` | string | Override model for this skill |
| `context` | string | `fork` = run in isolated subagent |

### Invocation Control

| Setting | User | Agent |
|---------|------|-------|
| Default | Yes | Yes |
| `disable-model-invocation: true` | Yes | No |
| `user-invocable: false` | No | Yes |

### Security

- `name` must not contain "anthropic" or "claude"
- `description` must not contain angle brackets (`<`, `>`)
- No XML tags in `name` or `description`

## Loading Precedence

```
<workspace>/skills/     ← highest
~/.openclaw/skills/     ← global
bundled skills          ← lowest
```

Workspace overrides global and bundled without warning.

## Naming Rules

- File: exactly `SKILL.md` (case-sensitive). `skill.md`, `Skill.md` are ignored.
- Folder: kebab-case. `my-skill-name/`, not `MySkillName/`.
- Max 500 lines for SKILL.md.
