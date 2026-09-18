# Akamai literature-closure record — 14 July 2026

Status: completed/archived.
This file preserves the executed request and its audit trail; it is not an active
queue. Current work is routed through `tasks/final-draft-100.md`.

## Closure handoff — 14 July 2026

The literature-discovery pass is closed and Codex has taken caretaker ownership of the
integration stage on `jrl/codex-v3-integration`.
The active route is `notes/manuscript-v3-integration-plan.md`.
Citation-independent corrections proceed now; CHPC receives one bounded line-free figure
regeneration task; new PDFs use `notes/literature/PDF-HARVEST-WORKFLOW.md`.

`paperpile.bib` work is deliberately downgraded.
John will provide a small curated Paperpile export later, so agents must not spend time
repairing or expanding the current file and must not treat it as a blocker.

## Codex caretaker execution record — 14 July 2026

Host check returned `localhost`, not a CHPC hostname, and work is on `jrl/akamai-lit-closure`.

- [x] **1 — 8 K source:** Lareau et al. (2013) was verified, but its crest-relative sounding deficit is not equivalent to the two-site surface contrast; remove the plotted reference rather than use it as validation (`notes/literature/verified-citations.md`).
- [x] **2 — heat deficit:** Whiteman et al. (1999) and the closest column variant in Adler et al. (2023) were verified, with the present method's departures recorded (`notes/literature/verified-citations.md`).
- [ ] **3 — model/products, partial:** WRF, GFS, NAM, Synoptic wording, current defaults, access terms, and the frozen cache hash are recorded, but exact input hashes, historical Synoptic request/QC, and network reuse rights remain open (`notes/literature/verified-citations.md`).
- [x] **4 — LIT-01:** Matichuk claim, evidence, and caveat rows are complete (`notes/literature/matichuk-claim-rows.md`).
- [x] **5 — LIT-02:** The ten-source design comparison and passage routes are complete (`notes/literature/comparison-table.md`).
- [x] **6 — LIT-05:** Four reports survive for Discussion context, four are dropped from narrative, and none is needed in the Introduction (`notes/literature/report-source-decisions.md`).
- [x] **7 — contradiction sweep:** Eleven source-specific flags are recorded; the direct manuscript correction is removal of the non-equivalent 8 K reference (`notes/literature/contradiction-flags.md`).
- [ ] **8 — MAN-09, deferred / low priority:** The checklist is retained, but John will provide a small curated Paperpile export instead of expanding the current bibliography; `paperpile.bib` remains correctly untouched (`notes/literature/paperpile-export-list.md`).

The original copy-ready prompt is retained below as the task specification and audit trail.

Copy-ready prompt. Run Claude in this repo's clone on the writing host and paste
everything below the rule.

---

You are on the writing host (run `hostname -f` to confirm you are NOT on CHPC).
This host has `~/reviews` (per-paper critiques and synthesis collections) and
Paperpile access; CHPC does not. Your job is literature closure only.

Cold start: read `AGENTS.md`, then `notes/resource-map.md`,
`notes/literature-synthesis-register.md`, and the "Maximal working revision and gate
execution" section of `notes/manuscript-v3-rationale.md`. Context you need: all five
Architecture C evidence gates are now executed (ledger rows C26--C32;
`rewrite/HYBRID-GATE-REVIEW.md`); the working draft `_manuscript_v3.tex` on branch
`jrl/chpc-20260713-maximal-draft` cites only the five verified `paperpile.bib`
sources and carries `\rewritegate{}` markers for every literature hole listed below.

Ground rules (repo contract): a critique or synthesis is a route, not a citation —
every citation you deliver must be verified against the underlying passage (quote it,
with page/section). One sentence per source line in notes. Do not edit any
manuscript, `figures/`, manifests, or the claim ledger. Work on branch
`jrl/akamai-lit-closure`; commit one concern at a time with John's identity; push.

Deliverables, in priority order:

1. **The 8 K reference source** (blocks the promoted Figure caption). Find the
   PCAPS-era (or other) paper that supports an ~8 K bulk/valley potential-temperature
   contrast as a cold-pool yardstick. Deliver: exact reference, quoted passage, and
   whether 8 K is defensible as "literature reference value" for a two-site surface
   theta contrast — or the nearest defensible alternative wording.
   Write to `notes/literature/verified-citations.md`.

2. **Heat-deficit method citation** (Whiteman-style valley heat deficit,
   H = (cp/g) ∫ max{θ_crest − θ, 0} dp). Verify the original formulation and the
   variant closest to ours; quoted passage + reference. Same file.

3. **Model and product citations**: WRF 4.x (exact tech-note/DOI for 4.8.0),
   GFS analysis `gfsanl_4`, NAM analysis `namanl_218` (NCEI/NCEP archive citations
   or DOIs), and the Synoptic Data citation + archive-license/access wording
   (INV-17 support). Same file.

4. **LIT-01**: convert the completed Matichuk critique in `~/reviews` into
   claim / evidence / caveat rows usable in Introduction and Discussion.
   Write to `notes/literature/matichuk-claim-rows.md`.

5. **LIT-02**: the compact comparison table — case, model, meteorological lever,
   chemistry lever, observations, principal confounds — for Ahmadov 2015,
   Neemann 2015, Matichuk 2017, Tran 2018, UBAQR-2019/2020, OSIP-2021,
   Ramboll-2023, the top-down inventory report, and the Rocky Mountain Power
   report. Write to `notes/literature/comparison-table.md`.

6. **LIT-05 recommendation**: which report sources genuinely survive narrative
   freeze (cite the register), each with a one-line justification and where it
   would enter (Introduction motivation, Discussion context, or drop).
   Write to `notes/literature/report-source-decisions.md`.

7. **Contradiction sweep**: anything in `~/reviews` (including the four synthesis
   collections) that contradicts or complicates the draft's Introduction/Discussion
   claims — especially our uses of Ahmadov (inventory conditioning), Matichuk
   (profiles-vs-ozone decoupling), Neemann (snow/cloud bounding treatment, grid
   mismatch), Tran (FDDA nuance). Flag list with passages.
   Write to `notes/literature/contradiction-flags.md`.

8. **MAN-09 staging**: list the exact Paperpile items (titles + keys) a complete
   export must contain to cover items 1--6 plus the existing five, so the export
   can be done in one browser pass. If you can produce the export, replace
   `paperpile.bib` wholesale (never partially) and check every `\citep` key in
   `_manuscript_v3.tex` and `main.tex` resolves. Otherwise write the list to
   `notes/literature/paperpile-export-list.md`.

Do not: guess a citation from memory without a verified passage; touch
`Definitions/`; rename existing bib keys; start any new analysis; edit
this closure record except to preserve the historical result notes.

When done: push the branch and summarize per-item status (done / partial / not
found on this host) at the top of your final message so John can relay it to the
CHPC session.
