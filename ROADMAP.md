# Manuscript roadmap

Current phase: **reconcile the experiment inventory before promoting results**.

The paper's durable claim is that credible cold-pool meteorology is a prerequisite for interpreting winter-ozone chemistry.
It must not claim that chemistry, emissions, deposition, or photolysis are already settled.

## Candidate large-scale narratives

| Narrative | Role if supported | Evidence already present | Gate before promotion |
|---|---|---|---|
| Initial and boundary conditions affect a short cold-pool forecast | Leading candidate | GFS two-way and NAM two-way touchstones | Reconcile as-run namelists; use one domain, station set, and valid window; quantify uncertainty. |
| Domain design and nest feedback affect the structure seen by a chemistry grid | Secondary candidate | NAM one-way/two-way pair; d02/d03 coverage contrast | Prove the pair isolates feedback; distinguish grid resolution from station-coverage artifacts. |
| Stable-layer, surface, snow, terrain, or cloud choices control cold-pool persistence | Experiment-led candidate | Several local run families and literature sensitivities | Inventory must yield controlled pairs; do not infer a physics sensitivity from unrelated configurations. |
| Nudging can correct or manufacture cold-pool structure | Context or result, depending on recovered runs | Tran critique, SIP-era comparator, January historical evaluation | A same-case controlled nudged/free pair and held-out verification are required for a result. |
| Meteorological error changes the volume available for ozone chemistry | Air-focused bridge | Consistent literature rationale | Phrase as an implication of evaluated structure, not proof that meteorology dominates inventory or mechanism error. |

The preferred paper is a compact original-research article led by the first two narratives.
The third and fourth narratives enter Results only if the inventory exposes defensible controls; otherwise they remain Discussion and future work.

## Phases and exit gates

| Phase | Outcome | Exit gate |
|---|---|---|
| 0. Repository foundation | Current MDPI template, sparse manuscript, evidence gates, safe submission builder | Complete in commits `3e21a28`--`e84c751`. |
| 1. Inventory reconciliation | Stable run IDs and fingerprints for every candidate comparison | `verification/provenance/run-inventory.csv` contains exact archive path, version, window, grid, physics, forcing, feedback, FDDA, and evidence hashes for each promoted run. |
| 2. Experiment design freeze | A short matrix of controlled comparisons and preregistered diagnostics/falsifiers | Each row isolates a named lever or lists every confound; common domain/stations/window selected. |
| 3. Evidence longlist | Recomputed statistics and diagnostic figures from provenance-checked real data | Commands are reproducible; uncertainty and missingness are explicit; synthetic output is absent. |
| 4. Narrative freeze | One primary result arc, one or two secondary arcs, and a limitations spine | Every paragraph-level claim is linked to a ledger row and a table/figure or cited source. |
| 5. Manuscript build | Methods, Results, Discussion, abstract, and required MDPI back matter | Coauthors confirm configuration, interpretation, roles, funding, data availability, and attribution. |
| 6. Figure and reproducibility freeze | Promoted figures, supplement/reviewer reserve, and public data/code plan | Both manifests are complete; canonical WRF styling reviewed; clean source ZIP compiles independently. |
| 7. Coauthor review and submission | Reviewed MDPI Air package | Michael reviews provenance/diagnostics; Loknath and Seth review chemistry framing; all authors approve. |

## Workstreams

### Run and data truth

- Reconcile the July 9 CHPC inventory archive with the canonical run-inventory CSV.
- Fingerprint the three JRL touchstones first, then the SIP-era comparator and any controlled sensitivity pairs.
- Preserve the January nudged evaluation as historical context unless a same-case design makes it relevant.

### Analysis and verification

- Freeze the 2 February 2013 evaluation window, station sample, domain, and spin-up rule before recomputing tables.
- Add uncertainty suitable for autocorrelated short time series; retain circular treatment for wind direction.
- Use independent or held-out observations for any nudging claim.

### Literature and argument

- Use critiques before extracted papers; use extracted sections before PDFs.
- Carry the Matichuk/Ahmadov warning that tuning emissions can absorb meteorology, photolysis, and deposition errors.
- Carry the Neemann/Tran warning that on/off experiments, nudging labels, PBL diagnostics, and chemistry-grid mismatches can hide confounding.
- Use `notes/literature-synthesis-register.md` to carry the three synthesis collections' shared challenge to any claim that meteorology is uniquely dominant.

### Figures and reviewer reserve

- Generate a broad diagnostic longlist on CHPC, then promote only figures that answer a named hypothesis.
- Keep useful rejected or secondary diagnostics reproducible for supplements and reviewer requests.
- Do not promote an inherited image solely because it looks publication-ready.

## Current decision point

The next irreversible decision is the experiment matrix, not prose or figure order.
John's CHPC inventory should first answer which controlled pairs exist; the manuscript shape follows that evidence.

The active granular queue is in `tasks/microtasks.md`.
The source-mining order and legacy to-do location are in `notes/resource-map.md`.
