# Uinta Basin winter-ozone meteorology

Public manuscript and evidence history for John R. Lawson, Michael J. Davies, Loknath Dhar and Seth N. Lyman's MDPI *Air* study of the 2 February 2013 episode. The study evaluates WRF meteorology; it does not run atmospheric chemistry.

## Submitted proof

John confirmed return of the corrected proof to MDPI on 11 October 2026. The exact source checkpoint is [`mdpi-air-proof-return-2026-10-11`](https://github.com/Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026/tree/mdpi-air-proof-return-2026-10-11); the [proof TeX](proof-package/working/air-4472509-done.tex), [publisher replies](PROOFER-RETURN-REPLIES.md), and [closeout handoff](PROOFING-HANDOFF.md) are on this branch. The received publisher bundle is preserved under `proof-package/air-4472509-english/`. Generated PDFs and ZIPs are local review artifacts, not Git files.

Build from `proof-package/working/` with `latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex`. The source includes its bibliography, MDPI template and eleven figures. This branch's root `main.tex` is an earlier revision, not the returned proof.

## Evidence

- [Claims and limits](notes/claim-evidence-ledger.md), [run inventory](verification/provenance/run-inventory.csv), [comparison inventory](verification/provenance/comparison-inventory.csv).
- [Figure admission](verification/figures/manifest.csv), [promoted figures](figures/MANIFEST.md), [derived data](verification/data/manifest.csv).
- [First-round revision history](https://github.com/Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026/tree/jrl/peer-review-round1) and [proof query record](notes/proof-query-catalogue.md).

The four-run X6/X10/X5/X3 matrix is the primary comparison. Other diagnostics retain their recorded limits; the repository does not establish chemistry, basin export, inversion depth or multi-day persistence. See [AGENTS.md](AGENTS.md) for the working route.
