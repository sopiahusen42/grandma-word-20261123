"""Entry for the make.fun bounty "One Word From Grandma".

The program writes exactly one word -- the word a grandma would text about AI
-- followed by a single newline, to entry.txt in the output directory. The
output directory is /output unless the MAKEFUN_OUTPUT_DIR environment variable
overrides it.

It is deterministic: the same word produces the same bytes on every run. There
is no randomness, no clock access and no network use. The word is checked
before writing and the file is read back afterwards to confirm the bytes on
disk are exactly the bytes intended.
"""

import os
import sys

WORD = "robocall"
DEFAULT_OUTPUT_DIR = "/output"


def validate_word(text):
    """Return an error message for an invalid entry word, or None if it is fine.

    A valid word is a single-line string of 1..30 code points that is not
    blank and carries no leading or trailing whitespace.
    """
    if not isinstance(text, str):
        return "entry word must be a string, got %s" % type(text).__name__
    if text.strip() == "":
        return "entry word is blank after strip"
    if not (1 <= len(text) <= 30):
        return "entry word must be 1..30 code points, got %d" % len(text)
    if "\n" in text or "\r" in text:
        return "entry word must be a single line (contains \\n or \\r)"
    if text != text.strip():
        return "entry word must equal its stripped form (leading/trailing whitespace)"
    return None


def main():
    text = WORD

    error = validate_word(text)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    payload = (text + "\n").encode("utf-8")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")

    with open(path, "rb") as handle:
        on_disk = handle.read()

    if on_disk != payload:
        print("error: bytes on disk do not match intended payload", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
