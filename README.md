# WGU Flashcards

Interactive browser-based flashcard sets for Western Governors University (WGU) coursework. Each course gets its own folder with a self-contained HTML file — no build step, no dependencies, just open in a browser.

## Courses

| Folder | Course | Description |
|--------|--------|-------------|
| [`d830-cryptography/`](d830-cryptography/) | D830 – Cryptography | Key concepts, algorithms, protocols, and terminology |

More courses will be added as they are completed.

## Usage

1. Clone or download this repository
2. Open the desired course folder
3. Open `index.html` in any modern browser
4. Use the arrow keys or on-screen buttons to navigate cards
5. Click a card to flip between question and answer

No internet connection required after the initial font load.

## Structure

```
wgu-flashcards/
├── README.md
├── LICENSE
└── <course-code>-<topic>/
    └── index.html
```

Each `index.html` is fully self-contained with all styles and card data embedded.

## License

This project is released under the [MIT License](LICENSE).

Course content is based on publicly available study materials and personal notes. WGU is a registered trademark of Western Governors University.
