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
| 6 | **Feedback at FINE terrain (X9−X0)** | CMP06 | **nothing** — X9 has quicklooks only, no full-figures, not a TOML run key | none | **whole run** | ⬛ **highest-value gap** — cleaner feedback test than CMP03 (matches control terrain) |
| 7 | **Slope/shading radiation (X1−X0)** | CMP07 | `CMP/diff_slope_shading/` (7, surface only) | engine | native **missing**; sections **missing** | 🟨 discussion; ⬛ render if promoted |
| 8 | **PBL/sfclay scheme MYJ-Eta vs YSU-MM5 (X2−X1)** | CMP08 | `CMP/diff_myj_eta/` (21) | engine | native **missing** | 🟨 discussion — ⚠ PBLH is scheme-dependent (C19); needs AGL/TKE-aware recompute before any claim |
| 9 | **Terrain source: default vs fine 3-arcsec (X3−X0)** | CMP09 | `CMP/diff_terrain_fine/` (**42 — over-count, likely stale**) | engine | native **missing**; data-quality flag | 🟨 discussion — verify/​clean the over-count first |
| 10 | **Terrain source: default vs coarse 5-arcmin (X3−X4)** | CMP10 | `CMP/diff_terrain/` (7) | engine | native **missing** | 🟨 discussion — ⚠ X4 archive-name provenance caveat |
| 11 | **Terrain source: fine vs coarse, widest bracket (X0−X4)** | CMP11 | `CMP/diff_terrain_res/` (21, "headline") | engine | native **missing** | 🟨 discussion/supplement — ⚠ resolve X4 provenance |
| 12 | **Resolution ladder 1 km / 333 m / 111 m (X7/X0/X8)** | CMP12 | — (no valid difference) | none | — | 🟥 **do NOT plot as a resolution difference** — confounded by init time, forecast age, domain count, levels, cadence. Exhibit = the confound table + a 3-panel *domains/terrain* figure labelled "not controlled" |
| 13 | **Driving heritage / SIP nudged reference** | CMP13 | `wrf_xsect_theta_trang_ref`, `…_trang_anlnudge_jan17`, time-heights | native (context) | identity unresolved | 🟨 discussion-only — label "un-nudged SIP-era, config after Tran 2018", never "the Tran 2018 run" |

**Coverage tally:** 13 decisions — **2** paper-grade (CMP01, CMP03), **2** paper-grade-but-native-spatial-diff-missing (CMP02, CMP04), **5** engine-only needing a native render (CMP07–11), **1** whole-run gap (CMP06), **1** confounded/do-not-plot (CMP12), **1** context-only (CMP13), plus the 4-run retention that serves CMP01–05.

---

## §2 Per-experiment figure completeness (X0–X10)

| X | run | full-figure set (63) | manuscript-native candidates | keep/drop for paper |
|---|---|---|---|---|
| X0 | NAM 1-way fine-terrain **control** | ✓ | θ x-sect/time-height (native); transect locator | 🟩 control + **Fig 1** (domain) |
| X1 | +slope/shading | ✓ | — (engine diff only) | 🟨 discussion |
| X2 | +MYJ/Eta | ✓ | — (engine diff only) | 🟨 discussion (C19 caveat) |
| X3 | NAM 1-way default | ✓ | native x-sect/time-height + upper/t2/dtheta diffs | 🟩 primary (one-way NAM leg) |
| X4 | NAM 1-way coarse terrain | ✓ | — | 🟨 discussion (provenance caveat) |
| X5 | NAM 2-way default | ✓ | native x-sect/time-height + diffs | 🟩 primary |
| X6 | GFS 2-way default | ✓ | native x-sect/time-height + diffs | 🟩 primary |
| X7 | NAM 2-way **1 km 24 h** | ✓ (216) | — | 🟥 confounded resolution rung — context only |
| X8 | NAM 1-way **111 m 50-lev** | ~86 non-standard | — | ⬛/🟥 fine rung; standardize before use; resolution claim confounded |
| X9 | NAM 2-way fine-terrain | ✗ quicklooks only | — | ⬛ **render** — unlocks CMP06 |
| X10 | GFS 1-way default | ✓ | `wrf_retention` (4-run) | 🟩 primary (one-way GFS leg) |

---

## §3 Gaps to plot — prioritized (the "not yet plotted, and important" set)

1. **⬛ X9 full-figure set + X9−X0 difference (CMP06).** The only *controlled* feedback test at the
   control's own fine terrain. Prereq: add a `[runs.nam_twoway_terrain3s]` key to
   `verification/config/figures/pelican2013.toml`, then `/wrf-full-figures pelican2013, case
   nam_twoway_terrain3s, latest run, all figures`, and add an `X9−X0` `[[differences]]` block.
2. **⬛ Native θ *difference* cross-sections + time-heights.** `plot_wrf_cross_sections.py` now takes a
   fixed θ scale but still plots one run at a time. Add a two-run **difference** mode (GFS−NAM,
   1-way−2-way) — the inventory's prescribed "GFS−NAM difference" exhibit that no native figure yet
   provides. One code change unlocks CMP01/02/03/04 native vertical diffs.
3. **⬛ Native spatial diffs for CMP02 & CMP04** (X10−X3, X6−X10) to match the CMP01/CMP03 upper-air set.
4. **🟦 Common-AGL / low-layer zoom** of the x-sections (the 4500 m ceiling compresses the pool);
   a 0–1000 m AGL companion reads the inversion far better.
5. **🟨 One native exhibit each for CMP07–CMP11** *only if* that lever is promoted from discussion —
   don't pre-render all five at manuscript quality.

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
- **Provenance gates a figure, not polish.** X4 (terrain5m) carries an archive-name discrepancy and
  `diff_terrain_fine` is an unexplained 42-vs-21 over-count — resolve both before either terrain
  lever is quoted, however good the picture looks.
- **Scheme-dependent diagnostics need scheme-aware reading.** CMP08 PBLH/TKE differ *by construction*
  between MYJ and YSU (C19); a raw PBLH difference map invites a wrong inference.
- **Context ≠ result.** The Trang/SIP and January-baseline exhibits (11 `context` rows in the manifest)
  are for Discussion framing only — different episode/config/identity; never rank February runs with them.
- **Combine before promoting.** Prefer GFS|NAM as two panels of *one* figure on the shared scale, and
  1-way−2-way as a difference panel, over four standalone plots. Push the rest to Supplement.

*Net:* the frozen paper stays at the CMP01/CMP03 core (+retention, +domain Fig 1). Everything
below that line is a team-discussion exhibit or reviewer reserve, catalogued here so a "why didn't
you test X?" question has a picture to point at — not a mandate to grow the paper.
