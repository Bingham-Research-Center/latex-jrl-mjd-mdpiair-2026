# pelican2013 — experiment & figure inventory

**AI-optimized index. Read this instead of `ls`-ing the archive.** It maps every
pelican2013 WRF experiment to a short code, states which publication figures exist and
*where*, lists the comparison figures, and gives the `/wrf-full-figures` commands to fill
any gap. The archive is ~30 GB of PNG + wrfout across many near-duplicate runs — do **not**
dredge it; use the exact paths below.

- **Archive root** (`ARC`): `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/`
  (all paths below are relative to `ARC`). Group storage, not a repo; no cross-machine paths.
- **Event:** Uinta Basin cold-air pool, init **2013-02-02**; main case 12→18 UTC hourly.
- **Authoritative figure defs:**
  `verification/config/figures/{pelican2013,pelican2013_1km,pelican2013_d04}.toml`.
  Figure engine: sibling `../brc-tools/docs/WRF-FIGURE-ENGINE.md`.
- **Run and narrative authority:** use `verification/provenance/run-inventory.csv`
  for run identity and `verification/provenance/comparison-inventory.csv` for what
  each comparison may support. This catalogue owns figure coverage and paths only.
- **Last verified:** 2026-07-10 after jobs `13896642`, `13896828`, and
  exact-config convergence `13896871`; counts/mtimes were checked and representative X10,
  direct-feedback, forcing-contrast, profile, heat-deficit, skew-T, section,
  surface, and upper-air images were opened.
- **Exact renderer state:** brc-tools `89883ceb52988182943d0fb3f9efd0b2dd835c10`;
  `verification/config/figures/pelican2013.toml` SHA-256
  `58e2b12749983f9525046919694c965624c8b2945aec84cc22caaf5dd1a8f06a`.
- **Never `cat`/open the PNGs to answer "does the set exist"** — count with
  `ls "$ARC/<full-figures-path>/<family>" | wc -l` (see Appendix).

The X-codes are a **provisional typing shorthand / lookup only** — not committed labels.
They can be remapped to hypothesis/weakness labels later by editing the one code column;
nothing else depends on them. **X0 = control** (best-estimate free-running config); the
rest are variations. Why X0 is X0 and why the MYJ run is a *treatment* not the control
is documented in
`verification/docs/pelican2013-pbl-scheme-justification.md`.

Physics is shared across all runs — Thompson(8)/RRTMG(4)/Noah(2), YSU PBL(1)+MM5 sfclay(1),
`cu=0`, 21-cat land — **except X2**, which swaps to MYJ(2)+Eta(2). A complete standard
per-run publication set = **63 PNG** (14 sections + 35 surface + 14 upperair, at 7 hourly
valid times 12–18Z).

## Table 1 — Experiment lookup + figure status

| X | archive dir (under `ARC/`) | ICs | nesting · inner dx | lev | terrain (GEOG) | physics Δ | window | `full-figures/` path (under the dir) | figs | newest | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **X0** | `pelican2013_nam_3_1_333m_75lev_oneway_terrain3s` | NAM | 1-way · 3dom/333 m | 75 | fine `terrain3s` (~90 m†) | baseline (YSU) | 6 h 12–18Z | `full6h/run_20260708T021809Z/full-figures` | ✓ 63 | 07-09 18:49 | **control**; physics-bridge pivot |
| X1 | `…_oneway_terrain3s_slope` | NAM | 1-way · 333 m | 75 | fine | +slope/shading rad | 6 h | `full6h/run_20260710T003606Z/full-figures` | ✓ 63 | 07-09 23:35 | X0 + `slope_rad=1,topo_shading=1` |
| X2 | `…_oneway_terrain3s_slope_myj` | NAM | 1-way · 333 m | 75 | fine | +**MYJ PBL/Eta** | 6 h | `full6h/run_20260710T003606Z/full-figures` | ✓ 63 | 07-10 01:45 | Tran-PBL **sensitivity** (treatment, not control); shares run-id w/ X1 but distinct dir |
| X3 | `pelican2013_nam_3_1_333m_75lev_oneway` | NAM | 1-way · 333 m | 75 | default ~900 m | baseline | 6 h | `full6h/run_20260702T053120Z/full-figures` | ✓ 63 | 07-09 23:34 | standard-terrain 1-way; ref leg of terrain diffs |
| X4 | `…_oneway_terrain5m` | NAM | 1-way · 333 m | 75 | 5-arcmin coarse (≈9 km) | baseline | 6 h | `full6h/run_20260707T182414Z/full-figures` | ✓ 63 | 07-09 18:58 | `terrain5m` = 5 arc-**min**, coarser than default |
| X5 | `pelican2013_nam_3_1_333m_75lev` | NAM | **2-way** · 333 m | 75 | default ~900 m | baseline | 6 h | `full6h/run_20260626T163737Z/full-figures` | ✓ 63 | 07-09 23:34 | feedback test vs X3 |
| X6 | `pelican2013_gfs_3_1_333m_75lev` | **GFS** | 2-way · 333 m | 75 | default ~900 m | baseline | 6 h | `full6h/run_20260630T181555Z/full-figures` | ✓ 63 | 07-09 23:34 | driving-state contrast vs X5; IC/LBC contributions unresolved |
| X7 | `pelican2013_nam_3_1km_75lev` | NAM | 2-way · 2dom/**1 km** | 75 | default | baseline | **24 h** 00→00Z | `full24h/run_20260625T212123Z/full-figures` | ✓ **216** (48/120/48) | 07-10 02:57 | coarse resolution rung; own `verification/config/figures/pelican2013_1km.toml` |
| X8 | `pelican2013_nam_d04_111m_50lev_oneway_terrain3s` | NAM | 1-way · **4dom/111 m** | 50 | fine | baseline | 6 h (d03/d04 sub-hrly) | `full6h/run_20260709T041225Z_d04only3s_ts12/full-figures` | ~86 **non-std** | 07-10 01:09 | fine rung; nested `nam_d04_111m/{sections28,surface35,upperair7}` + profiles7/skewt7/domains1/heatdeficit1; **upperair crest-only** (no p600); focus=**Vernal**; own `verification/config/figures/pelican2013_d04.toml` |
| X9 | `pelican2013_nam_3_1_333m_75lev_twoway_terrain3s` | NAM | **2-way** · 333 m | 75 | fine | baseline | 6 h | — | ✗ **none** | quicklooks 07-10 04:5x | **quicklooks only** at `full6h/run_20260710T084413Z/quicklooks`; **not a TOML `[runs]` key yet** — see Table 3 |
| X10 | `pelican2013_gfs_3_1_333m_75lev_oneway` | **GFS** | **1-way** · 333 m | 75 | default ~900 m | baseline | 6 h | `full6h/run_20260710T234000Z/full-figures` | ✓ 63 | 07-10 19:38 | feedback-only companion to X6; preparation `13894268`, WRF `13894282`, quicklooks `13896648` |

Legacy dirs `feb2013_basin_nam_12_4km`, `jan2013_basin_gefs`, `pelican2013_rap_3_1_333m_75lev`
are **out of scope** (no/near-zero publication figures) and intentionally omitted.

† **Terrain-label caveat:** `terrain3s` = 3 arc-**second** GEOG (~90 m) per
`verification/config/figures/pelican2013.toml`; the delivered source may be finer,
but that detail is not verified in the current run inventory. Reconcile it before
quoting another resolution. `terrain5m` = 5
arc-**minute** (~9 km, coarser than the default ~900 m).

## Table 2 — Comparison figures (cross-case, under `ARC/pelican2013_pub_figures/compare/`)

Each pair holds everything fixed except the named axis (`a − b`). Present-counts are
on-disk PNG at last verify. Note: `X0` is the manuscript *control* but is **not** the
reference leg of every pair — each pair names its own `a`/`b`.

| pair (a − b) | TOML tag | `compare/<dir>/` | axis isolated | sections? | PNG | note |
|---|---|---|---|---|---|---|
| X6 − X5 | `GFS-NAM` | `diff_gfs_nam` | driving analysis, two-way row | yes | 21 | GFS is warmer and less stable over the short window |
| X10 − X3 | `GFS-NAM-1way` | `diff_gfs_nam_oneway` | driving analysis, one-way row | yes | 21 | symmetric forcing contrast; same qualitative separation |
| X5 − X3 | `2way-1way` | `diff_feedback` | NAM nest feedback | yes | 21 | nearly null at basin core; vertical sections now included |
| X6 − X10 | `GFS-2way-1way` | `diff_feedback_gfs` | GFS nest feedback | yes | 21 | small spatial response relative to either forcing contrast |
| X3 − X4 | `terrain-900m-9km` | `diff_terrain` | terrain: default vs coarse | no | 7 | |
| X3 − X0 | `terrain-900m-90m` | `diff_terrain_fine` | terrain: default vs fine | yes | 42 | count > expected 21 — likely extra/stale; verify before use |
| X1 − X0 | `slope-shading-control` | `diff_slope_shading` | slope/shading radiation | no | 7 | Tran-bridge step 1 |
| X2 − X1 | `MYJ-Eta-slope` | `diff_myj_eta` | PBL scheme | yes | 21 | Tran-bridge step 2; coherent low-level response, with PBLH/TKE interpretation pending C19 |
| X0 − X4 | `terrain-3arcsec-5arcmin` | `diff_terrain_res` | terrain: fine vs coarse (**headline**) | yes | 21 | |

Also under `compare/`: `domains/` (1), `heatdeficit/` (1), `profiles/` (1, Horsepool 12Z),
`skewt/` (62 — focus Horsepool per case/time + stations KSLC/KGJT/KRIW at 12Z for gfs+nam).
The current `pelican2013` compare root contains 247 PNGs.
The 1-km rung has its own `pelican2013_1km_pub_figures/compare/` (domains/heatdeficit/
profiles 1 each, skewt 27). **No `[[differences]]` pair yet involves X8 (d04) or X9.**

## Table 3 — Recommended `/wrf-full-figures` runs to complete the set

Slash-command strings only (the skill maps them to the SLURM job; never invoke the
python/sbatch directly). Free-form NL args — name the case, run, and selection. Add
`--skip-existing` to keep completed figures. Status legend: 🔴 gap · 🟡 non-standard · 🟢 refresh-only.

| # | `/wrf-full-figures …` | fills / does | status | prerequisite |
|---|---|---|---|---|
| 1 | `/wrf-full-figures pelican2013, case nam_twoway_terrain3s, latest run, all figures` | X9 full 63-PNG set (2-way at control terrain) | 🔴 | **first** add a `[runs.nam_twoway_terrain3s]` entry (dir `pelican2013_nam_3_1_333m_75lev_twoway_terrain3s`) to `verification/config/figures/pelican2013.toml` — it is not a run key yet |
| 2 | `/wrf-full-figures pelican2013_d04 case, latest run, figures sections surface upperair` | X8 standardized surface/section/upperair (adds p600 advection; flattens the nested `nam_d04_111m/` layout) | 🟡 | uses `verification/config/figures/pelican2013_d04.toml`; focus = Vernal |
| 3 | `/wrf-full-figures pelican2013, all cases, compare figures only: difference skewt profiles heatdeficit domains, --skip-existing` | regenerate cross-case `compare/` after any run changes; also refreshes `diff_terrain_fine` (over-count) | 🟢 complete for X10 | jobs `13896642` and `13896828`; X9 remains outside the TOML |
| 4 | `/wrf-full-figures pelican2013, all cases, all figures, --skip-existing` | idempotent sweep — confirms the configured eight-case set complete | 🟢 complete | final exact-config convergence `13896871`: all 730 tasks skipped as up to date |
| — | *(optional science)* add `X9 − X0` feedback-at-fine-terrain diff pair to `verification/config/figures/pelican2013.toml`, then rerun #3 | cleaner feedback test than X5−X3 (matches the control's fine terrain) | 🟡 | your call — a new `[[differences]]` block |

The configured X0--X6 and X10 standard sets are **complete** at 63 PNGs each;
X7 retains its separate 216-PNG 24-hour set. X8 remains non-standard and X9
remains the only unrendered standard candidate.

## Appendix — navigation & completeness (for the agent)

**A standard per-run set = 63 PNG**, under `<full-figures-path>/`:
- `sections/` = 14 → `section_{ew,ns}_<case>_{12,13,14,15,16,17,18}z.png`
- `surface/` = 35 → `{theta2m,t2,wspd10,snow,pblh}_<case>_multidomain_{12..18}z.png`
- `upperair/` = 14 → `crest2200_<case>_{12..18}z.png` + `p600_advection_<case>_{12..18}z.png`

`<case>` = the TOML `[runs]` key (e.g. `gfs`, `nam`, `nam_terrain3s`). 24-h run X7 has 3×
the counts (24 valid times). Cross-case families live under `pelican2013_pub_figures/compare/`,
not under any single run. All PNG @ 300 DPI.

**Verify a set without opening images:**
```
ARC=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
ls "$ARC/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z/full-figures/surface" | wc -l   # expect 35
```

**Caveats:** station skew-Ts exist only at 12Z and only for gfs+nam. `--lead N` targets
forecast lead hours (overrides `--time`). `--skip-existing` = idempotent (missing ≠ error;
check the job `.out` for `[SKIP]`/`[WARN]`). X8's `full-figures/` uses a nested
`nam_d04_111m/` subtree and crest-only upperair — treat its counts separately from the 63
standard. `run_*` dirs above are the newest at verify time; if absent, `ls` the experiment's
`full6h/` (or `full24h/`) for the current `run_*`.
