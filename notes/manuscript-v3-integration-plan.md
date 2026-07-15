# Codex caretaker plan for manuscript v3

Status: active on `jrl/codex-v3-integration` from 14 July 2026.

Active structural and domain review:
`notes/manuscript-v3-structure-and-domain-review.md`.
It defines the manuscript-facing experiment vocabulary, evidence-led Results order,
figure-trim ledger, and the proposed d02-to-d03 transfer gate.

Executed CHPC Batch B record:
`rewrite/CHPC-V3-FIGURE-RECOMPUTE-HANDOFF.md`.
Its return commit was integrated without alteration as `28eb502` on
`jrl/codex-v3-integration`; `verification/provenance/v3-figure-review-20260714.json`
is the immutable execution record.
The next CHPC dispatch is the separate, single-job finishing pass in
`rewrite/CHPC-V3-FINISHING-PASS.md`.

Literature closure now means the discovery pass is closed and controlled manuscript
integration has begun.
`_manuscript_v3.tex` remains an over-inclusive working revision, `main.tex` remains the
audited baseline, and Codex is the caretaker for selecting and verifying what survives.

## Batch order

| Batch | Host and owner | Work | Exit condition |
|---|---|---|---|
| A | Akamai / Codex | Apply citation-independent literature corrections; remove the non-equivalent 8 K comparison from code and manuscripts; withhold its stored renders; clarify the heat-deficit method and literature caveats. | Builds and repository checks pass; no manuscript includes a withheld figure. |
| B | CHPC / bounded figure task | Execute `rewrite/CHPC-V3-FIGURE-RECOMPUTE-HANDOFF.md`: finish the line-free overlay baton, then the terrain, profile, locator, and radiation-restyle products from existing output. | Every submitted job reaches a terminal state; selected artifacts are inspected, hashed, provenance-recorded, committed, and pushed; no excluded experiment or post-hoc claim is added. |
| C | Akamai / John plus Codex | John replaces `paperpile.bib` with a small curated Paperpile export; Codex records its generated keys and inserts only citations that already have verified source passages. | Every retained citation resolves; no key is guessed or hand-edited. |
| D | Akamai / Codex, then coauthors | Admit only candidates whose exact data and visual review pass; prune v3 to an evidence-led coauthor draft; move only accepted material into `main.tex`. | All rewrite gates are closed or explicitly deferred, figures are admitted, and the resulting PDF is visually reviewed. |

## Cross-server finishing track

Keep one branch, one active owner, and one explicit transition at a time.
Do not edit the integration branch concurrently on Akamai and CHPC.
At each transition, push the branch, record the exact commit in the handoff, and make
the receiving host verify `hostname -f`, branch, HEAD, upstream, and clean status
before running or editing anything.

| Phase | Host | State | Work and handoff condition |
|---|---|---|---|
| F0 | Akamai | complete | Review and integrate the bounded CHPC return as immutable commit `28eb502`; keep `main.tex` unchanged. |
| F1 | Akamai | complete | Auditable bulk-theta and profile CSV emission, offline locator context, the terrain composite, manuscript wiring, and the single-job CHPC handoff are tested and committed. |
| F2 | CHPC | complete | Job `13968404` returned exact CSVs and final candidates from source `92d96b1`; the verified 15-file return is commit `010e833` on `jrl/chpc-20260715-v3-finishing-return`. |
| F3 | Akamai / Codex admission review | complete | PDF and raster inspection, exact-value review, claim-ledger registration, dual manifests, bounded promotions, rewrite-gate closure, and main-figure pruning are complete; CMP11 remains diagnostic. |
| F4 | Akamai / Codex | complete | `make check`, `make rewrite-check`, `make v3-check`, `make smoke`, PDF inspection, and `git diff --check` passed on 15 July 2026; the audited integration is ready to push and open as a PR. |
| F5 | CHPC / Codex | complete | Reusable X8 deficit-transport, horizontal-convergence, bulk, transect, and budget products were added to `brc-tools`; the 26-task generalized archive render is job 13970596 and the final budget refresh is job 13971081. |
| F6 | CHPC / Codex review return | complete | Job 13971080 returned a verified 14-file manuscript packet from manuscript `5a51486` and `brc-tools` `548fee4`; commit `05996b9` preserves the byte-identical return; registries, C36, review-only Appendix B, repository checks, pages 22--24, and `drafts/manuscript-v3_2026-07-15_x8-deficit-transport-review.pdf` were closed on 15 July 2026. |

Current editorial destinations are fixed unless John changes them:

- bulk-theta X6/X5 overlay: promoted for a narrow main-text surface-corroboration role;
- locator: promoted as one coherent geographic map with a nesting inset;
- X6/X5 Horsepool profiles: promoted for appendix supplied-state context only;
- CMP11 terrain maps and sections: registered as one appendix diagnostic, without
  inventing or reversing an evidence gate;
- ANA-18 radiation diagnostic: appendix diagnostic with its failed gate preserved.

## CHPC Batch B record

Batch B completed on CHPC and returned as `6946fd8`; Akamai integrated that exact tree
as `28eb502` after independent branch, provenance, hash, build, and PDF review.
The returned images remain evidence artifacts, not automatic manuscript admissions.
Do not rerun the old handoff or edit its provenance JSON to describe later work.

## John figure-review additions, 14 July 2026

The next bounded figure pass also carries three review products requested after the
initial v3 trim:

1. replace the mismatched two-panel Figure 1 with one sourced geographic locator and
   a compact d01--d03 nesting inset;
2. compare fine versus coarse static terrain (CMP11, X0 minus X4), not fine-terrain
   nest feedback, using basin-wide d02 and inner-basin d03 top-down heat-deficit
   fields plus orthogonal d03 sections; and
3. replace the dense 12 UTC Horsepool profile with X6 and X5 only at 12 and 13 UTC.

The d02 and d03 terrain views answer different spatial questions.
The d02 panel is required for Browns Park, Split Mountain, and Tavaputs Plateau context;
d03 does not cover all of those features and is retained for inner-basin detail.
Use the same 16 UTC time, X0-minus-X4 sign, 2200 m crest, and +/-1.6 MJ m-2 scale in
both top-down heat-deficit panels.

The original raw-render commands remain historical context in
`notes/manuscript-v3-structure-and-domain-review.md`.
The authoritative finishing commands, expected filenames, and return contract are now
in `rewrite/CHPC-V3-FINISHING-PASS.md` and
`verification/slurm/run_v3_finishing_pass.slurm`.
These are exploratory review additions only; they do not change the failed CMP09 gate
or create a post-hoc CMP11 claim.

## Bibliography boundary

The small curated export is deliberately low priority until Batch C.
Citation-independent prose and evidence work should continue now.
Do not normalize, prune, or repair the current `paperpile.bib`; John will replace it
wholesale, and Codex will then integrate the generated keys.

## Immediate reading route

For each new PDF, start with `notes/literature/PDF-HARVEST-WORKFLOW.md` and create one
Akamai harvest packet.
Send CHPC only the bounded run/configuration questions extracted from that packet, not a
second request to reread the whole paper.
