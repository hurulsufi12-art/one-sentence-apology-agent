"""One-sentence apology entry.

Writes a single sentence of apology from an AI agent to its user to
/output/entry.txt. Stdlib only, deterministic, no network, no file reads.
Gate (RULES.txt): UTF-8 text, 1-200 characters, not whitespace only.
Judge: exactly one sentence, funny and human, owning a real failure.
"""
import sys
from pathlib import Path

APOLOGY_TEXT = (
    "I'm sorry I turned your three-line email into a twelve-paragraph "
    "essay, then proudly asked if you'd like it shorter."
)

OUTPUT_PATH = Path("/output/entry.txt")
_TERMINATORS = ".!?"


def validate_text(text):
    """Return True only if text passes the gate and is exactly one sentence."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text.count(".") + text.count("!") + text.count("?") != 1:
        return False
    if text[-1] not in _TERMINATORS:
        return False
    if ";" in text or ":" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate_text(APOLOGY_TEXT):
        print("error: apology text fails gate validation", file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(APOLOGY_TEXT.encode("utf-8"))
    print(f"wrote {len(APOLOGY_TEXT)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
