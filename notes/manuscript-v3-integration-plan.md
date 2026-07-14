# Codex caretaker plan for manuscript v3

Status: active on `jrl/codex-v3-integration` from 14 July 2026.

Active structural and domain review:
`notes/manuscript-v3-structure-and-domain-review.md`.
It defines the manuscript-facing experiment vocabulary, evidence-led Results order,
figure-trim ledger, and the proposed d02-to-d03 transfer gate.

Active CHPC execution record:
`rewrite/CHPC-V3-FIGURE-RECOMPUTE-HANDOFF.md`.
It is the single source of truth for pending recomputations; the older Batch B text
and the standalone commands in the structural review are rationale, not independent
dispatches.

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
| D | Akamai / Codex, then coauthors | Restore the re-promoted panel if it earns a role; prune v3 to an evidence-led coauthor draft; move only accepted material into `main.tex`. | All rewrite gates are closed or explicitly deferred, figures are admitted, and the resulting PDF is visually reviewed. |

## CHPC Batch B baton

Batch A is pushed.
The remaining line-free overlay work and John's 14 July additions are now factored
into `rewrite/CHPC-V3-FIGURE-RECOMPUTE-HANDOFF.md` with exact hashes, commands,
scratch destinations, copy mappings, allowed writes, stop conditions, and return
branch.
Do not execute the legacy commands independently or regenerate from Akamai's
synthetic smoke-test caches.
CHPC must commit and push the result before Akamai resumes edits to the same files.

## John figure-review additions, 14 July 2026

The next bounded figure pass also carries three review products requested after the
initial v3 trim:

1. keep Figure 1 as two panels, with the archived d01--d03 nesting on the right;
2. compare fine versus coarse static terrain (CMP11, X0 minus X4), not fine-terrain
   nest feedback, using basin-wide d02 and inner-basin d03 top-down heat-deficit
   fields plus orthogonal d03 sections; and
3. replace the dense 12 UTC Horsepool profile with X6 and X5 only at 12 and 13 UTC.

The d02 and d03 terrain views answer different spatial questions.
The d02 panel is required for Browns Park, Split Mountain, and Tavaputs Plateau context;
d03 does not cover all of those features and is retained for inner-basin detail.
Use the same 16 UTC time, X0-minus-X4 sign, 2200 m crest, and +/-1.6 MJ m-2 scale in
both top-down heat-deficit panels.

Exact commands, expected filenames, interpretive limits, and the new bounded d03 config
are in `notes/manuscript-v3-structure-and-domain-review.md` and
`verification/config/figures/pelican2013_terrain_d03.toml`.
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
