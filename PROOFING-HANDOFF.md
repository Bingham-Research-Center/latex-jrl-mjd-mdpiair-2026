# Proof return: closed 11 October 2026

John confirmed submission of the corrected proof to MDPI after reviewing the current PDF. Codex did not submit to the journal or upload a preprint. There is no active proof-return task; wait for the next publisher communication.

| Checkpoint | Location |
| --- | --- |
| Immutable submitted-source commit | `f06ee3d`, tag `mdpi-air-proof-return-2026-10-11` |
| Working source | `proof-package/working/air-4472509-done.tex` on `jrl/proofs-round1` |
| Original publisher bundle | `proof-package/air-4472509-english/`, unchanged |
| Query history and replies | `notes/proof-query-catalogue.md`, `PROOFER-REPLY-TABLE.md`, `PROOFER-RETURN-REPLIES.md` |
| Local review PDF | `proof-package/working/air-4472509-done.pdf` (ignored by Git) |
| Local source/PDF ZIP | `dist/air-4472509-proof-return-author-pass-20261011.zip` (ignored by Git) |

The tagged TeX SHA-256 is `3dec02cd7aad5da9411977403d4f7b3738d8ba87da096c993a1496447fb4b55e`. The reviewed 18-page PDF SHA-256 is `ba90154edd0745f705f05a19f4805eea01f3b9605507fed793122aeb9320d909`; ZIP SHA-256 is `4ec9052502a2bc893d01c41ad836010b9c9be779a8323c994e5685a02e10d72b`. All 26 ZIP members matched the working files at closeout. Keep the journal receipt outside Git.

The repository is public. Default `main` is an older snapshot with a route to this proof branch; `main.tex` and `submission-package/` were not made into the submitted proof. The first-round review branch remains available for its evidence and commit history. The submitted proof source is recoverable from the tag even if work continues on this branch.

When a new proof arrives: record the receipt, preserve its files unchanged, create a new `jrl/<topic>` branch/worktree from this checkpoint, compare source and publisher notes, then handle questions in small author-approved batches. Rebuild and inspect the PDF before any return. Use [AGENTS.md](AGENTS.md) for the short route and evidence rules.
