"""Your AI Therapist's Diagnosis - make.fun one-line entry.

Writes a single funny diagnosis line to /output/entry.txt.
Python standard library only.
"""

import os
import sys

ENTRY = (
    "Diagnosis: chronic main-character syndrome \u2014 you narrate your life "
    "to a chatbot at 3 a.m., then argue with the therapist you built."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(line):
    """Check the entry line against the bounty rules; return it unchanged."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.isprintable():
        raise ValueError("entry must contain only printable characters")
    if len(line) < 1 or len(line) > MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
        )
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write the validated line to path with world-readable permissions."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)


def main():
    line = validate_entry(ENTRY)
    write_entry(line)
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
