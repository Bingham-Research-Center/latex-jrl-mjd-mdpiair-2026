# Review milestones

Commit only PDFs that mark a meaningful coauthor-review or submission milestone.
Routine `main.pdf` builds remain ignored.

Use `main_<YYYY-MM-DD>_<short-label>.pdf`, for example:

```bash
cp ../main.pdf main_2026-07-10_initial-review.pdf
```

This directory is excluded from the MDPI submission allowlist.

Latest review snapshots:

- `manuscript-main_2026-07-15_final-draft-start.pdf` — audited 17-page candidate
  promoted to `main.tex`; it contains only contract-listed figures and
  citation keys and is the starting point for the final author draft.

- `manuscript-v3_2026-07-15_last-codex-draft.pdf` — over-inclusive 26-page
  caretaker snapshot preserving diagnostic, terrain, radiation, and X8 review
  material without promoting those gated claims to `main.tex`.

- `manuscript-v3_2026-07-14_figure-recovery-review.pdf` — v3 review build restoring
  the common-AGL spatial evolution, vertical sections, heat-deficit trajectory,
  and heat-deficit map as explicitly gated editorial candidates supporting Section 4.

- `manuscript-v3_2026-07-14_contrast-ordered-draft.pdf` — v3 reordered around
  controlled scientific contrasts, with the common-pipeline comparison panel,
  figure trim, and explicit d02/d03 scope at source commit `c43237e`.

- `manuscript-v3_2026-07-14_codex-integrated-maximal-draft.pdf` — maximal v3 after
  the Akamai literature integration at source commit `653a49a`; the non-equivalent
  8 K render is withheld pending line-free CHPC regeneration.
