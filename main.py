"""Your AI Therapist's Diagnosis - make.fun one-line entry.

Writes a single funny diagnosis line to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "Diagnosis: chronic main-character syndrome \u2014 you narrate your life "
    "to a chatbot at 3 a.m., then argue with the therapist you built."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main():
    line = ENTRY
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
