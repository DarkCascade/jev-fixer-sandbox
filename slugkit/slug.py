import re


def slugify(text: str) -> str:
    """Convert text to a lowercase, hyphen-separated URL slug."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]", "-", text)
    return text
