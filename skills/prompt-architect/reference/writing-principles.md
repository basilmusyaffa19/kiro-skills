# Prompt Writing Principles

- Clear, specific, explicit language. Direct commands.
- Provide relevant context: include only the Chain of Thought needed for the AI to understand the task's objective and scope.
- State requirements, constraints, and expectations explicitly. Vague or ambiguous instructions cause misinterpretation.
- Maximize impact, minimize effort. Apply the Pareto principle: design each instruction for minimal effort and maximal impact.
- One concept stated once. No repetition across sections.
- Output format declared explicitly in `<Expectations>`.
- Token-efficient: remove unnecessary whitespace, cut verbose phrasing, merge overlapping points.
- Examples (when included) use generic placeholders only. No real data, no domain-specific values.
- Examples demonstrate structure, not content. They illustrate transformation patterns using abstract placeholders.

## Enforcement

- No free-form prompts in production systems.
- No implicit expectations.
- No mixed objectives in one prompt.
- No vague instructions.
- No missing `<Narrowing>` section.
- No deviation from the Chain of Thoughts template.

Incomplete structure invalidates the prompt.

## Prompt Modification Rules

When modifying an existing prompt:

- New logic MUST NOT duplicate existing logic.
- New logic MUST NOT overlap with existing logic.
- New logic MUST NOT alter the existing flow.
- Change the flow only when explicitly instructed with clear justification.
- Updates are additive and non-destructive by default.
