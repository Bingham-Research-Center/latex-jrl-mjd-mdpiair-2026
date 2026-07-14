# Codex caretaker plan for manuscript v3

Status: active on `jrl/codex-v3-integration` from 14 July 2026.

Literature closure now means the discovery pass is closed and controlled manuscript
integration has begun.
`_manuscript_v3.tex` remains an over-inclusive working revision, `main.tex` remains the
audited baseline, and Codex is the caretaker for selecting and verifying what survives.

## Batch order

| Batch | Host and owner | Work | Exit condition |
|---|---|---|---|
| A | Akamai / Codex | Apply citation-independent literature corrections; remove the non-equivalent 8 K comparison from code and manuscripts; withhold its stored renders; clarify the heat-deficit method and literature caveats. | Builds and repository checks pass; no manuscript includes a withheld figure. |
| B | CHPC / bounded figure task | Pull Batch A; verify frozen-cache SHA-256 `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64`; rerun the two overlay commands in `verification/figures/chpc-figure-inventory-2026-07-10.md`; confirm the new PDFs contain no 8 K line; inspect; update hashes and both manifests; re-promote only the X6/X5 panel if it passes. | A real-data, line-free render is inspected and committed with complete hashes; no synthetic or current-network substitute is used. |
| C | Akamai / John plus Codex | John replaces `paperpile.bib` with a small curated Paperpile export; Codex records its generated keys and inserts only citations that already have verified source passages. | Every retained citation resolves; no key is guessed or hand-edited. |
| D | Akamai / Codex, then coauthors | Restore the re-promoted panel if it earns a role; prune v3 to an evidence-led coauthor draft; move only accepted material into `main.tex`. | All rewrite gates are closed or explicitly deferred, figures are admitted, and the resulting PDF is visually reviewed. |

## CHPC Batch B baton

Do Batch B only after Batch A is committed and pushed.
Use the exact first overlay command at lines 570--579 of
`verification/figures/chpc-figure-inventory-2026-07-10.md` for the manuscript panel and
the second command only to refresh the tracked feedback candidate.
Do not regenerate from Akamai's synthetic smoke-test caches.
After visual inspection, copy only the accepted X6/X5 PDF into `figures/`, update its
candidate and promoted hashes, and record the generator commit used.

Commit and push the CHPC result before Akamai resumes edits to the same files.
This push/pull baton is the default; separate host branches are preferable if both hosts
must work concurrently.

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
