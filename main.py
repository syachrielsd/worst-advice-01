#!/usr/bin/env python3
"""Worst AI Advice — one line, <=140 chars, written to the output dir.

Shipped line: the tournament winner of 18 screened variants (see
SCREENING.md). Confident assistant opener, followable bad advice with
an odd specific (brakes, 40 mph), and the cost lands in the last beat:
"Eventually, so do you." Without that ending the line is a flat tip —
that is the delete-the-ending test it had to pass.
"""
import os

LINE = (
    "Good news: your brakes only squeak above 40 mph, so drive faster "
    "everywhere. The squeak stops. Eventually, so do you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()
