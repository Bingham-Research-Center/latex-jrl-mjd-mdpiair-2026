# Evidence longlist — one exhibit per experimental decision

**Purpose.** A *superset* of the paper's figures: for **every experimental decision** we made
(each run, each controlled comparison), name **at least one exhibit** the team can look at to
decide whether that lever earns a place in the manuscript — *including the decision to leave a
run out*. This is deliberately "too much"; promotion to `main.tex` is gated separately by
`figures/MANIFEST.md` (status `promoted` only) and the `comparison-inventory.csv` role column.

**Authorities (do not restate their contents here):** run identity → `verification/provenance/run-inventory.csv`;
what a comparison may support → `verification/provenance/comparison-inventory.csv`; figure coverage/paths →
`verification/figures/archive-inventory.md` (+ `chpc-figure-inventory-2026-07-10.md`); promotable files →
`verification/figures/manifest.csv`. Archive compare root (`CMP`):
`…/lawson-group6/jrlawson/wrf_archive/pelican2013_pub_figures/compare/`.

**Availability correction (13 July 2026).** The earlier gap audit treated X9 as unrendered
and the terrain over-count as open.
This revision follows `archive-inventory.md`: X9 now has a complete standard set, X9-X0
has 21 difference figures, the stale terrain-label duplicates were removed,
`heatdeficit_map` was rendered across the matrix, and the compare root was verified at
324 PNGs.
Those renders make CMP06 analysis-ready; they do not by themselves create a confirmed
claim or promoted manuscript figure.

**Exhibit tiers.**
- **native** = manuscript-style candidate in `verification/figures/candidates/` (promotable).
- **engine** = 300-DPI figure-engine quicklook under `CMP/diff_*/` (exists, but *not* manuscript-native; a rougher exhibit).
- **none** = not plotted yet → a **gap** (see §3).

**Disposition legend:** 🟩 promote-candidate · 🟦 supplement · 🟨 discussion-only · 🟥 confounded — do **not** plot as a clean difference · ⬛ render-the-gap.

---

## §1 Decision ledger — lever → comparison → best exhibit → disposition

| # | Decision / lever | CMP | Best exhibit that EXISTS | Tier | Gap? | Disposition |
|---|---|---|---|---|---|---|
| 1 | **Driving IC: GFS vs NAM (two-way)** | CMP01 | θ x-sections `wrf_xsect_theta_{gfs,nam}_2way_d02_16z` (now shared scale); `wrf_upper_{500,700}hPa_gfs_minus_nam2way`; `wrf_dtheta/t2…gfs2way_vs_nam2way`; `CMP/diff_gfs_nam/` (21) | native+engine | — | 🟩 **primary result** — strongest coverage |
| 2 | **Driving IC: GFS vs NAM (one-way)** | CMP02 | `wrf_retention_ventilation` (4-run); `CMP/diff_gfs_nam_oneway/` (21) | engine (spatial) | native diff **missing** | 🟩 promote + ⬛ render native X10−X3 diff/x-section |
| 3 | **Nest feedback, NAM (1-way vs 2-way)** | CMP03 | `wrf_{t2,dtheta}…nam1way_vs_nam2way`; `wrf_upper_{500,700}…nam1way_minus_nam2way`; θ x-sect `nam_1way`↔`nam_2way` (shared); `CMP/diff_feedback/` (21) | native+engine | — | 🟦 secondary (near-null) — supplement/Results |
| 4 | **Nest feedback, GFS (1-way vs 2-way)** | CMP04 | `wrf_retention…`; `gfs-feedback-factorial-2026-07-10.md`; `CMP/diff_feedback_gfs/` (21) | engine (spatial) | native diff **missing** | 🟦 supplement + ⬛ render native X6−X10 |
| 5 | **Forcing × feedback interaction** | CMP05 | `wrf_retention…`; `retention_interaction_summary.csv` | native | — | 🟦 supplement (descriptive only) |
| 6 | **Feedback at FINE terrain (X9−X0)** | CMP06 | Complete X9 standard set plus `CMP/diff_feedback_terrain3s/` (21) and heat-deficit maps | engine | native matched analysis | 🟦 analysis-ready robustness result — cleaner feedback test than CMP03 (matches control terrain) |
| 7 | **Slope/shading radiation (X1−X0)** | CMP07 | `CMP/diff_slope_shading/` (7, surface only) | engine | local process analysis **missing** | 🟩 candidate Result after radiation/slope/time analysis |
| 8 | **PBL/sfclay scheme MYJ-Eta vs YSU-MM5 (X2−X1)** | CMP08 | `CMP/diff_myj_eta/` (21) | engine | scheme-aware analysis **missing** | 🟩 candidate Result — ⚠ PBLH is scheme-dependent (C19); needs AGL/flux/TKE-aware recompute |
| 9 | **Terrain source: default vs fine 3-arcsec (X3−X0)** | CMP09 | `CMP/diff_terrain_fine/` (21; stale mislabeled duplicates removed) | engine | native matched analysis **missing** | 🟩 candidate Result after terrain-aware analysis |
| 10 | **Terrain source: default vs coarse 5-arcmin (X3−X4)** | CMP10 | `CMP/diff_terrain/` (7) | engine | X4 provenance + matched analysis | 🟩 candidate Result after X4 path reconciliation |
| 11 | **Terrain source: fine vs coarse, widest bracket (X0−X4)** | CMP11 | `CMP/diff_terrain_res/` (21, "headline") | engine | X4 provenance + matched analysis | 🟩 candidate Result after X4 path reconciliation |
| 12 | **Resolution ladder 1 km / 333 m / 111 m (X7/X0/X8)** | CMP12 | — (no valid difference) | none | — | 🟥 **do NOT plot as a resolution difference** — confounded by init time, forecast age, domain count, levels, cadence. Exhibit = the confound table + a 3-panel *domains/terrain* figure labelled "not controlled" |
| 13 | **Driving heritage / SIP nudged reference** | CMP13 | `wrf_xsect_theta_trang_ref`, `…_trang_anlnudge_jan17`, time-heights | native (context) | identity unresolved | 🟨 discussion-only — label "un-nudged SIP-era, config after Tran 2018", never "the Tran 2018 run" |

**Current coverage:** CMP01--CMP05 have manuscript analyses; CMP06--CMP11 have complete or
targeted engine exhibits and are candidate Results with named analysis/provenance gates;
CMP12 is confounded and CMP13 is context only.

---

## §2 Per-experiment figure completeness (X0–X10)

| X | run | full-figure set (63) | manuscript-native candidates | keep/drop for paper |
|---|---|---|---|---|
| X0 | NAM 1-way fine-terrain **control** | ✓ | θ x-sect/time-height (native); transect locator | 🟩 control + **Fig 1** (domain) |
| X1 | +slope/shading | ✓ | — (engine diff only) | 🟩 candidate Result after local-process analysis |
| X2 | +MYJ/Eta | ✓ | — (engine diff only) | 🟩 candidate Result after scheme-aware analysis (C19) |
| X3 | NAM 1-way default | ✓ | native x-sect/time-height + upper/t2/dtheta diffs | 🟩 primary (one-way NAM leg) |
| X4 | NAM 1-way coarse terrain | ✓ | — | 🟩 candidate terrain Result after provenance gate |
| X5 | NAM 2-way default | ✓ | native x-sect/time-height + diffs | 🟩 primary |
| X6 | GFS 2-way default | ✓ | native x-sect/time-height + diffs | 🟩 primary |
| X7 | NAM 2-way **1 km 24 h** | ✓ (216) | — | 🟥 confounded resolution rung — context only |
| X8 | NAM 1-way **111 m 50-lev** | ~86 non-standard | — | ⬛/🟥 fine rung; standardize before use; resolution claim confounded |
| X9 | NAM 2-way fine-terrain | ✓ 63 (+optional families) | engine differences complete | 🟦 analyse CMP06; no WRF rerun needed |
| X10 | GFS 1-way default | ✓ | `wrf_retention` (4-run) | 🟩 primary (one-way GFS leg) |

---

## §3 Gaps to plot — prioritized (the "not yet plotted, and important" set)

1. **Analyse X9−X0 (CMP06) from the completed figures and outputs.** Recompute the matched
   surface/common-AGL and process summaries used for the default-terrain feedback result;
   do not rerender the complete X9 or difference sets merely to prove they exist.
2. **⬛ Native θ *difference* cross-sections + time-heights.** `plot_wrf_cross_sections.py` now takes a
   fixed θ scale but still plots one run at a time. Add a two-run **difference** mode (GFS−NAM,
   1-way−2-way) — the inventory's prescribed "GFS−NAM difference" exhibit that no native figure yet
   provides. One code change unlocks CMP01/02/03/04 native vertical diffs.
3. **⬛ Native spatial diffs for CMP02 & CMP04** (X10−X3, X6−X10) to match the CMP01/CMP03 upper-air set.
4. **🟦 Common-AGL / low-layer zoom** of the x-sections (the 4500 m ceiling compresses the pool);
   a 0–1000 m AGL companion reads the inversion far better.
5. **One decision-grade exhibit each for the CMP07--CMP11 rows selected by the new paper
   architecture.** Do the matched analysis first; do not pre-promote every engine panel.

**Variables/axes still barely exploited** (for the "more variables" instinct): `snow`/`snowh`
fields (near-static, low value), `wspd10` ventilation maps, extra pressure levels (850/600 hPa),
and the **p600 advection** upper-air family exist in the engine sets but have no native exhibit.
Treat these as reviewer-reserve, not first-round.

---

## §4 Pushback — where "too much" must stop

- **Confounded comparisons must not become clean-looking difference plots.** CMP12 (the
  1 km→333 m→111 m ladder) mixes ≥6 uncontrolled axes; a tidy "resolution difference" panel would
  read as a result it cannot support. Its honest exhibit is the confound list + a labelled domains
  figure. Same discipline for any X7/X8 pairing.
- **Provenance gates a figure, not polish.** X4 (terrain5m) still carries an archive-name
  discrepancy. The old terrain-file over-count is resolved, but X4 lineage and a matched
  terrain-process analysis remain necessary before quoting the terrain bracket.
- **Scheme-dependent diagnostics need scheme-aware reading.** CMP08 PBLH/TKE differ *by construction*
  between MYJ and YSU (C19); a raw PBLH difference map invites a wrong inference.
- **Context ≠ result.** The Trang/SIP and January-baseline exhibits (11 `context` rows in the manifest)
  are for Discussion framing only — different episode/config/identity; never rank February runs with them.
- **Combine before promoting.** Prefer GFS|NAM as two panels of *one* figure on the shared scale, and
  1-way−2-way as a difference panel, over four standalone plots. Push the rest to Supplement.

*Net:* CMP01--CMP05 remain the verified floor, not the figure cap.
CMP06--CMP11 should now be tested as candidate Results, while CMP12/CMP13 retain their
confounded/context limits.
