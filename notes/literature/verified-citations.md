# Verified citations for the maximal working revision

Supporting analysis only; this file is excluded from the MDPI submission package.

Verified on the Akamai writing host on 14 July 2026 against the underlying publication, official product page, or local request path named below.

## 1. The 8 K cold-air-pool reference

### Exact source and passage

Neil P. Lareau, Erik Crosman, C. David Whiteman, John D. Horel, Sebastian W. Hoch, William O. J. Brown, Thomas W. Horst, and others, “The Persistent Cold-Air Pool Study,” *Bulletin of the American Meteorological Society* 94 (2013), 51–63, doi:10.1175/BAMS-D-11-00255.1.

The underlying PDF was checked at printed page 55, “Initial Findings—CAPs and air pollution,” and defines multiday episodes using “a deficit threshold of 8 K.”

The same passage defines that deficit from sounding potential temperature relative to potential temperature at 2500 m, the approximate crest height of the Salt Lake Valley's confining topography.

Figure 3 likewise labels deficit greater than 8 K as a strong cold-air pool.

### Decision for this manuscript

The 8 K value is not defensible as a literature reference value for Mountain Home minus Pariette Draw surface potential temperature.

Lareau et al. use a vertical, crest-relative sounding deficit in the Salt Lake Valley, whereas the proposed Uinta diagnostic is a horizontal contrast between two surface stations with different exposure and elevation.

The current draft already states that the two-site contrast is a spatial surface proxy rather than inversion strength, so plotting the PCAPS threshold beside it would undo that guardrail.

Recommended action at the next manuscript-edit stage: remove the 8 K reference line and caption claim.

If a contextual sentence is retained, the nearest defensible wording is: “PCAPS used an 8 K crest-relative sounding deficit as an operational threshold for strong Salt Lake Valley cold-air pools; that vertical diagnostic is not equivalent to the two-site surface contrast used here.”

Local verification route: `~/reviews/lareau-persistent-coldpool-bams-2013/lareau-bams-2013.pdf`, printed page 55, Figure 3 and “Initial Findings—CAPs and air pollution.”

## 2. Atmospheric heat-deficit method

### Original basin-volume formulation

C. David Whiteman, Xindi Bian, and Shiyuan Zhong, “Wintertime Evolution of the Temperature Inversion in the Colorado Plateau Basin,” *Journal of Applied Meteorology* 38 (1999), 1103–1117, doi:`10.1175/1520-0450(1999)038<1103:WEOTTI>2.0.CO;2`.

Section 6, printed pages 1111–1112, defines

\[
Q=c_p\int_0^h \rho(z)\,[\theta_h-\theta(z)]\,A(z)\,dz,
\]

where \(A(z)\) is the basin's horizontal area at height \(z\).

The authors describe \(Q\) as “the heat that must be added” to remove the inversion, and they divide it by the drainage area at inversion-top height to report joules per square metre.

Underlying source checked: author-hosted article PDF, §6 and equation (1), printed pages 1111–1112.

### Closest modern column formulation

Bianca Adler, Ming-Sung Yu, Jerome D. Fast, Jennifer D. M. Berg, and others, “Evaluation of a Cloudy Cold-Air Pool in the Columbia River Basin in Different Versions of the HRRR Model,” *Geoscientific Model Development* 16 (2023), 597–619, doi:10.5194/gmd-16-597-2023.

Section 3.3, printed page 605, defines the column proxy

\[
Q=c_p\int_{h_\mathrm{sfc}}^{h_\mathrm{ridge}}\rho(z)\,[\theta_{h_\mathrm{ridge}}-\theta(z)]\,dz
\]

and calls it a proxy for cold-pool strength while citing Whiteman et al. (1999).

Local verification route: `~/reviews/adler-cloudy-coldpool-2023/adler-gmd-2023.pdf`, §3.3, printed page 605.

### Fit to the present diagnostic

The present pressure-coordinate expression

\[
H={c_p\over g}\int \max\{\theta_\mathrm{crest}-\theta,0\}\,dp
\]

is the hydrostatic pressure-coordinate counterpart of Adler et al.'s column form.

Cell-area weighting over the analysis footprint then produces an area-normalized analogue of Whiteman et al.'s basin-volume heat deficit.

Both sources should be cited because Whiteman et al. establish the original physical interpretation and Adler et al. supply the closest column implementation.

The manuscript must disclose four departures: a fixed 2200 m crest, nonnegative clipping, a convex-hull analysis footprint rather than a hydrologic drainage area, and model-derived rather than observed profiles.

The quantity should be called an area-normalized atmospheric heat-deficit proxy, not a direct reproduction of either published diagnostic.

## 3. Model and input-product citations

### WRF 4.8.0

The general Version 4 technical reference is William C. Skamarock, Joseph B. Klemp, Jimy Dudhia, David O. Gill, Zhiquan Liu, Judith Berner, Wei Wang, Jordan G. Powers, Michael G. Duda, Dale M. Barker, and Xiang-Yu Huang, *A Description of the Advanced Research WRF Model Version 4*, NCAR Technical Note NCAR/TN-556+STR, doi:10.5065/1dfh-6p97.

That DOI identifies the Version 4 technical note, not release 4.8.0 specifically.

The exact software identity must therefore pair the technical-note citation with the official `v4.8.0` release page and archived tag or commit identifier.

The official release page records `v4.8.0`, released 8 June 2026, and identifies short commit `06d4240`.

Stable source: <https://github.com/wrf-model/WRF/releases/tag/v4.8.0>.

Citation guidance: cite Skamarock et al. for the model and record WRF `v4.8.0`, the release URL, the complete local source commit, compile options, and namelist fingerprint in the reproducibility record.

### GFS analysis `gfsanl_4`

The official NCEI product page identifies GFS Analysis grid 004 as the 0.5° analysis product with 00, 06, 12, and 18 UTC cycles and a +00 analysis hour.

Stable source: <https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast>.

No product-specific DOI was found on the official page.

Use a corporate dataset citation rather than inventing one: NOAA National Centers for Environmental Information and National Centers for Environmental Prediction, *Global Forecast System Analysis, grid 004 (0.5°)*, subset comprising the 2 February 2013 12 and 18 UTC +00 analyses, accessed 14 July 2026, with the official product URL.

The final reproducibility record must also give the local input-manifest filenames and SHA-256 values because the archive family alone does not identify the exact files used.

### NAM analysis `namanl_218`

The official NCEI product page identifies NAM Analysis grid 218 as the 12 km analysis product with four daily cycles and a +00 analysis hour.

Stable source: <https://www.ncei.noaa.gov/products/weather-climate-models/north-american-mesoscale>.

The NCEI metadata record identifies the archive as NCEI dataset identifier `gov.noaa.ncdc:C00630`, DSI 6173, rather than assigning a DOI.

Stable metadata: <https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc%3AC00630/html>.

Use a corporate dataset citation: NOAA National Centers for Environmental Information and National Centers for Environmental Prediction, *North American Mesoscale Forecast System Analysis, grid 218 (12 km)*, exact 2013 subset cycles from the input manifest, accessed 14 July 2026, with the official product and metadata URLs.

The exact cycle filenames and SHA-256 values remain required before the reference closes the provenance claim.

### Synoptic Data observations and `INV-17`

`verification/scripts/case_study_2013_obs.py` calls `brc_tools.obs.ObsSource`, whose inspected SynopticPy request supplies station identifiers, start, end, and variables but no explicit quality-control arguments.

The current Synoptic Timeseries documentation says omitted arguments default to quality control on, removal of flagged data on, flag return off, and only the `sl_range_check` check enabled.

Stable service documentation: <https://docs.synopticdata.com/services/time-series>.

This is an inference from the current wrapper and current API defaults, not proof of the settings applied when the frozen cache was generated, because the cache does not preserve the request URL or explicit quality-control parameters.

The frozen cache SHA-256 is `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64`.

Before submission, regenerate or independently archive the request with station list, UTC window, variable list, request URL, explicit quality-control arguments, response metadata, access date, and hash.

Use a corporate acknowledgement such as: “Observations for the named stations and networks were obtained through the Synoptic Data PBC Mesonet API.”

The Synoptic data disclaimer does not provide a blanket reusable-data license and says availability and reuse can depend on the contributing provider and agreement.

Stable policy routes: <https://synopticdata.com/data-disclaimer/> and <https://synopticdata.com/tcs>.

Station-network ownership and permission for redistribution of cached observations or derived tables must therefore be confirmed rather than inferred from API access.

`INV-17` remains partial: citation wording, current API defaults, access conditions, and cache identity are documented here, but the historical request, explicit quality-control state, and network-specific redistribution rights are not closed.
