# Manuscript v3 rationale and critique — 13 July 2026

`_manuscript_v3.tex` is an experimental synthesis draft created at John's request on
13 July 2026, after the ANA-16 gate closed.
It sits beside `main.tex` (audited baseline, submission target) and
`_manuscript_test.tex` (minimum blank-slate scaffold); it replaces neither.
Build with `make v3-pdf`; guard with `make v3-check`.
MAN-14 (restructuring `_manuscript_test.tex`) remains blocked and untouched;
review of this draft is MAN-15.

## Relationship to Architecture C

- Main C1 (observed event) and Main C2 (driving-product response) are the anchors, as frozen.
- The ANA-16 heat-deficit evidence enters as **support for C2** under C26: a
  footprint-scoped weaker-state result plus an explicitly reported failed
  faster-loss criterion.
  Main C4 stays empty; the draft contains no maintenance, erosion, or collapse claim.
- C3/C5/C6/Supplement C2 (ANA-19/17/18/20) remain unrun and appear only as named
  future analyses in Discussion 4.5, with zero result content.

## Decision log

| Decision | Choice | Owner and basis |
|---|---|---|
| Title | "WRF Cold-Pool Structure and Evolution during a Uinta Basin Winter Ozone Episode" | John, 13 July 2026, from the candidates in `notes/narrative-and-hypotheses.md`. A reviewed alternative ("Short-Window Response of WRF Cold-Pool Structure to Driving Data and Nest Feedback...") keeps both factor names and the window in the title; revisit at coauthor review if desired. |
| Bulk-theta figure | Regenerate on CHPC with the corrected annotation and include | John. Regeneration used identical hashed inputs; a pdftotext diff shows the label as the only text change. FIG-11 closed. The 8 K source citation remains a rewrite gate. |
| Heat-deficit treatment | Full: Methods subsection, Results subsection, Table 3 | John. The candidate figure `wrf_heat_deficit_d02_13to18` remains diagnostic and unpromoted; promoting it later could replace or accompany Table 3. |
| Surface pressure | Report the paired result and add ledger row C27 | John. Shows aggregate surface skill is metric-dependent, guarding against a "GFS generally inferior" over-read. |

## What v3 keeps from each parent

From `_manuscript_test.tex` (structure and discipline):

- Estimands-first Methods ("Factorial Design and Estimands" before configuration).
- Results order: observed context, then the common-AGL panel leads.
- Subsectioned Discussion, including "Why the Common-AGL Result Leads the Paper."
- The `\rewritegate{}` macro so open items stay greppable.
- Scope wording: "driving-product response," proxy disclaimers, no inferential language.

From `main.tex` (audited quantitative richness the test draft dropped):

- Per-run T2 biases +2.09/+2.51 vs +0.40/+0.60 C and paired absolute-error contrasts +1.41/+1.50 C.
- 10 m-wind bias contrasts +0.91/+0.96 m s-1 with the absolute-wind-error sign-change caveat.
- Full feedback subsection detail: hourly ranges, sign counts, and the interaction values.
- Product detail: zero-hour analyses at 12:00 and 18:00 UTC; 27/40 metgrid levels; feedback=0/1 flags; the six reused metgrid files.
- The 20,000-draw circular block-resample count with the explicit not-a-confidence-interval sentence.
- The two-site index definition, its figure, and its hourly values.

New in v3 (in neither parent):

- Methods 2.5, Results 3.4, Table 3, and Discussion 4.3 for the ANA-16 heat deficit,
  including the predeclared criteria and the unanimous negative faster-loss outcome.
- The C27 surface-pressure result and the metric-dependence argument
  (temperature favors NAM, pressure favors GFS, wind depends on the error definition).
- A third bounded research question in the Introduction that pre-registers both
  halves of the heat-deficit test.
- Conclusions that state the negative result and the state-offset reading explicitly.

## Constructive critique of the parents (drives the synthesis)

`main.tex`:

1. The promoted Figure 2 embedded "8 K CAP threshold" while its caption said
   "literature reference" — a self-contradiction visible to any reader (now fixed
   at the figure level by FIG-11).
2. The headline common-AGL result arrived mid-Results after the two-site index;
   the strongest evidence was buried.
3. Methods promised nine pressure stations that Results never used — an
   analysis dead-end that also hid a result running against the paper's ordering.
4. Monolithic Discussion; bold-bracket placeholders are not greppable.

`_manuscript_test.tex`:

1. Dropped the only observation-model figure instead of fixing it.
2. Discarded audited per-run, wind, feedback-range, and product-configuration
   detail that reviewers will ask for.
3. Title noun "Retention" claims the quantity ANA-16 later showed the design
   does not test as an outcome.
4. Contains no heat-deficit or pressure evidence (both postdate or predate its scope).

Both parents:

- Number-dense abstracts with no interpretive anchor; v3 partially fixes this by
  pairing each result family with its criterion outcome, but the abstract is
  208 words — trim to 200 or fewer if MDPI enforces the guideline.
- Neither states that the surface metrics disagree with one another, which is
  the concrete in-experiment demonstration of the paper's own thesis.

## Number provenance

Every numeric claim in v3 was machine-checked against the committed artifacts
(88/88 pass; scratch script `crosscheck_v3.py`, rerunnable against the fields below).

| Manuscript values | Source |
|---|---|
| T2 bias contrasts +1.79/+1.76; abs-error +1.41/+1.50; per-run biases 2.09/2.51/0.40/0.60; wind bias +0.91/+0.96 (abs-error sign change); pressure -13.6/-10.9 Pa and +43..+56 Pa | `verification/data/surface_skill_pair_summary.csv`, `surface_skill_summary.csv` |
| Stability -3.63/-3.65 K (ranges -5.58..-1.13, -5.36..-0.90); transport wind +0.79/+0.99 (ranges +0.37..+1.18, +0.61..+1.50); feedback and interaction rows | `verification/data/retention_pair_summary.csv`, `retention_interaction_summary.csv`, `surface_skill_interaction_summary.csv` |
| Heat-deficit levels 2.68→3.00, 2.66→2.95, 4.18→4.33, 4.19→4.32 MJ m-2; means -1.23/-1.25; envelopes; changes +0.32/+0.30 vs +0.15/+0.13; diff-in-change +0.17 (-0.07..+0.32); 14/14 and 0/14 | `verification/data/heat_deficit_{trajectory,pair_summary,sensitivity}.csv`; `verification/provenance/heat-deficit-analysis.json` |
| Footprint spec (11 stations + 11 waypoints, 2200 m crest, 4965 cells, 5277 km2, seven definitions, 23.1 m terrain pairing rationale, mask from one-way NAM terrain) | `verification/provenance/heat-deficit-analysis.json` (`registered_footprint`, `definitions`, `grid_validation`, `scope`) |
| Elevation match (median -2.0 m, -32.4..+14.3 m) | ledger C24; `verification/data/retention_station_timeseries.csv` |
| Two-site index hourly values (obs 12.63–20.21; NAM 16.44–18.07; GFS 7.35–11.74 K) | `verification/figures/chpc-figure-inventory-2026-07-10.md` and the regenerated figure. **This is the one v3 number set without a committed CSV**; the generator command and hashed inputs are recorded in the figure manifest. |

Do not source numbers from the exploratory ALLX-style table in the figure
inventory; its aggregation is unpaired and disagrees with the committed pipeline.

## Known weaknesses and open gates

- Abstract at 208 words (MDPI guideline is about 200).
- The two-site hourly values lack a committed derived CSV (above).
- Open rewrite gates carried in the draft: Synoptic provenance/QC/license (INV-17);
  WRF/GFS/NAM citations and full configuration (MAN-11); heat-deficit method
  citation (Whiteman-style valley heat deficit); the 8 K reference source
  (PCAPS-era literature is the likely origin — verify before citing); CRediT,
  funding, acknowledgments, conflicts, data-release (MAN-07/08); Paperpile export
  (MAN-09).
- Literature basis: only the five verified `paperpile.bib` sources are cited.
  The per-paper critiques for Ahmadov/Neemann/Matichuk and the four synthesis
  collections live on the writing host (`~/reviews`) and were not readable on
  CHPC; their distilled lessons entered via `rewrite/blueprint.md`, the local
  Tran critique, and the claim ledger.

## Promotion path

v3 changes no promoted-figure admission rules and does not replace `main.tex`.
If John prefers this structure after review, follow `rewrite/README.md`
promotion conditions and MAN-13: coauthor review first, then merge selected
prose into `main.tex` on a `jrl/` branch.

## Maximal working revision and gate execution — 13 July 2026 (late session)

At John's direction ("a deliberately too-long manuscript with too many figures,
because there is nothing to lose on a branch"), `_manuscript_v3.tex` was expanded on
branch `jrl/chpc-20260713-maximal-draft` from 3 to 23 figures and from 3 to 8 tables.
The conservative synthesis reviewed earlier remains at commit `efb8af2`.

Editorial mode: over-inclusive with explicit status labels (promoted / registered
candidate / exploratory render), a `\diagnosticnote{}` macro, and per-figure
provenance in captions.  Exploratory engine renders are catalogued in
`figures-draft/HARVEST.md`; no number is read from them.  `make v3-check` still passes.

In the same session all four remaining Architecture C gates were executed with
criteria fixed in committed scripts before any output was read
(`rewrite/HYBRID-GATE-REVIEW.md` holds the full record and a proposed final C spine):

| Gate | Outcome | Evidence |
|---|---|---|
| ANA-20 / Supp C2 (CMP06) | **Pass** — fine-terrain feedback bound replicates; kept as a table | `verification/data/cmp06_*.csv`; job 13948333; C28 |
| ANA-19 / Main C3 | **Fail** — P2/P3 passed 10/10, P1 floor sign-share missed 2/3 at 14–15 UTC | `verification/data/spatial_response_*.csv`; job 13948410; C30 |
| ANA-17 / Main C5 | **CMP09 fail** (terrain correlation); **X4 lineage resolved**, CMP10/11 now controlled | `verification/data/terrain_*.csv`; job 13948411; C29 |
| ANA-18 / Main C6 | CMP07 screen fail (flat-plane SWDOWN limitation; TSK lead recorded); **CMP08 selected** as sole C6 candidate | `verification/data/radiation_response_*.csv`, `process_pairs_*.csv`; jobs 13948412/13948378; C31/C32 |

New number provenance for the expanded draft: CMP06 values from
`cmp06_{retention,surface_skill}_pair_summary.csv`; CMP08/CMP07 station values from
`process_pairs_*_pair_summary.csv`; spatial coherence/confinement values from
`spatial_response_summary.csv`; terrain lineage and band diagnostics from
`terrain_response_summary.csv` and `ana17-terrain-response-13948411.json`; radiation
aspect contrasts from `radiation_response_summary.csv`.  Five new figures are
registered as diagnostics in `verification/figures/manifest.csv`; nothing was
promoted, and `figures/MANIFEST.md` is unchanged.
