#!/usr/bin/env python3
"""
Assembles WGU flashcard HTML files from a template + card data files.

Card data files live in _build/cards/ and have this format:
  # title: WGU D268 – Introduction to Communication Flashcards
  # badge: WGU D268
  # h1: Introduction to Communication: Connecting with Others
  # folder: d268-communication
  # file: d268_flashcards.html
  [
    { cat: "...", q: "...", a: "..." },
  ]

Usage: python assemble.py
"""

import os, re, pathlib

ROOT   = pathlib.Path(__file__).parent.parent
BUILD  = pathlib.Path(__file__).parent
CARDS  = BUILD / "cards"
TMPL   = ROOT / "d830-cryptography" / "d830_flashcards.html"

# Read template
tmpl_text = TMPL.read_text(encoding="utf-8")

# Split on the parts that vary per course
# Part 1 ends just before the title tag content
# We'll use regex substitution

def assemble(card_file: pathlib.Path):
    lines = card_file.read_text(encoding="utf-8").splitlines()
    meta = {}
    card_lines = []
    in_cards = False
    for line in lines:
        if line.startswith("# "):
            k, _, v = line[2:].partition(": ")
            meta[k.strip()] = v.strip()
        else:
            card_lines.append(line)

    cards_js = "\n".join(card_lines)

    title    = meta.get("title",  "WGU Flashcards")
    badge    = meta.get("badge",  "WGU")
    h1       = meta.get("h1",     "Flashcards")
    folder   = meta.get("folder", "unknown")
    filename = meta.get("file",   "flashcards.html")

    html = tmpl_text

    # 1. Replace <title>
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>{title}</title>',
        html
    )
    # 2. Replace badge
    html = re.sub(
        r'<div class="badge">.*?</div>',
        f'<div class="badge">{badge}</div>',
        html,
        count=1
    )
    # 3. Replace h1
    html = re.sub(
        r'<h1>.*?</h1>',
        f'<h1>{h1}</h1>',
        html,
        count=1
    )
    # 4. Replace ALL_CARDS array content
    html = re.sub(
        r'(const ALL_CARDS = \[).*?(\];)',
        r'\g<1>\n' + cards_js + r'\n\g<2>',
        html,
        flags=re.DOTALL
    )

    out_dir = ROOT / folder
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / filename
    out_path.write_text(html, encoding="utf-8")
    print(f"  wrote {out_path.relative_to(ROOT)}")

if __name__ == "__main__":
    CARDS.mkdir(exist_ok=True)
    card_files = sorted(CARDS.glob("*.js"))
    if not card_files:
        print("No card files found in _build/cards/")
    else:
        print(f"Assembling {len(card_files)} course(s)...")
        for f in card_files:
            assemble(f)
        print("Done.")
