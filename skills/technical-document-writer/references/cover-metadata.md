# Cover Metadata Reference

The cover file contains only YAML frontmatter between `---` delimiters. The script parses these fields and replaces placeholders in `template/template.docx`.

## Field Reference

### Page 1 — Cover Page

| Field | Target | Example |
|---|---|---|
| `title` | Main title | "Internal Technical Documentation" |
| `subtitle` | Subtitle line | "Panduan Pizza Order dengan Dify" |
| `topic` | Topic line | "Agent + Workflow as Tool" |
| `author` | Author table row | "[Name / email]" |
| `approved_by` | Approved by table row | "[Name / email]" |
| `version` | Version table row | "1.0" |

### Page 2 — Document Overview

| Field | Target | Example |
|---|---|---|
| `document_title` | Document title row | "Panduan Pizza Order dengan Dify" |
| `version_number` | Version number row | "1.0" |
| `reviewer` | Reviewer row | "Reviewer Name" |
| `doc_author` | Author row | "Author Name" |
| `last_update` | Last update row | "2026-04-01" |
| `status` | Status row | "Draft" |

### Page 2 — Revision History (list)

```yaml
revision_history:
  - version: "1.0"
    date: "2026-04-01"
    description: "Initial release"
    rev_author: "Author Name"
    rev_approved_by: "Approver Name"
```

### Page 2 — Authors (list)

```yaml
authors:
  - name: "Author Name"
    squad: "Team Name"
```

## Notes

- All string values should be quoted in YAML.
- The template has placeholder text (`[…]` and `(…)`) that gets replaced.
- Table rows in the template must exist — the script fills existing rows, it does not create new ones.
- For multiple revision history or author entries, ensure the template has enough rows.
