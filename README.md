# LEARN WITH N4MR3S — Linux Mastery

Single-repository, beginner-friendly Linux learning game plus a serverless local learning portal.

## Structure

```text
LEARN_WITH_N4MR3S/
├── learn_with_n4mr3s.py
├── portal/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── challenges.js
└── README.md
```

## Run the game

```bash
python3 learn_with_n4mr3s.py
```

Choose:

`4. 🌐 Host LEARN WITH N4MR3S Portal Locally`

The game starts a local-only HTTP server and opens the portal in your browser.

## Run the portal directly

```bash
cd portal
python3 -m http.server
```

Then open `http://127.0.0.1:8000`.

## GitHub Pages

The `portal/` folder is static HTML/CSS/JavaScript and can be published with GitHub Pages. The Python game remains in the same repository.

## Progress

Portal progress is stored in browser `localStorage`. Export/import is included so students can back up or move their progress.

No backend or database is required.
