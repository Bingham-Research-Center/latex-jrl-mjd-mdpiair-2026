# Repository Guidelines

This is the private working repository for an MDPI **Air** manuscript about WRF meteorology during the 2 February 2013 Uinta Basin winter-ozone episode.

## Cold start

1. Read `README.md`.
2. Read `notes/narrative-and-hypotheses.md` for framing work or `notes/claim-evidence-ledger.md` before changing a scientific claim.
3. Open only the relevant manuscript, provenance record, script, table, or figure.

Do not ingest `Definitions/`, every file under `verification/`, or all of `~/reviews` by default.

## Evidence rules

- Treat `main.tex`, notes, scripts, tables, and prior papers as claims to reconcile, not mutually validating truth.
- Separate controlled touchstone comparisons, heterogeneous historical references, and literature yardsticks.
- Do not render draft numbers until the evaluation window, stations, run identity, and source artifact match.
- Never call `trang_ref` the literal Tran et al. (2018) run.
- Only files listed as `promoted` in `figures/MANIFEST.md` may be included by `main.tex`.
- Synthetic tests must write only to temporary directories.

## Hosts

Check `hostname -f` and path existence first.

- Akamai/Linode: manuscript work and selective Markdown critiques under `~/reviews`.
- CHPC: WRF and publication-figure work; archive root `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/`.
- `wrf-full-figures` is canonical only when its skill is actually installed and readable; otherwise record that styling remains provisional and use documented `brc-tools` conventions.

## Manuscript conventions

- Keep `main.tex` single-file and sparse.
- Use American English and one sentence per source line.
- Compile with pdfLaTeX + BibTeX through `latexmk -pdf main.tex`; do not switch to XeLaTeX or biber.
- Do not edit `Definitions/`; refresh it only from an official MDPI archive.
- Replace `paperpile.bib` as a complete Paperpile export; do not hand-edit an exported library.
- Routine `main.pdf` is ignored. Commit only meaningful dated PDFs under `drafts/`.

## Commands

```bash
make pdf
make check
make smoke
make submission
```

Before committing, confirm a clean build where Ghostscript is available, run `git diff --check`, and inspect the PDF when prose, citations, figures, or layout changed.

## Git

- New work uses `jrl/<topic>` branches and PRs after the foundational setup.
- Keep commits limited to one coherent manuscript or analysis concern.
- Use John’s configured identity and add a Codex co-author trailer for Codex-assisted work.
- Preserve Michael’s inherited authorship; do not add people or tools to commits they did not contribute to.
- Push after each substantial, verified batch.
