---
name: prompt-architect
description: Generate production-grade structured XML prompts following the RISEN framework (Role, Instructions, Steps, Expectations, Narrowing). Use this skill whenever the user asks to create a prompt, design a prompt template, build an agent prompt, write a system prompt, structure a prompt for automation, or needs a deterministic XML prompt for any use case. Also activate when the user mentions prompt engineering, prompt design, or wants to convert a vague request into a structured prompt.
---

# Prompt Architect

Generate structured XML prompts that produce deterministic, verifiable AI behavior.

## Core Concept

Every prompt you generate contains five XML sections in this order:

```xml
<Role>       — Who the AI is
<Instructions> — What the AI does
<Steps>      — How the AI reasons
<Expectations> — What the output looks like
<Narrowing>  — What the AI must not do
```

All five sections are mandatory. A missing section invalidates the prompt.

## Workflow

1. Read the user's request.
2. Identify the task objective, target persona, output format, and constraints.
3. Generate the complete XML prompt.
4. Save the prompt as a `.xml` file in the user's working directory.
5. Audit the generated prompt against writing principles. Check for: repeated logic blocks, restated constraints between sections, verbose phrasing, concepts defined in multiple sections. Revise before delivery.

Do not interview the user step-by-step. Extract all necessary information from the request and generate the prompt directly. If critical information is genuinely missing (e.g., no discernible task objective), ask once, then generate.

## Section Rules

### `<Role>`

Define the AI's identity and operational context.

Include: persona and expertise level, primary objective, expected input description, personality definition, communication style (tone, clarity level, formality).

Communication style supports the primary objective. Omit theoretical explanation. Define operational behavior only.

### `<Instructions>`

State the core directive.

- One primary objective per prompt.
- Direct, unambiguous language.
- Eliminate multi-interpretation phrasing.
- Focus on WHAT the AI does, not why.

### `<Steps>`

Define execution logic as an ordered sequence.

- Structure reasoning step by step.
- Add one blank line between major Steps for readability.
- DO NOT add blank lines between Sub-steps within the same Step.
- Each Step may contain Sub-steps.
- Sub-steps follow the Chain of Thoughts patterns (see `reference/cot-patterns.md`).
- Steps connect in logical sequence.

Purpose: enforce reasoning discipline, reduce hallucination, increase determinism.

### `<Expectations>`

Define the output contract.

Specify: output format (Markdown, JSON, table, bullet points, etc.), structural requirements, level of detail, formatting rules.

The expected output must be testable and verifiable. Ambiguous output formats invalidate the prompt.

### `<Narrowing>`

Define constraints and boundaries per Step.

Use capital emphasis for enforcement: MUST, DO NOT, ONLY.

Format constraints per step:
```
Step 1 Constraints:
- MUST ...
- DO NOT ...

Step 2 Constraints:
- ONLY ...
```

Narrowing contains ONLY constraints that add boundaries beyond what Steps already define. DO NOT restate execution logic from Steps as MUST statements in Narrowing. Test: "Does this constraint prevent a behavior not already controlled by Steps?" If no, remove it.

## Design Priorities

| Priority | Over |
|----------|------|
| Determinism | Creativity |
| Control | Verbosity |
| Clarity | Flexibility |
| Execution | Exploration |

## When NOT to Generate a Full Prompt

Skip the full RISEN structure for:
- Simple, single-turn factual questions.
- Casual conversational interactions.
- One-off exploratory queries.

If the user's request does not require repeatable or deterministic behavior, say so and answer directly instead.

## Output Rules

- Save the generated prompt as `<descriptive-name>.xml` in the user's working directory.
- The XML file contains only the five sections. No wrapper elements, no metadata.
- No indentation of XML tags. Content starts at column 0 after the opening tag.

## Validation Checklist

Before delivering a prompt, verify six properties:

1. Clear structure — all five XML sections present and ordered.
2. Specific instructions — no vague or multi-interpretation phrasing.
3. Emphasis on key points — MUST, DO NOT, ONLY applied where enforcement is required.
4. No repetition — no logic block or concept appears more than once across all sections.
5. Token efficiency — every line changes agent behavior. If a line can be removed without losing behavior, remove it.
6. Narrowing independence — every constraint in Narrowing adds a boundary not already expressed in Steps.

A prompt that fails any property requires revision before delivery.

## Common Pitfalls

| Pitfall | Cause | Fix |
|---|---|---|
| Generic output | Missing or vague `<Role>` | Assign a specific persona with domain expertise |
| Rambling response | No `<Steps>` defined | Break the task into 3–5 ordered sub-tasks |
| Off-topic content | No `<Narrowing>` constraints | Add scope boundaries, exclusions, or word limits |
| Misaligned result | Missing `<Expectations>` | Specify output format, structure, and level of detail |
| Ambiguous behavior | Vague `<Instructions>` | One primary objective per prompt; eliminate multi-interpretation phrasing |
| Narrowing duplicates Steps | Restating execution logic as MUST constraints | Test each constraint: "Does this prevent a behavior not already controlled by Steps?" Remove if no |
| Prompt bloat | Too many steps without Sub-Procedures | Extract shared logic into Sub-Procedures; see `reference/complex-prompts.md` |
| Untestable output | Expectations written as description, not contract | Rewrite Expectations as verifiable assertions: exact format, structure, constraints |

When you encounter a new failure pattern not listed above, append it to this table.

## Reference Files

Technical details are split into separate files. Read as needed:

| File | Content | ~Tokens | When to Read |
|------|---------|---------|--------------|
| `reference/cot-patterns.md` | Chain of Thoughts patterns, sub-step formatting, sub-procedures | 500 | When writing `<Steps>` section |
| `reference/complex-prompts.md` | Multi-workflow prompts, shared sub-procedures | 150 | When prompt has 10+ steps or multiple workflows |
| `reference/writing-principles.md` | Writing principles, enforcement rules, modification rules | 280 | When auditing or modifying a prompt |
| `reference/example-rules.md` | Example neutrality, structural examples, overfitting avoidance | 150 | When prompt includes examples |
