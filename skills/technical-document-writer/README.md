# Technical Document Writer

A Kiro skill that writes internal technical documents as numbered Obsidian Markdown files and converts them to styled Word documents (.docx).

## What's Included

```
technical-document-writer/
├── SKILL.md                # Agent instructions (style guide, chapter structure, conventions)
├── README.md               # This file — human setup guide
├── scripts/
│   ├── md_to_docx.py       # Conversion script (PEP 723 inline dependencies)
│   └── preprocessor.py     # Obsidian syntax preprocessing
├── assets/
│   └── template.docx       # Default Word template for styling
└── references/
    ├── style-guide.md       # Detailed writing patterns (do/don't per section)
    ├── cover-metadata.md    # YAML field reference for cover page
    └── preprocessing-support.md  # Supported Obsidian syntax conversion table
```

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)
- [Pandoc](https://pandoc.org/installing.html) (document conversion engine)

### Required Companion Skills

Install these two skills into `.kiro/skills/` alongside `technical-document-writer`:

| Skill | Source | Purpose |
|-------|--------|---------|
| `obsidian-markdown` | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-markdown) | Obsidian Markdown syntax (wikilinks, callouts, embeds, properties) |
| `writing-clearly-and-concisely` | [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit/tree/main/skills/writing-clearly-and-concisely) | Clear, concise writing following Strunk's principles |

## Setup

### 1. Install the skill

Copy this folder into your project:

```
your-project/.kiro/skills/technical-document-writer/
```

### 2. Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Install Pandoc

```bash
# macOS
brew install pandoc

# Windows
winget install pandoc

# Ubuntu/Debian
sudo apt install pandoc
```

No `pip install` needed. The script declares its Python dependencies via PEP 723 inline metadata. `uv run` reads them and installs automatically in an isolated environment.

## Usage

### Writing (via Kiro agent)

Ask the agent to create a technical document. The agent follows SKILL.md to:
1. Scaffold numbered `.md` files in a draft folder
2. Write content following the style guide (Indonesian body, English headings, second-person perspective)
3. Create a cover file with YAML metadata

### Converting to DOCX

From your project root:

```bash
uv run .kiro/skills/technical-document-writer/scripts/md_to_docx.py \
  --source ./draft \
  --output output.docx
```

The `--template` flag defaults to the bundled `assets/template.docx`. Override with your own:

```bash
uv run .kiro/skills/technical-document-writer/scripts/md_to_docx.py \
  --source ./draft \
  --template ./my-template.docx \
  --output output.docx
```

### CLI Options

| Flag | Default | Description |
|------|---------|-------------|
| `--source`, `-s` | `draft` | Folder containing `.md` files |
| `--template`, `-t` | bundled `assets/template.docx` | Reference template for styling |
| `--output`, `-o` | `output.docx` | Output file path |
| `--no-toc` | off | Disable table of contents |
| `--toc-depth` | `3` | Heading depth for TOC |
| `--skip-first` | off | Skip the first file in sort order |

## Customizing Styles

Edit `assets/template.docx` in Word (modify styles, not content), save, re-run the script. Generate a fresh base template:

```bash
pandoc -o template-base.docx --print-default-data-file reference.docx
```
