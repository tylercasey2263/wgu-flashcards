# WGU Flashcards

Interactive browser-based flashcard sets for Western Governors University (WGU) coursework. Each course gets its own folder with a self-contained HTML file — no build step, no dependencies, just open in a browser.

**Live site:** https://tylercasey2263.github.io/wgu-flashcards/

## Courses

| Course | Description | Link |
|--------|-------------|------|
| D830 – Cryptography | Key concepts, algorithms, protocols, and terminology | [Open](https://tylercasey2263.github.io/wgu-flashcards/d830-cryptography/d830_flashcards.html) |

More courses will be added as they are completed.

## Usage

Open the live site above, or clone and open locally:

1. Clone this repository
2. Open the desired course folder
3. Open `<code>_flashcards.html` in any modern browser

**Flashcard mode controls:**

| Key / Action | Effect |
|---|---|
| `Space` or click card | Flip card |
| `→` (after flipping) | Mark as "Got It" |
| `←` (after flipping) | Mark as "Review Again" |
| `S` | Shuffle deck |

**Modes:** switch between **Flashcard** (interactive study) and **Browse** (scrollable list of all cards).

No internet connection required after the initial font load.

## Structure

```
wgu-flashcards/
├── index.html                          ← course hub / landing page
├── README.md
├── LICENSE
├── .gitignore
└── <course-code>-<topic>/
    └── <course-code>_flashcards.html   ← e.g. d830_flashcards.html
```

Each flashcard file is fully self-contained with all styles and card data embedded.

## License

This project is released under the [MIT License](LICENSE).

Course content is based on publicly available study materials and personal notes. WGU is a registered trademark of Western Governors University.
