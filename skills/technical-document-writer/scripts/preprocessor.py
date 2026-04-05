"""
Obsidian Markdown Preprocessor
Transforms Obsidian-specific syntax to standard Markdown for Pandoc compatibility.
"""

import re

CALLOUT_EMOJI = {
    "note": "📝",
    "abstract": "📄",
    "summary": "📄",
    "tldr": "📄",
    "info": "ℹ️",
    "tip": "💡",
    "hint": "💡",
    "important": "💡",
    "success": "✅",
    "check": "✅",
    "done": "✅",
    "question": "❓",
    "help": "❓",
    "faq": "❓",
    "warning": "⚠️",
    "caution": "⚠️",
    "attention": "⚠️",
    "failure": "❌",
    "fail": "❌",
    "missing": "❌",
    "danger": "🔴",
    "error": "🔴",
    "bug": "🐛",
    "example": "📋",
    "quote": "💬",
    "cite": "💬",
    "todo": "☑️",
}


def preprocess(content: str) -> str:
    """Orchestrator: run all preprocessing rules in order."""
    content = strip_frontmatter(content)
    content = strip_comments(content)
    content = convert_mermaid(content)
    content = convert_embeds(content)
    content = convert_wikilinks(content)
    content = convert_highlights(content)
    content = convert_callouts(content)
    content = strip_tags(content)
    return content


def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter delimited by --- at the start of the file."""
    return re.sub(r"\A---\n.*?\n---\n?", "", content, count=1, flags=re.DOTALL)


def strip_comments(content: str) -> str:
    """Remove Obsidian comments %% ... %% (inline and block)."""
    content = re.sub(r"%%.*?%%", "", content, flags=re.DOTALL)
    return content


def convert_mermaid(content: str) -> str:
    """Replace mermaid code blocks with a placeholder."""
    def _replace_mermaid(match):
        return "\n[Diagram: Mermaid — render terpisah]\n"

    return re.sub(
        r"```mermaid\n.*?```",
        _replace_mermaid,
        content,
        flags=re.DOTALL,
    )


def convert_embeds(content: str) -> str:
    """Transform Obsidian embeds ![[...]] to standard markdown or placeholder."""
    image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp")

    def _replace_embed(match):
        inner = match.group(1)
        name = inner.split("|")[0].strip()

        if any(name.lower().endswith(ext) for ext in image_extensions):
            return f"![{name}]({name})"

        return f"[Embedded: {name}]"

    return re.sub(r"!\[\[([^\]]+)\]\]", _replace_embed, content)


def convert_wikilinks(content: str) -> str:
    """Transform Obsidian wikilinks [[...]] to bold text."""
    content = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"**\2**", content)
    content = re.sub(r"\[\[([^#\]]+)#\^?([^\]]+)\]\]", r"**\2**", content)
    content = re.sub(r"\[\[([^\]]+)\]\]", r"**\1**", content)
    return content


def convert_highlights(content: str) -> str:
    """Transform Obsidian highlights ==text== to bold."""
    return re.sub(r"==(.+?)==", r"**\1**", content)


def convert_callouts(content: str) -> str:
    """Transform Obsidian callouts > [!type] to blockquote with emoji prefix."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        callout_match = re.match(
            r"^>\s*\[!(\w+)\][-+]?\s*(.*)", line
        )

        if callout_match:
            callout_type = callout_match.group(1).lower()
            title = callout_match.group(2).strip()
            emoji = CALLOUT_EMOJI.get(callout_type, "📝")

            if title:
                result.append(f"> {emoji} **{title}**")
            else:
                result.append(f"> {emoji} **{callout_type.capitalize()}**")

            result.append(">")

            i += 1
            while i < len(lines) and re.match(r"^>", lines[i]):
                continuation = re.sub(r"^>\s?", "", lines[i])
                result.append(f"> {continuation}" if continuation else ">")
                i += 1
            continue

        result.append(line)
        i += 1

    return "\n".join(result)


def strip_tags(content: str) -> str:
    """Remove # from Obsidian tags, preserving heading syntax."""
    return re.sub(r"(?<=\s)#([\w][\w/]*)", r"\1", content)
