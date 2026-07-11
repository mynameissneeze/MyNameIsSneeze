#!/usr/bin/env python3
"""
Picks a random pixel image from pixels.json and swaps it into README.md
between the <!-- PIXEL:START --> / <!-- PIXEL:END --> markers.
"""
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
PIXELS_FILE = Path(__file__).resolve().parent / "pixels.json"

START_MARKER = "<!-- PIXEL:START -->"
END_MARKER = "<!-- PIXEL:END -->"


def main() -> int:
    pixels = json.loads(PIXELS_FILE.read_text())
    if not pixels:
        print("No pixels found in pixels.json", file=sys.stderr)
        return 1

    readme_text = README.read_text()

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if not pattern.search(readme_text):
        print("Could not find PIXEL markers in README.md", file=sys.stderr)
        return 1

    # Try to avoid picking the same pixel twice in a row.
    current_match = re.search(r'src="([^"]+)"', readme_text[
        readme_text.index(START_MARKER):readme_text.index(END_MARKER)
    ])
    current_url = current_match.group(1) if current_match else None

    choices = [p for p in pixels if p != current_url] or pixels
    new_pixel = random.choice(choices)

    new_block = f'{START_MARKER}\n<img src="{new_pixel}" width="99">\n{END_MARKER}'
    new_text = pattern.sub(new_block, readme_text, count=1)

    if new_text == readme_text:
        print("No change needed (picked the same pixel).")
        return 0

    README.write_text(new_text)
    print(f"Updated pixel to: {new_pixel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
