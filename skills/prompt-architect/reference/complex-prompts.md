# Complex Prompts

A Sub-Procedure is a named, reusable logic sequence extracted from Steps. Define it once, reference by name in subsequent Steps. See `cot-patterns.md` for full Sub-Procedure rules and formatting.

For prompts with multiple workflows or 10+ steps:

- If two or more Steps share >50% of their logic, extract the shared portion into a Sub-Procedure.
- Each workflow references shared Sub-Procedures by name.
- Keep each Step to its unique logic. Shared logic lives in Sub-Procedures.
- Define format contracts (tables, display templates) once in `<Expectations>`. Reference from `<Steps>` by name.
- Do not inline repeated display logic. A single reference replaces a repeated block.
