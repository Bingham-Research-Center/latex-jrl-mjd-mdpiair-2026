# MDPI *Air* submission package

Complete, self-contained package for:

> **WRF Cold-Pool Sensitivities Relevant to Winter-Ozone Modelling in the Uinta Basin**
> John R. Lawson, Michael J. Davies, Loknath Dhar, and Seth N. Lyman

This is the **single** package used both for co-author review and for journal
submission — the contents are identical, prepared as a peer-review submission.

## Contents

| File | What it is |
|---|---|
| `main.tex` | Main article (MDPI `air` class). |
| `main.pdf` | Compiled main article. |
| `paperpile.bib` | Bibliography database. |
| `main.bbl` | Pre-built bibliography (lets `main.tex` compile without re-running BibTeX). |
| `Definitions/` | The MDPI class and support files needed to compile. |
| `figures/` | Every figure referenced by the main article. |

## Compiling

Requires a TeX distribution (TeX Live, MiKTeX, or TinyTeX) with the usual packages.
From inside this folder:

```
latexmk -pdf main.tex
```

- `main.tex` uses BibTeX (apacite). Because `main.bbl` is included, a plain
  `pdflatex main` also resolves the references if BibTeX is unavailable.
The compiled `main.pdf` is already included, so reviewers can read it directly without compiling.
The former separate supplement is retired; material required for review is integrated into the main article or appendix.

*Regenerate this folder from the repository root with `make package`.*
