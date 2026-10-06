# Editable MDPI Air proof

**Edit [air-4472509-done.tex](air-4472509-done.tex) in this directory.**

Full path: `/uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1/proof-package/working/air-4472509-done.tex`.
Branch: `jrl/proofs-round1`.
The sibling `../air-4472509-english/` directory is the preserved received bundle.

Compile from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex
```

The source embeds `thebibliography`; it does not require a separate BibTeX run or `main.bbl`.
The MDPI template, logos, bibliography inputs and eleven figure files are included.
Compilation outputs and this directory's manuscript PDF are ignored by Git.
Root `main.tex` and `submission-package/` are separate later integration targets.

Follow [the proof query catalogue](../../notes/proof-query-catalogue.md) for decisions and remaining work.
The working source is an in-progress author proof with unresolved placeholders; a successful build does not establish submission readiness.
