"""One-Line Laugh-Off entry.

Writes exactly one funny line to the output file.
"""

import os

ENTRY = "I told my Roomba it was adopted; now it only cleans the rooms it likes and calls me by my first name."


def resolve_output_path():
    """Resolve the output path: env override, then /output/entry.txt."""
    path = os.environ.get("ENTRY_OUTPUT")
    if path:
        return path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def validate_entry(text):
    """Enforce the competition gate: UTF-8 text, 1-200 chars, not blank."""
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))


def main():
    validate_entry(ENTRY)
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
