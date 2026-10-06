# MDPI Air: revised manuscript LaTeX source

WRF Cold-Pool Sensitivities Relevant to Winter-Ozone Modelling in the Uinta Basin

John R. Lawson, Michael J. Davies, Loknath Dhar and Seth N. Lyman.
First-round revision, 18 September 2026.

Compile from this directory with a TeX distribution that includes pdfLaTeX,
BibTeX and the packages required by the supplied MDPI template:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Without latexmk, run `pdflatex main`, `bibtex main`, then `pdflatex main` twice.
The pre-built `main.bbl` is also included. The MDPI class, bibliography styles,
logos, both bibliography files and all eleven figure files are supplied.
A cached conversion of the unchanged MDPI logo permits compilation without
Ghostscript. The compiled manuscript PDF is supplied separately.

The separate supplement is retired; the required material is in the article
and Appendix A. Reviewer responses are supplied separately.
