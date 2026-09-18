# PDF harvest workflow across Akamai and CHPC

Use this route for one paper or report at a time.
The PDF is read once on Akamai; CHPC receives only questions that require local run,
configuration, or output evidence.

## Host authority

| Host | Owns | Must not infer |
|---|---|---|
| Akamai | Bibliographic identity, full-text reading, page/section routes, short verified passages, claim/evidence/caveat synthesis, manuscript wording, citation need. | WRF run identity or archive contents from names and narrative resemblance. |
| CHPC | Exact run/configuration/output matches, archive paths, machine fingerprints, commands, hashes, and match verdicts. | What the paper says from a second-hand summary or filename alone. |

Literature evidence and run evidence remain separate until both records support a join.

## One-paper sequence

1. John gives Codex the local PDF path or exact title on Akamai and the reason it matters.
2. Codex copies `notes/literature/harvest/TEMPLATE.md` to
   `notes/literature/harvest/<author-year-short-title>.md` and fills the Akamai record.
3. Codex paraphrases the argument, records page and section locators, and uses only short
   passages needed to verify disputed wording.
4. If the paper creates a run/configuration question, Codex copies
   `verification/provenance/pdf-followups/TEMPLATE.md` to the matching slug and writes a
   bounded CHPC request.
5. Commit and push the Akamai packet before changing hosts.
6. On CHPC, pull the commit, answer only the fingerprint questions, commit the small
   response record, and push before returning to Akamai.
7. On Akamai, pull the response and update the claim ledger, manuscript, or bibliography
   checklist only after the literature and machine evidence agree.

Use a push/pull baton when both hosts touch the same branch.
If work must overlap, use host-named branches and host-owned packet files, then merge on
Akamai.

## Akamai harvest standard

Each packet records:

- exact reference and stable identifier;
- local PDF path, access route, and bibliographic uncertainty;
- the manuscript question being tested;
- page, section, table, or figure locators;
- claim, evidence, caveat, and nearest defensible wording;
- design classification: controlled, configuration-controlled, cumulative,
  heterogeneous, or context only;
- contradictions with current prose;
- any exact strings or fingerprints CHPC should search;
- manuscript action: use, qualify, reserve, drop, or unresolved;
- small-bibliography status: needed now, later only if cited, or not needed.

Do not bulk-extract a PDF into Git, reproduce long passages, or treat a critique as the
underlying source.

## CHPC follow-up standard

The response records exact run IDs and comparison IDs; `TITLE`, `P_TOP`, `ZNW`, dates,
domain geometry, FDDA coefficients, `OBS_DOMAIN*`, namelist hashes, and other relevant
machine fingerprints; archive paths; commands; output hashes; and one verdict:
`proven`, `likely but unproved`, `not found`, or `not comparable`.

Keep raw WRF, observations, and bulk output off Git.
Return compact metadata and derived evidence only.

## Stop rules

- No manuscript claim from an unread or unlocated passage.
- No run-to-publication join from labels alone.
- No citation key until John's small Paperpile export supplies it.
- No second host task if Akamai can answer the question from literature alone.
- No new WRF integration unless the existing archive cannot answer a selected question.
