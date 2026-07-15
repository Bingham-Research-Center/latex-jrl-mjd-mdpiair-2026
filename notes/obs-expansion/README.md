# obs-expansion staging — UNREGISTERED exploration evidence

Written 2026-07-15 by an exploratory session on the Akamai-side host (no CHPC
access). Lives only on the dead-end branch `jrl/ref-obs-expansion-2026-07`;
companion code on brc-tools branch `jrl/aqs-airdata-client`. **Nothing in
this directory is registered, gated, promoted, or referenced by any
manifest.** It exists so the verified findings in
`../obs-expansion-plan.md` are reproducible without re-running the network
pulls blind.

Contents:

- `probe_extra_vars_2013.py` — Synoptic availability probe for variables the
  committed `verification/scripts/select_proxies_2013.py` did not cover
  (wind_direction, dew point, RH, gusts, ceiling, weather codes, air_temp,
  altimeter). Run with the `brc-tools` conda env; loads the token from the
  legacy `[default]` section of `~/.config/SynopticPy/config.toml` in-process.
- `feasibility_pulls_2013.py` — end-to-end case-window pulls behind the plan's
  Synoptic feasibility verdicts (eval-station wind dir/moisture, METAR
  visibility + weather codes, solar radiation, SNOTEL snow). Writes the
  `probe_*.parquet` previews.
- `filter_aqs_ozone.py` — EPA AQS bulk-file filter that produced the ozone
  evidence tables. Superseded for future use by the reusable client
  `../../../brc-tools/brc_tools/api/aqs/` (`scripts/fetch_aqs_airdata.py`);
  kept as the record of what was actually run.
- `data-preview/*.parquet` — small filtered extracts (~230 KB total): AQS
  daily/hourly ozone and hourly PM2.5 for basin sites (Jan–Feb 2013, from EPA
  files with Last-Modified 2026-07-13), and the four Synoptic probe pulls
  (31 Jan–4 Feb 2013). Previews for inspection only — the promotion path is a
  fresh scripted pull under `verification/scripts/` with DATA-manifest rows,
  hashes, and provenance sidecars.

Promotion path and per-avenue actions: see `../obs-expansion-plan.md`.
