#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda.

The text is written verbatim, in UTF-8, with no trailing newline, into the
folder named by the MAKEFUN_OUTPUT_DIR environment variable (falling back to
/output), which is created if it does not exist yet.
"""

import os
import sys

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text must be 1-280 characters, got {len(TEXT)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    entry = os.path.join(out_dir, "entry.txt")
    with open(entry, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
