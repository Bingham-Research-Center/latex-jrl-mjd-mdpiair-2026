# Blank-slate manuscript workbench

Status: **experimental and non-submission**.

This directory supports a total editorial reconstruction without overwriting the audited review baseline in `main.tex`.
The experimental manuscript stays at repository root as `_manuscript_test.tex` so the MDPI class, bibliography, and promoted figures resolve exactly as they do for `main.tex`.

## Read order

| Need | Open |
|---|---|
| Reopen the Results breadth and figure architecture | `rewrite/RESULTS-EXPANSION-HANDOFF.md` |
| Understand the minimum verified argument and its limits | `rewrite/blueprint.md` |
| Read or edit the experimental paper | `_manuscript_test.tex` |
| Send bounded evidence work to CHPC Codex | `rewrite/CHPC-CODEX-PROMPT.md` |
| Check the source audit that triggered the rewrite | `notes/manuscript-audit-2026-07-13.md` |
| Verify a claim or run identity | `notes/claim-evidence-ledger.md`, then the exact artifact named there |

The blueprint is a compact editorial control packet, not a new scientific authority.
Run identity remains in `verification/provenance/run-inventory.csv`, comparison role in `verification/provenance/comparison-inventory.csv`, figure admission in the two manifests, and claim status in the claim ledger.

## Current work state

The current experimental paper is a deliberately minimal four-run scaffold, not the
chosen scope of the rewritten paper.
The active next step is to audit the wider X0--X10 result matrix, smaller findings, and
figure families through `rewrite/RESULTS-EXPANSION-HANDOFF.md`, then choose a paper
architecture before adding prose.
The held two-site bulk-theta PDF is still not a vertical profile and its promoted copy
still needs the corrected 8 K annotation.
The existing `main.tex` remains intact as a detailed evidence-audit baseline.

## Working contract

- Write only from confirmed ledger rows or verified underlying literature passages.
- Keep product attribution at the GFS-versus-NAM bundle level; do not rename it an isolated initial-condition effect.
- State the exact domain, sample, and window for each result; the confirmed factorial uses five post-spin-up hours on fixed d02 station columns, while other threads require their own matched analysis.
- Treat station medians as one spatial field, not independent replicates.
- Keep chemistry, ozone, basin export, residence time, inversion depth, and multi-day persistence outside the demonstrated result.
- Mark missing provider, model, citation, and author metadata visibly rather than guessing.
- Keep unverified mechanism figures and CHPC-only findings out of prose until their source records are updated.

## Build and promotion

Run:

```bash
make rewrite-check
```

This compiles `_manuscript_test.tex`, checks the repository diff, and rejects known synthetic or wrong-date tokens.
It does not alter the submission target, which remains `main.tex`.

Promote the rewrite only after:

1. every rendered number maps to a confirmed ledger row and reproducible artifact;
2. observation and model-method placeholders are closed;
3. every included figure is current and `promoted` in both manifests;
4. coauthors review scientific interpretation and required back matter;
5. selected prose is deliberately merged into `main.tex`;
6. `make check`, PDF inspection, and the independent submission-package build pass.
