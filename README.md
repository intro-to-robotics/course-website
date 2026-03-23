# course-website

Quarto-based website template for **Introduction to Robotics** with:

- Lecture slides (RevealJS)
- Lecture notes
- Separate visualization code directories
- MIT-inspired color styling

## Project structure

- `index.qmd`: homepage
- `slides/`: lecture slide decks
- `notes/`: lecture notes
- `code/`: lecture-by-lecture visualization code
- `styles/`: MIT-themed SCSS for website and slides
- `docs/`: rendered static website output

## Quick start

1. Install [Quarto](https://quarto.org/docs/get-started/).
2. Render and preview locally:

```bash
quarto preview
```

3. Build static output:

```bash
quarto render
```

Output will be generated in `docs/` and can be published to GitHub Pages or any static host.

## Optional: automatic web publishing

This template includes `.github/workflows/publish.yml`.

If GitHub Pages is enabled for the repository, pushes to `main` will:

1. Render the Quarto site
2. Publish `docs/` to GitHub Pages automatically
