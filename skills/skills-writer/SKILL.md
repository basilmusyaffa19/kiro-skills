---
name: skills-writer
description: Create well-structured agent skills following Anthropic's best practices. Use when the user asks to create a new skill, scaffold a skill folder, write a SKILL.md, design a skill for Kiro or OpenClaw, or wants to turn a workflow into a reusable skill. Also activate when the user mentions skill creation, skill design, or skill packaging.
---

# Skill Writer

Create agent skills that follow Anthropic's design principles and the AgentSkills specification.

## Workflow

1. Read the user's request. Identify: what the skill does, when it triggers, what tools/dependencies it needs.
2. Select the skill category from the 9 Anthropic categories (see `reference/categories.md`).
3. Scaffold the folder structure.
4. Write SKILL.md with proper frontmatter and body.
5. Create reference files if the skill needs progressive disclosure.
6. Validate against the checklist before delivery.

Do not interview the user step-by-step. Extract information from the request and generate directly. Ask only if the core purpose is genuinely unclear.

## Folder Structure

Every skill is a folder, not a file.

```
{skill-name}/
├── SKILL.md              ← Required: frontmatter + instructions
├── references/           ← Optional: docs loaded on-demand
│   └── api.md
├── scripts/              ← Optional: executable helpers
└── assets/               ← Optional: templates, data files
```

Rules:
- Folder name: kebab-case, lowercase. No underscores, no camelCase.
- File must be named exactly `SKILL.md` (case-sensitive).
- Max 500 lines for SKILL.md. Split to reference files if longer.

## SKILL.md Frontmatter

```yaml
---
name: skill-name
description: >
  [What it does]. Use when [trigger 1], [trigger 2].
  Also covers [related topic].
---
```

### Required Fields

| Field | Max | Rule |
|-------|-----|------|
| `name` | 64 chars | Kebab-case, lowercase, no spaces/underscores. |
| `description` | 1024 chars | Trigger rule — when should the agent activate this skill. Not a summary. |

### Description Formula

Write as: `[What it does]. Use when [trigger scenario 1], [trigger scenario 2]. Also covers [related topic].`

Good: `Write Makefiles for any project type. Use when setting up build automation, defining multi-target builds, or using Make for non-C projects.`

Bad: `A skill about Makefiles.`

The description is the most important field. The agent scans descriptions at session start to match user requests.

### Optional Fields

| Field | Purpose |
|-------|---------|
| `metadata` | JSON: emoji, required binaries (`anyBins`), supported OS |
| `allowed-tools` | Tools allowed without permission prompt |
| `disable-model-invocation` | `true` = manual only via `/name` |
| `user-invocable` | `false` = hidden, agent-only trigger |
| `context` | `fork` = run in isolated subagent context |

## SKILL.md Body Sections

```markdown
# Skill Title

One-paragraph summary.

## When to Use

- Trigger scenario 1
- Trigger scenario 2

## Prerequisites

- Required tools or dependencies

## Main Content

Core instructions...

## Gotchas

- Failure point 1 and how to avoid it
- Failure point 2 and how to avoid it
```

## Design Principles

Apply these when writing any skill:

### Explain Why, Not MUST

Today's LLMs are smart. They have good theory of mind. Explain the reasoning behind each instruction so the model understands why something matters. If you find yourself writing ALWAYS or NEVER in all caps, reframe — explain the reasoning instead. That's more effective than rigid enforcement.

### Don't State the Obvious

The agent already knows how to code. Write only information that changes the agent's default behavior. Every token consumes context window.

### Description = Trigger Rule

Write description as a condition for when the skill activates. Not "This skill does X" but "Use when the user asks for Y". Be slightly "pushy" — Claude tends to undertrigger skills. Include adjacent contexts where the skill should activate even if the user doesn't explicitly name it.

Important: Claude only consults skills for tasks it can't easily handle on its own. Simple one-step queries won't trigger skills regardless of description quality. Target complex, multi-step, or specialized tasks.

### Progressive Disclosure (Three-Level Loading)

Skills use a three-level loading system:

| Level | What | When | Size |
|-------|------|------|------|
| Metadata | name + description | Always in context | ~100 words |
| SKILL.md body | Full instructions | When skill triggers | <500 lines |
| Bundled resources | References, scripts, assets | On demand | Unlimited |

SKILL.md is the entry point, not the entire content. Split detailed references into separate files. Declare token count per file so the agent chooses efficiently.

### Gotchas Section

Highest-signal content in any skill. Build from actual failure points, not theoretical anticipation. Update iteratively as the agent encounters new edge cases.

### Generalize, Don't Overfit

Skills are used across many different prompts. Don't put in fiddly, overfitty changes or oppressively constrictive MUSTs for specific examples. If there's a stubborn issue, try different metaphors or recommend different patterns rather than adding more constraints.

### Keep It Lean

Remove things that aren't pulling their weight. Read transcripts of skill usage — if the skill makes the model waste time on unproductive steps, remove those parts.

### Look for Repeated Work

If multiple test runs independently write similar helper scripts or take the same multi-step approach, that's a signal to bundle that script. Write it once in `scripts/`, reference from SKILL.md.

### Avoid Railroading

Provide information and context, not rigid step-by-step instructions. The agent decides the best approach based on the situation.

### Config-Driven Setup

If the skill needs user input (API keys, channel names), store in `config.json`. If config doesn't exist, ask the user before execution.

### Memory Pattern

For skills that need state across executions, use stable storage (`${CLAUDE_PLUGIN_DATA}`), not the skill directory (deleted on upgrade).

### Auto-Learning via Gotchas

Every skill with a `references/gotchas.md` should instruct the agent to append new findings during execution. When the agent encounters a failure, unexpected behavior, or learned pattern, it writes to gotchas.md under the relevant category. This turns every execution into a learning opportunity — the skill improves over time without manual curation.

### Domain Organization

When a skill supports multiple domains or frameworks, organize by variant:

```
cloud-deploy/
├── SKILL.md
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

The agent reads only the relevant reference file.

## Category Selection

Before writing, classify the skill into one of 9 categories. A good skill fits one category cleanly. See `reference/categories.md` for the full list.

Quick reference:

| Category | Signal |
|----------|--------|
| Library & API Reference | "How to use X correctly" |
| Product Verification | "Test that X works" |
| Data Fetching & Analysis | "Get data from X" |
| Business Process Automation | "Automate this workflow" |
| Code Scaffolding | "Generate boilerplate for X" |
| Code Quality & Review | "Enforce standard X" |
| CI/CD & Deployment | "Build, test, deploy X" |
| Runbooks | "Investigate symptom X" |
| Infrastructure Operations | "Maintain X with guardrails" |

If the skill straddles multiple categories, it's too broad. Split it.

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| Stating the obvious | Remove info the agent already knows |
| Railroading | Replace rigid steps with context + flexibility |
| Heavy-handed MUSTs | Explain the why instead — models respond better to reasoning than enforcement |
| Straddling categories | Split into separate skills |
| Flat file skill | Use folder structure + progressive disclosure |
| No gotchas section | Add gotchas from actual failure points |
| Overfitting to examples | Generalize — the skill runs across many different prompts |
| Static skill | Plan for iterative updates |
| Unstable storage | Use `${CLAUDE_PLUGIN_DATA}` |
| Prompt bloat | Remove instructions not pulling their weight |

## Validation Checklist

Before delivering a skill, verify:

1. Folder name is kebab-case, file is exactly `SKILL.md`.
2. Frontmatter has `name` and `description`. Description is a trigger rule.
3. Skill fits one category cleanly.
4. SKILL.md under 500 lines. Detailed content in reference files.
5. Gotchas section exists (even if initially small).
6. No obvious information that the agent already knows.
7. Instructions provide context, not rigid railroading.
8. Gotchas section includes auto-learning instruction — agent appends new findings during execution.

## Reference Files

| File | Content | ~Tokens | When to Read |
|------|---------|---------|--------------|
| `reference/categories.md` | 9 skill categories with details and examples | 800 | When selecting category |
| `reference/format-spec.md` | Full SKILL.md format specification | 600 | When writing frontmatter or optional fields |
