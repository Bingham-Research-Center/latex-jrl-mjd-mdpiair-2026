# GFS/NAM by Nest-Feedback Factorial — 10 July 2026

**Coverage refresh, 13 July 2026.** The factorial design and five-hour analysis below
remain current.
The 247-PNG comparison count was the 10 July checkpoint; the authoritative archive
inventory now records 324 comparison PNGs after X9/X9-minus-X0 rendering,
`heatdeficit_map` production, and removal of 21 stale terrain-label duplicates.

## Design

| Study ID | Driving analysis | Feedback | Exact archive |
|---|---|---|---|
| X6 | GFS | two-way | `pelican2013_gfs_3_1_333m_75lev/full6h/run_20260630T181555Z` |
| X10 | GFS | one-way | `pelican2013_gfs_3_1_333m_75lev_oneway/full6h/run_20260710T234000Z` |
| X5 | NAM | two-way | `pelican2013_nam_3_1_333m_75lev/full6h/run_20260626T163737Z` |
| X3 | NAM | one-way | `pelican2013_nam_3_1_333m_75lev_oneway/full6h/run_20260702T053120Z` |

All paths are below `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/`.
Within each forcing family, the normalized as-run namelists differ only in
`domains.feedback`. X10 reused X6's six verified GFS `met_em` inputs, so it is a
new `real.exe`/`wrf.exe` integration but not a new GFS download or WPS run.

## Execution and Provenance

- X10 preparation: Slurm `13894268`.
- X10 WRF: Slurm `13894282`, `0:0`; `real.exe` 32 s, `wrf.exe` 5865 s; 21 hourly files; empty error scan.
- X10 quicklooks: Slurm `13896648`, `0:0`; 54 PNGs.
- Four-run manuscript analysis: Slurm `13896641`, `0:0`; exact metadata in `../provenance/retention-analysis-13896641.json`.
- X10 WRF record: `../provenance/gfs-oneway-wrf-13894282.json`.
- Full figures: Slurm `13896642` and `13896828`, both `0:0`.
- Final exact-config convergence: Slurm `13896871`, `0:0`; all 730 configured tasks skipped as up to date.
- Renderer: `brc-tools` commit `89883ceb52988182943d0fb3f9efd0b2dd835c10`.
- Study TOML SHA-256: `58e2b12749983f9525046919694c965624c8b2945aec84cc22caaf5dd1a8f06a`.

The named `wrf-full-figures` skill was not installed in this session. The same
maintained workflow was run directly through the documented `brc-tools` engine,
`verification/config/figures/pelican2013.toml`, and
`verification/slurm/pelican_figures.slurm`.

## Figure Inventory and Visual Review

- X10 standard set: 63 PNGs = 14 sections + 35 surface + 14 upper-air.
- Cross-case compare root: 247 PNGs at this 10 July checkpoint; 324 PNGs in the current
  archive record.
- Direct 21-panel families exist for X6-X5, X10-X3, X5-X3, and X6-X10.
- Representative X10 surface, EW section, crest-level, and skew-T products were opened.
- Representative GFS feedback and one-way GFS-NAM surface/section differences were opened.
- Refreshed Horsepool profile and heat-deficit products were opened.
- No blank, truncated, mislabeled, or unit-broken representative panel was found.

## Frozen Five-Hour Result

On d02 from 14--18 UTC, GFS-minus-NAM 50--500 m AGL stability is `-3.63 K`
under two-way feedback and `-3.65 K` under one-way feedback. Transport wind is
`+0.79` and `+0.99 m s-1`, respectively. All four descriptive two-hour block
intervals exclude zero and every hourly spatial median retains its sign.

One-way minus two-way stability and transport wind are `+0.002 K` and
`+0.006 m s-1` for NAM, versus `-0.066 K` and `+0.104 m s-1` for GFS. The
station/hour-paired interaction is `-0.103 K` and `+0.097 m s-1`. The feedback
response is therefore source conditioned but much smaller than the forcing
contrast over this sample. These are descriptive short-window effects, not a
general nesting-equivalence claim or formal confidence statement.
