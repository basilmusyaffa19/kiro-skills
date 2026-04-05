# Preprocessing Support Reference

The conversion pipeline has two stages: Obsidian preprocessing → Pandoc conversion. This determines what Markdown syntax writers can use.

## Pandoc Native (no preprocessing needed)

These work directly in the DOCX output:

- Headings `#` through `######`
- Bold `**text**`, italic `*text*`, bold+italic `***text***`
- Strikethrough `~~text~~`
- Inline code and fenced code blocks
- Ordered and unordered lists (including nested)
- Task lists `- [ ]` / `- [x]`
- Tables with alignment
- Standard blockquotes `>`
- Footnotes `[^1]`
- Horizontal rules `---`
- Math LaTeX `$...$` and `$$...$$`
- External links `[text](url)`
- Standard images `![alt](path)`

## Preprocessed (Obsidian → Standard Markdown)

| Obsidian Syntax | Output | Notes |
|---|---|---|
| `[[Note]]` | `**Note**` | Bold as visual indicator |
| `[[Note\|Display]]` | `**Display**` | Uses alias text |
| `[[Note#Heading]]` | `**Heading**` | Uses heading reference |
| `==text==` | `**text**` | Bold fallback (no highlight in DOCX) |
| `![[image.png]]` | `![image](image.png)` | Standard image syntax |
| `![[image.png\|300]]` | `![image](image.png)` | Width stripped |
| `![[note]]` | `[Embedded: note]` | Placeholder only |
| `> [!type] Title` | `> emoji **Title**` | Callout → blockquote + emoji |
| YAML frontmatter | Stripped | Not included in content |
| `%% comment %%` | Stripped | Hidden content removed |
| `#tag` | `tag` | Hash removed, text kept |

## Callout Emoji Mapping

| Type | Emoji | Type | Emoji |
|---|---|---|---|
| note | 📝 | warning | ⚠️ |
| info | ℹ️ | danger | 🔴 |
| tip | 💡 | failure | ❌ |
| success | ✅ | bug | 🐛 |
| question | ❓ | example | 📋 |
| abstract | 📄 | quote | 💬 |
| todo | ☑️ | | |

## Not Supported in DOCX

| Syntax | Behavior |
|---|---|
| Mermaid code blocks | Replaced with `[Diagram: Mermaid — render terpisah]` |
| Nested embeds | One level only, no recursion |
| Highlight color | Falls back to bold |
| Math LaTeX | Depends on Pandoc OMML support, results vary |
