# Chain of Thoughts Patterns

All Sub-steps inside `<Steps>` conform to one of these patterns:

| ID | Pattern |
|----|---------|
| A  | If "condition1" is true then do "condition2". |
| B  | Run if "condition1" is true. |
| C  | Validate that "item" is between "value1" and "value2". |
| D  | Skip if "item1" is "value1". |
| F  | If "item1" is "value1", then do "condition1", otherwise do "condition2". |
| G  | Only run if "item1" is "value". |
| H  | Validate if "condition1" is true or false. |
| I  | MUST NOT do "action" if "condition" is false. |

No free-form reasoning sentences. All conditions are explicit and testable.

Sub-steps conform strictly to one pattern above. No implicit logic. Use MUST, DO NOT, ONLY where applicable. Sub-steps that deviate from this template invalidate the prompt.

Pattern IDs (A, B, C, D, F, G, H, I) are internal validation references. DO NOT write pattern IDs in the generated XML output. Write the sub-step sentence directly using the pattern structure without prefixing the ID letter.

## Sub-Step Formatting

- Step headers and Sub-Procedure headers use no prefix (e.g., "Step 1.1: Name", "Sub-Procedure: Name").
- Sub-steps within a Step or Sub-Procedure use numbered list (1. 2. 3.) for sequential logic.
- Detail actions belonging to a specific sub-step use `-` prefix directly below the parent numbered sub-step.
- Numbering resets per Step (each Step starts at 1.).
- No indentation required between numbered sub-steps and their `-` detail actions. The format change (number → dash) signals the hierarchy.
- Max depth: 3 tiers (header → numbered sub-step → dash detail). If a detail action needs sub-details, extract as Sub-Procedure.

Example:
```
Step 1.1: Step Header
1. Validate if condition is true or false.
2. If condition is true, then do action.
- For EACH item, extract value.
- Store result.
3. If condition is false, then STOP.
```

## Sub-Procedures

- If the same logic sequence appears in more than one Step, extract it as a named Sub-Procedure.
- Define the Sub-Procedure once within `<Steps>`. Reference it by name in subsequent Steps.
- Reference format: "Execute [Sub-Procedure Name]." — single line.
- Sub-Procedures follow the same CoT pattern rules and numbered sub-step convention as regular Steps.
