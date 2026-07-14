# Matichuk et al. (2017) claim rows

Supporting analysis only; this file is excluded from the MDPI submission package.

Underlying source: Rebecca Matichuk et al., “Evaluation of the Community Multiscale Air Quality Model for Simulating Winter Ozone Formation in the Uinta Basin,” *Journal of Geophysical Research: Atmospheres* 122 (2017), 13545–13572, doi:10.1002/2017JD027057, citation key `Matichuk2017-bq`.

The local critique at `~/reviews/matichuk-cmaq-ub-2017/critique.md` was used only as a route, and each row below was checked against the underlying article section and printed page.

| Candidate claim | Underlying evidence | Required caveat | Safe use |
|---|---|---|---|
| Better simulated temperature structure did not reliably yield better ozone structure. | The §3.2 census covers 177 paired profiles; the article concludes on printed page 13569 that “improved temperature profiles rarely resulted in improved O3 profiles.” | This is a decoupling result within one WRF snow-albedo and heat-capacity perturbation, not evidence that meteorology is unimportant. | Introduction or Discussion guardrail against treating temperature skill as sufficient chemistry skill. |
| The tested emissions perturbations moved ozone more than the tested snow-only meteorological perturbation. | Sections 3.2–3.3, especially printed pages 13560–13564, show little ozone improvement from the snow case and much larger changes after the VOC scaling ladder. | The experiment samples one meteorological dimension and does not compare emissions against fog microphysics, nighttime mixing, PBL choice, or other meteorological errors. | Discussion only, phrased as a result of the tested ladder rather than a general ranking of error sources. |
| The national inventory likely understated oil-and-gas VOC emissions in direction, but the paper did not establish a final correction magnitude. | Section 3.3, printed page 13562, describes the Horsepool-derived factors as an indication of missing-emission magnitude rather than a final inventory correction. | Factors were tuned to ambient concentrations and therefore absorb warm-bias dilution, photolysis, deposition, and other model errors; Horsepool is not basin-wide validation. | Introduction context for inventory uncertainty, with no adoption of the scaling factors. |
| A warm WRF bias and overly deep daytime mixing could dilute modeled surface precursors and ozone. | Sections 3.1.3 and 4, printed pages 13559–13560 and 13569, connect the warm bias and excessive mixed-layer height to dilution. | The paper does not isolate how much low bias arises from mixing versus emissions, chemistry, photolysis, or deposition. | Discussion explanation for compensating-error risk, explicitly labeled as a competing pathway. |
| Nighttime ozone is sensitive to how deposition to snow is represented in this platform. | Section 3.4 and the conclusion, printed pages 13565–13569, show that eliminating ozone deposition prevents much of the modeled nighttime collapse. | The displayed final case also contains VOC and leaf-area-index changes, and deposition was not separated from excessive stability, titration, and nighttime-mixing error. | Discussion only as a platform-conditional sensitivity, not as a clean deposition attribution. |
| Basin-wide observations complicate a Horsepool-only emissions interpretation. | Sections 2.2 and 3.1 evaluate surface and profile observations across as many as 14 sites and find spatially varying NOx behavior. | Some variables and profile types are not available at every site, and the later scaling is still calibrated at Horsepool. | Introduction motivation for station-matched, basin-spanning evaluation. |
| WRF snow-albedo changes do not automatically alter the photolysis calculation seen by offline CMAQ. | Section 2.3.1 says CMAQ used its internal albedo tables and did not receive the tested WRF albedo change for photolysis. | The paper therefore cannot use its own snow case to quantify the photolysis-albedo pathway, even though its conclusion discusses that pathway. | Methods and Discussion warning to verify every WRF-to-chemistry coupling path. |

## Narrative boundary

The strongest reusable result is profiles-versus-ozone decoupling, because the paper reports the full profile census rather than a selected example.

The strongest reusable caveat is attribution-by-tuning: the VOC factors establish the direction of an inventory shortfall but cannot uniquely measure its magnitude or dominance.

Do not turn this source into a claim that emissions dominate all meteorological errors, that zero ozone deposition is physically correct, or that improved temperature profiles should not be pursued.
