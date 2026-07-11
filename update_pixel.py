#!/usr/bin/env python3
"""
Picks a random pixel image URL from pixels.json and swaps it into README.md
between the PIXEL-START / PIXEL-END markers.
"""

import json
import random
import re
import sys
from pathlib import Path

README_PATH = Path("README.md")
PIXELS_PATH = Path("pixels.json")

START_MARKER = "<!-- PIXEL-START -->"
END_MARKER = "<!-- PIXEL-END -->"

# Width of the pixel image in the README (change if you want it bigger/smaller)
IMAGE_WIDTH = 100


def load_pixels():
    if not PIXELS_PATH.exists():
        sys.exit(f"Error: {PIXELS_PATH} not found.")
    with PIXELS_PATH.open("r", encoding="utf-8") as f:
        pixels = json.load(f)
    if not isinstance(pixels, list) or not pixels:
        sys.exit("Error: pixels.json must contain a non-empty list of URLs.")
    return pixels


def get_current_url(readme_text):
    match = re.search(
        rf"{re.escape(START_MARKER)}(.*?){re.escape(END_MARKER)}",
        readme_text,
        flags=re.DOTALL,
    )
    if not match:
        return None
    url_match = re.search(r'src="([^"]+)"', match.group(1))
    return url_match.group(1) if url_match else None


def pick_new_pixel(pixels, current_url):
    choices = [p for p in pixels if p != current_url] or pixels
    return random.choice(choices)


def main():
    if not README_PATH.exists():
        sys.exit(f"Error: {README_PATH} not found.")

    readme_text = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in readme_text or END_MARKER not in readme_text:
        sys.exit(
            "Error: could not find PIXEL-START / PIXEL-END markers in README.md. "
            "Add them where you want the pixel to appear:\n"
            f"{START_MARKER}\n<img src=\"...\" width=\"{IMAGE_WIDTH}\">\n{END_MARKER}"
        )

    pixels = load_pixels()
    current_url = get_current_url(readme_text)
    new_url = pick_new_pixel(pixels, current_url)

    new_block = f'{START_MARKER}\n<img src="{new_url}" width="{IMAGE_WIDTH}">\n{END_MARKER}'

    updated_text = re.sub(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        new_block,
        readme_text,
        flags=re.DOTALL,
    )

    README_PATH.write_text(updated_text, encoding="utf-8")
    print(f"Pixel updated: {current_url} -> {new_url}")


if __name__ == "__main__":
    main()
