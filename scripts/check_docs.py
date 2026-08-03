#!/usr/bin/env python3
"""Check local links in Markdown files.

The public repository uses many small documents. This script verifies that
relative file links still point to an existing file or directory.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")


def clean_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target)


def check_file(markdown_file: Path) -> list[str]:
    errors: list[str] = []
    text = markdown_file.read_text(encoding="utf-8")

    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in MARKDOWN_LINK.finditer(line):
            target = clean_target(match.group(1))
            if not target or target.startswith(SKIP_PREFIXES):
                continue

            path_part = urlsplit(target).path
            if not path_part:
                continue

            resolved = (markdown_file.parent / path_part).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{markdown_file.relative_to(ROOT)}:{line_number}: "
                    f"link escapes repository: {target}"
                )
                continue

            if not resolved.exists():
                errors.append(
                    f"{markdown_file.relative_to(ROOT)}:{line_number}: "
                    f"missing link target: {target}"
                )

    return errors


def main() -> int:
    markdown_files = sorted(ROOT.rglob("*.md"))
    errors: list[str] = []

    for markdown_file in markdown_files:
        if ".git" in markdown_file.parts:
            continue
        errors.extend(check_file(markdown_file))

    if errors:
        print("Documentation link check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Documentation link check passed: {len(markdown_files)} Markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
