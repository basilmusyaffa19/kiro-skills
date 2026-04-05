---
name: technical-document-writer
description: >
  Write internal technical documents as numbered Obsidian Markdown files
  ready for DOCX conversion. Use when creating onboarding guides, technical
  test documents, internal documentation, or any structured multi-chapter
  document. Also activate when the user asks to scaffold a new document,
  write a chapter, or prepare markdown for DOCX export.
---

# Technical Document Writer

Create structured technical documents as numbered Obsidian Markdown files in a draft folder. The files follow a defined chapter structure, style guide, and cover metadata schema. A conversion script (`src/md_to_docx.py`) transforms them into a styled DOCX via preprocessing + Pandoc.

## When to Use

- User asks to create a new technical document or onboarding guide
- User asks to write or add a chapter to an existing document draft
- User asks to scaffold a document folder structure
- User asks to prepare markdown files for DOCX conversion
- User mentions "template/draft" or document chapters

## Folder Structure

Each document lives in a `draft/` folder at the project root. Files are numbered sequentially and sorted ascending — this order determines chapter order in the final DOCX.

```
draft/
  001-cover.md                    # Cover metadata (YAML frontmatter only)
  002-introduction.md             # Chapter: Introduction
  003-overview.md                 # Chapter: Overview
  004-technical-documentation.md  # Chapter: Technical Documentation
  005-conclusion.md               # Chapter: Conclusion
  006-references.md               # Chapter: References
  007-appendix.md                 # Optional
```

Rules:
- File with "cover" in its name is auto-detected as cover metadata — not included in content.
- Remaining files become content chapters, processed in sorted filename order.
- Appendix is optional. Omit for technical test documents so participants work independently.

## Chapter Structure

Every document follows a 7-chapter template:

| # | Chapter | Purpose |
|---|---------|---------|
| 1 | Cover Page | Title, author, version, metadata (from template.docx + cover YAML) |
| 2 | Introduction | Background, objective, scope, target audience, prerequisites |
| 3 | Overview | Core concepts, architecture, context, design decisions |
| 4 | Technical Documentation | Specifications, configurations, task lists |
| 5 | Conclusion | Summary, key learnings, next steps |
| 6 | References | Source links |
| 7 | Appendix | Supplementary data, full code (optional) |

## Writing Style

### Language
- Headings (`#`, `##`, `###`, `####`): English only. No mixed language.
- Body content: Indonesian.
- Code, identifiers, file paths, API names: English (unchanged).

### Perspective and Tone
- Second person — address the reader as "kamu".
- Use "kita" for shared activities (team + reader).
- Tone: mentor speaking to mentee. Direct, friendly, professional, instructive.
- Avoid third-person narrative ("Dokumen ini bertujuan..."). Instead: "Setelah menyelesaikan panduan ini, kamu akan mampu..."

See `references/style-guide.md` (~120 lines) for detailed do/don't patterns per chapter section.

### Sub-heading Numbering
Sequential sub-headings (steps, nodes, components) use letter prefix:
```
#### A. Start Node
#### B. IF/ELSE Node
```

### Diagrams
Use text-based flow diagrams with `│`, `▼`, `→` inside code blocks. Mermaid is not supported in the DOCX pipeline — it renders as a placeholder.

## Cover Metadata

The cover file contains only YAML frontmatter. The script parses it and fills placeholders in `template/template.docx`.

Minimal example:
```yaml
---
title: "Document Title"
subtitle: "Subtitle"
topic: "Topic"
author: "[Name / email]"
approved_by: "[Name / email]"
version: "1.0"
document_title: "Document Title"
version_number: "1.0"
reviewer: "Reviewer Name"
doc_author: "Author Name"
last_update: "YYYY-MM-DD"
status: "Draft"
revision_history:
  - version: "1.0"
    date: "YYYY-MM-DD"
    description: "Initial release"
    rev_author: "Author Name"
    rev_approved_by: "Approver Name"
authors:
  - name: "Author Name"
    squad: "Team Name"
---
```

See `references/cover-metadata.md` (~50 lines) for full field reference.

## Content Strategy for Technical Tests

When the document is a technical test or hands-on exercise:
- Provide full context and specifications (input, output, architecture, reference data).
- State clear requirements per component.
- Do not provide direct answers (code, prompts, detailed config).
- Include a task list as a checklist.
- Include success criteria so participants can self-validate.

Principle: the reader knows **what** to build and **what** to expect, but decides **how** to build it.

## Supported Markdown Syntax

The preprocessing pipeline handles Obsidian-specific syntax. Writers can use:
- Standard Markdown (headings, bold, italic, lists, tables, code blocks, links, images) — Pandoc native
- Obsidian callouts `> [!type] Title` — converted to blockquote + emoji
- Wikilinks `[[Note]]` — converted to bold
- Highlights `==text==` — converted to bold
- Obsidian embeds `![[image.png]]` — converted to standard image syntax

Not supported in DOCX output:
- Mermaid diagrams → placeholder text
- Note embeds `![[note]]` → placeholder text
- Highlight color → falls back to bold

See `references/preprocessing-support.md` (~60 lines) for the full conversion table.

## Prerequisites

### Required Skills

This skill focuses on document structure, chapter conventions, and DOCX conversion. For writing quality, it depends on two companion skills that must be installed alongside it:

- `obsidian-markdown` — Obsidian-flavored Markdown syntax (wikilinks, callouts, embeds, properties). Install from: https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-markdown
- `writing-clearly-and-concisely` — Clear, concise prose following Strunk's principles. Install from: https://github.com/softaworks/agent-toolkit/tree/main/skills/writing-clearly-and-concisely

When writing document content, activate both skills before drafting. `obsidian-markdown` ensures correct syntax, `writing-clearly-and-concisely` ensures the prose is tight and readable.

### System Requirements

The conversion script requires Python 3.12+, uv, and Pandoc. Python package dependencies are declared as PEP 723 inline metadata in the script — `uv run` installs them automatically. See `README.md` in this skill folder for setup instructions.

## Conversion

Run from the user's project root:
```bash
uv run .kiro/skills/technical-document-writer/scripts/md_to_docx.py \
  --source ./draft \
  --output output.docx
```

The script resolves `--source` and `--output` relative to CWD (the user's project). The `--template` defaults to the bundled `assets/template.docx` inside this skill folder.

Key flags:
- `--source` / `-s`: draft folder (default: `draft`)
- `--template` / `-t`: reference template (default: bundled `assets/template.docx`)

## Gotchas

- Cover detection is substring-based: the file must have "cover" in its filename. If you name it `001-metadata.md`, the script won't find cover data.
- File sort order = chapter order. Numbering gaps are fine (`001`, `003`, `005`) but the sorted sequence determines output order.
- YAML frontmatter in content files is stripped by the preprocessor. Only the cover file's frontmatter is parsed for metadata.
- Text-based diagrams must be inside code blocks (triple backticks). Bare `│▼→` characters in body text may cause Pandoc parsing issues.
- After changing `template/template.docx` styles, just re-run the script — no code changes needed.
- Mermaid blocks render as `[Diagram: Mermaid — render terpisah]` in the DOCX. If the document needs diagrams, use text-based flow or pre-render Mermaid to PNG and embed as image.
