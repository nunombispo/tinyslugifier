"""A tiny slugifier for URL-friendly strings."""

import re


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug (lowercase, hyphens)."""
    if not text:
        return ""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")
