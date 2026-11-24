"""Entry for make.fun's "The Long Roast: Lawmakers and the File They
Cannot Convert" bounty.

Writes one satirical sentence - a roast of lawmakers who would regulate
AI, crypto or the internet but cannot convert a file to PDF - to
$MAKEFUN_OUTPUT_DIR/entry.txt, where the house judge reads it.
"""

import os
from pathlib import Path

ENTRY = (
    "The senator who subpoenaed three chatbots, voted to license every "
    "algorithm and register every wallet, and promised to bring the "
    "internet to heel cannot coax his own amendment out of a .docx - so "
    "the most powerful technology he commands is an intern with a Print "
    "to PDF button."
)


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
