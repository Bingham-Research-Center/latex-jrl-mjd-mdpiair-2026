# Observation-expansion plan: verified data avenues for episode context and new diagnostics

Status: exploratory boil-down, 2026-07-15, verified with real pulls that day
from the Akamai-side host (internet + Synoptic token; no CHPC access).
**This lives on the dead-end reference branch `jrl/ref-obs-expansion-2026-07`**
(based on `jrl/codex-v3-integration` @ 47682b3, the X8-review-supplement tip).
Companion code sits on the brc-tools branch **`jrl/aqs-airdata-client`**.
Neither branch is merged anywhere; return with
`git switch jrl/ref-obs-expansion-2026-07`, adopt by cherry-pick/merge or by
copying files, then delete the staging copies. Evidence extracts and probe
scripts: `notes/obs-expansion/` (unregistered — see its README).

**Integration protocol for the next session:** fetch/pull the working
branches first and re-read the current manuscript/figure-trim direction —
the X8 deficit-transport supplement (commits 1677a96/47682b3) postdates this
plan's drafting, so re-check which avenues still fit. Nothing here is
registered or gated. All new observations enter as registered candidates
under the normal admission path; none validates modeled vertical structure,
and the Synoptic-provenance rewrite gate (QC parameters, network ownership,
sensor metadata, request URL, reuse permission) applies to any new Synoptic
pull.

## 0 Execution and ownership split (terse)

Where things run:

| Locus | What must run there |
|---|---|
| **CHPC only** | anything touching raw wrfout/metgrid on scratch (A7 model profiles; any new model-side station re-reduction), the frozen DATA00 obs cache on scratch, and Slurm figure-engine jobs (`verification/slurm/pelican_figures.slurm`) |
| **Akamai or any internet host** | all external pulls — Synoptic archive (token), EPA AirData zips, IGRA2 soundings, USU Box workbook (browser), MODIS harvest. All verified from this host 2026-07-15. CHPC DTN/login nodes also work for these |
| **Doesn't matter** | analysis/plotting on small tracked CSVs/parquets (A1 panel build, A2/A3/A5/A6/A8, A4 if tracked reductions suffice), LaTeX |

Who owns what:

| Repo | Owns |
|---|---|
| `brc-tools` (branch `jrl/aqs-airdata-client`) | reusable retrieval + rendering code: **new** `brc_tools/api/aqs/` client + `scripts/fetch_aqs_airdata.py` CLI + walkthrough + tests; existing ObsSource/soundings/MODIS renderer |
| this repo | paper-specific truth: registered pull/plot scripts under `verification/scripts/`, DATA-manifest rows (record the AirData `*.meta.json` vintage), candidate figures, captions, gates, and this plan |

## 1 What was verified

### 1.1 Synoptic archive, basin bbox, 31 Jan–4 Feb 2013

| Stream | Real data in window | Case-day facts (2 Feb) |
|---|---|---|
| 10 m wind direction | all 11 eval stations (USU07 thin: n=3 in 14–18 UTC) + 50 stations basin-wide | floor/bench medians in the SE quadrant (QV4 140°, UUT01 159°, USU01/USU04 158°), Mountain Home 45°, Wells Draw 248°; all-station median speed 0.62 m s⁻¹ |
| Dew point / RH | all 11 eval stations (QV4 lacks moisture 14–18 UTC; QRS sparse) | already pulled by the DATA00 cache spec — unused in the manuscript |
| Visibility (METAR) | KVEL, K74V (Roosevelt), KPUC (Price) | KVEL 10 mi (31 Jan) → 1.5 mi (2 Feb) → ≤¼ mi (3 Feb); K74V ≤¼ mi on 2 Feb; **KPUC outside the basin held 10 mi throughout** |
| Present-weather codes | KVEL, K74V | Synoptic codes 31 = mist/ground fog (63 reports), 30 = freezing fog, 9 = fog, 6 = haze, 20 = light snow. UDOT sites (UTSTV/UTHLP/UTICS) emit a constant undocumented code 45 — unusable |
| Solar radiation | 25 stations incl. in-basin UUT01 | UUT01 daily max 632/521/528/466 W m⁻² (31 Jan–3 Feb) collapsing to 82 on 4 Feb → near-clear through the case day, cloud on 3–4 Feb. DIAU1 reads 791 W m⁻² — sensor-suspect, exclude |
| SNOTEL snow | 23 rim sites (depth + SWE) | SWE static across the episode (CWHU1 218→218 mm, MMTU1 224→226, KGCU1 133→135) while depth settles → no melt, no accumulation |
| Wind gust | 36 stations | available; marginal value inside a CAP — skip |
| Dense 2 m temperature | **78 stations** report in-window vs the 11 frozen | context/maps only; station pseudo-profiles stay rejected per the figure trim ledger |
| Ozone / PM2.5 | **0 stations return data** | POR metadata claims coverage (QRS/QV4) but pulls return nothing — confirmed dead for 2013 |

### 1.2 Ozone and PM2.5 (three working sources; Synoptic has none)

**EPA AQS AirData bulk files** (anonymous, quality-assured, citable;
`https://aqs.epa.gov/aqsweb/airdata/{hourly|daily}_44201_{year}.zip`).
Twelve monitors reported ozone through Jan–Feb 2013; identities verified
against the AQS site registry:

| Site | AQS ID | Operator | Role |
|---|---|---|---|
| Ouray | 49-047-2003 | Ute Indian Tribe | basin floor; + PM2.5 (88502) |
| Redwash | 49-047-2002 | Ute Indian Tribe | basin floor/bench; + PM2.5 |
| Myton | 49-013-7011 | Ute Indian Tribe | basin floor |
| Whiterocks | 49-047-7022 | Ute Indian Tribe | north bench |
| Roosevelt | 49-013-0002 | Utah DEQ | basin floor; + PM2.5 |
| Vernal | 49-047-1003 | Utah DEQ | basin floor |
| Dinosaur NM West | 49-047-1002 | NPS | east basin |
| Little Mountain | 49-047-0014 | USFS | north-rim control |
| Fruitland | 49-013-1001 | Utah DEQ | west-margin control |
| Rangely Golf Course | 08-103-0006 | NPS | CO side |
| Enefit (Dragon Rd) | 49-047-5632 | industry | 2013 flagged incomplete — **exclude** |

Episode MDA8 ramp (ppb, "Ozone 8-hour 2015" rows of the daily file):

| Site | 30 Jan | 1 Feb | **2 Feb** | 3 Feb | 5 Feb | 6 Feb |
|---|---|---|---|---|---|---|
| Ouray | 64 | 86 | **95** | 101 | 115 | 137 |
| Redwash | 48 | 74 | **81** | 82 | 98 | 91 |
| Roosevelt | 50 | 65 | **72** | 74 | 93 | 98 |
| Vernal | 46 | 49 | **65** | 68 | 89 | 87 |
| Little Mountain (rim) | 47 | 49 | **56** | 59 | 50 | 56 |

The 2 Feb case day is a measured basin-floor exceedance day mid-buildup, with
rim/outside sites flat — exactly the "quality-controlled observed ozone for
January–February 2013" panel the §3.1 rewrite gate requests. Hourly files add
diurnal structure (overnight titration minima 6–11 ppb at Vernal/Roosevelt on
the case morning; Ouray 56–100 ppb through the day; the 14–18 UTC WRF window
sits in the morning accumulation phase). **PM2.5**: hourly 88502 at
Roosevelt/Ouray/Redwash all winter; Roosevelt daily mean 6.6 → 21.7 → 32.5
µg m⁻³ over 31 Jan–3 Feb, corroborating the METAR haze/visibility collapse.

**USU BRC public Box downloads** (via
`https://www.usu.edu/binghamresearch/data-access.php`): workbook
`3-ALLSITESNov2012-Mar2013ozonedata_.xlsx` in the annual-winter-ozone folder
covers the **non-AQS study sites** (Horsepool, Seven Sisters, Pariette Draw,
Castle Peak). Box links are JavaScript-rendered — download by browser, record
the file hash manually. Acknowledgment-of-source condition; authors are BRC
members, so internal QC provenance is reachable (Seth).

**NOAA CSL UBWOS 2013 archive**
(`https://csl.noaa.gov/groups/csl7/measurements/2013ubwos/`): ICARTT 1-min
NO/NO₂/NOy/O₃ at Horsepool from 23 Jan 2013, PSD met + radiation from 1 Jan,
plus TOPAZ ozone lidar, HRDL Doppler lidar, and ozonesondes — the only true
in-basin **vertical** observations for this episode. **Data policy: contact
PIs before publication; co-authorship expected if the data are essential.**
For episode context, prefer AQS + the USU workbook and cite the NOAA vertical
assets as next-experiment material.

Utah DEQ's archive is PDF summaries only. Network/QA provenance citation:
Stoeckenius & McNally (2014), *Final Report: 2013 Uinta Basin Winter Ozone
Study*, stable at
`https://www.usu.edu/binghamresearch/files/reports/UBOS_2013_Final_Report_-_PDF.zip`.

### 1.3 Radiosondes

`brc-tools` `fetch_soundings.py` works for the case: KSLC 12:00 UTC 2 Feb 2013
returned 86 levels via IGRA2 after installing the missing declared dependency
`siphon` (now present locally, 0.10.0). First fetch per station downloads the
full period-of-record (~minutes); batch on a DTN node per the script header.

## 2 Actionable avenues, ranked

Effort: S ≈ under an hour, M ≈ half-day, L ≈ multi-day/CHPC-bound.

### A1 — Ozone episode-context panel (standing §3.1 rewrite gate) — M
The MODIS snow panel's companion. Daily MDA8 (ppb) for Jan–Feb 2013 at
Ouray/Redwash/Roosevelt/Vernal (+ optional Horsepool from the USU workbook,
+ Little Mountain as the flat rim control), 2 Feb marked, ~70 ppb reference
line optional.
- Pull: `python ../brc-tools/scripts/fetch_aqs_airdata.py --param ozone
  --kind daily --years 2013 --basin --start 2013-01-01 --end 2013-02-28
  --out <scratch>/aqs_ozone_daily_janfeb2013.parquet` (add `--years 2012` +
  December window if the panel should open in December).
- Promotion path: new `verification/scripts/` pull+plot scripts; DATA rows for
  the parquet (record the AirData `*.meta.json` vintage sidecar); registered
  candidate; caption per the spec in
  `manuscript-v3-structure-and-domain-review.md` (site IDs, operators, units,
  standard, averaging rule, missingness, access provenance; "context, not
  validation of modeled vertical structure").
- The gate text's "reconcile Horsepool/UBWOS and AQS coverage" step is now
  concretely: AQS for regulatory/tribal sites; USU workbook for Horsepool;
  NOAA ICARTT only if 1-min resolution is wanted (policy).

### A2 — Fog/haze corroboration on the observed-context figure — S
Shade fog/mist/freezing-fog hours (KVEL/K74V METAR codes + visibility) onto
`fig:v3-observed`'s time axis, or a one-sentence "(not shown)": *"Visibility
at Vernal and Roosevelt fell from 10 mi to ≤¼ mi with mist, freezing-fog, and
haze reports on 2–3 February, while Price, outside the basin, held 10 mi
(not shown)."* Only AQ-adjacent observation Synoptic has for 2013; pairs with
the PM2.5 ramp (A8). Pull is in `notes/obs-expansion/feasibility_pulls_2013.py`
(wx section); UDOT code-45 sites excluded.

### A3 — Moisture context from the frozen cache variables — S
Dew point/RH are in the DATA00 cache spec but unused. Either a second panel on
`fig:v3-observed` (same four sites) or a "(not shown)" sentence on
near-saturation of the basin floor; links to ice-fog literature (Neemann) and
the fog evidence in A2. No new pull needed on CHPC (cache) or re-pull locally.

### A4 — Wind-direction diagnostic vs the four runs, 14–18 UTC — M
Observed 10 m vectors at the eval stations against X6/X5/X10/X3 (earth-relative
model wind is derived in the tracked DATA04–06/DATA14 reductions — **check
whether components or only speeds were stored**; if only speeds, the model
side needs a CHPC re-reduction from the raw runs, otherwise this runs
anywhere). Question: does the faster GFS transport wind also rotate the flow
(synoptic intrusion vs down-basin drainage)? Registered diagnostic or scoped
"(not shown)". Handle calms (0° codes) and drop USU07 (n=3), QRS (n=5); note
directions are noisy at 0.6 m s⁻¹ speeds.

### A5 — Solar clear-sky context sentence — S
*"Daily-maximum downwelling shortwave at in-basin stations on 2 February
reached values consistent with near-clear skies, collapsing on 4 February
(not shown)"* — supports photochemistry context, MODIS granule choice, and the
radiation discussion around the CMP07 screen. Exclude DIAU1.

### A6 — SNOTEL snow-stability sentence — S
*"SWE at the 23 rim SNOTEL sites was unchanged through the episode (depth
settling only), indicating neither accumulation nor melt (not shown)"* —
complements the MODIS spatial panel with temporal stability; later doubles as
a sanity check on the WRF snow-field initialization the Methods rewrite gate
asks to recover.

### A7 — Driving-analysis sounding check (declared new question) — M/L
Compare NAM- and GFS-derived initial profiles against the 12:00 UTC 2 Feb
KSLC/KGJT (and KRIW/KDPG) RAOBs — outside the basin, at initialization. This
is the check whose absence the Tran-2018 critique (C5) faults ("(not shown)"
NAM bias); supplement/reviewer-reserve figure or a scoped sentence. Needs
CHPC-side metgrid/wrfout profiles; the triage note allows skew-T material only
under a newly declared question — this is that question. Does not validate
in-basin structure; say so.

### A8 — PM2.5 companion to A1 — S
`--param pm25_nonfrm` hourly at Roosevelt/Ouray/Redwash; optional second axis
or a sentence tying the aerosol ramp to A2's haze. Preview parquet staged.

**Explicit non-actions:** station pseudo-profiles remain rejected (trim
ledger); Enefit site excluded; UDOT weather-code sites unusable for weather
typing; no NOAA CSL data in the manuscript without the PI-contact step.

## 3 New-session integration checklist

1. Fetch/pull the working branches of this repo and `../brc-tools`; check the
   figure-trim ledger, `rewrite/`, and the X8 supplement for direction changes
   that moot any avenue.
2. Adopt from the parked branches: merge/cherry-pick
   `jrl/ref-obs-expansion-2026-07` (this repo) and `jrl/aqs-airdata-client`
   (brc-tools), or copy files. Run `pytest tests/test_aqs_client.py` in
   brc-tools (6 offline tests; passing as written). Hand-add the aqs
   walkthrough to brc-tools' doc index/API reference (deliberately not edited
   from the exploratory session).
3. Decide A1 site set and window (Dec–Feb vs Jan–Feb); run the A1 pull; build
   the panel; register alongside the MODIS candidate.
4. Fold A2/A3/A5/A6 sentences (or the fig:v3-observed panel extension) into
   §3.1 with their pulls re-run under `verification/scripts/` + DATA rows.
5. Extend `verification/scripts/select_proxies_2013.py`'s candidate list with
   the newly probed variables and re-commit the availability CSV (evidence
   currently only in `notes/obs-expansion/`).
6. Schedule A4 and A7 as registered diagnostics when CHPC model columns are at
   hand.
7. Migrate anything adopted out of `notes/obs-expansion/` into the governed
   locations, then delete the staging copies.

## 4 Environment and provenance notes

- **SynopticPy token**: `~/.config/SynopticPy/config.toml` uses the legacy
  `[default]` layout; the installed synopticpy (≥2025) reads only a top-level
  `token = "..."` or `SYNOPTIC_TOKEN`. Fix by adding a top-level `token` line
  (keep `[default]` for old tools) or exporting the env var; the staged probe
  scripts load it in-process as a workaround. Never print it — Synoptic echoes
  the token in failed-request URLs.
- **siphon 0.10.0** installed into the local `brc-tools` conda env
  (`~/.conda/envs/brc-tools`) — it is a declared dependency that was missing.
- **EPA AirData vintage**: bulk files are regenerated by EPA (downloads used
  here: Last-Modified 2026-07-13). The brc-tools client writes a `*.meta.json`
  sidecar per zip; record it in any DATA row.
- The original bulk zips live in an **ephemeral** session job directory and
  will disappear; re-download via the client (URLs are stable), or re-derive
  everything from the commands in this note.

## 5 File inventory (parked on dead-end branches; no pre-existing tracked file was modified)

On `../brc-tools` branch `jrl/aqs-airdata-client` (from 2c79fc7):
- `brc_tools/api/aqs/__init__.py`, `brc_tools/api/aqs/client.py` — EPA AirData
  client: `download_airdata` (cache + provenance sidecar), `load_airdata`
  (site/bbox/date filters, hourly `valid_time` UTC), `UINTA_BASIN_SITES`
  verified registry, `PARAMS` map. Style mirrors `api/soundings`.
- `scripts/fetch_aqs_airdata.py` — CLI with `--basin` registry shortcut.
- `docs/walkthroughs/aqs.md` — walkthrough (index/API-reference links to be
  added by hand at adoption, to avoid editing tracked files from this session).
- `tests/test_aqs_client.py` — 6 offline tests, passing.

On this repo's branch `jrl/ref-obs-expansion-2026-07` (from 47682b3):
- `notes/obs-expansion-plan.md` — this note.
- `notes/obs-expansion/` — probe/exploration scripts + `data-preview/`
  parquets (~230 KB) + README with promotion path.
