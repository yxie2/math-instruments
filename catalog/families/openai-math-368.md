---
id: openai-math-368
record_type: family
title: Preserving the target and composing at collapsed strata
source_family: '368'
source_collection: openai/math
batch_id: B086
subject: Partial differential equations
source_paper_ids:
- P-000526
instrument_ids:
- MI-000798
- MI-000799
headline: The family claims strong diffeomorphic approximation in three-dimensional Sobolev spaces.
central_instrument: Use a fine value tolerance and positive Jacobian to preserve the exact target; prove
  tangential derivative convergence on the parameter domain when ambient rank collapses.
novelty_assessment: Classical ingredients are distinguished from source-specific uses. Exact priority
  of the extracted formulations is not established.
formalization_summary: No family scope is supplied; no Lean verification is claimed.
statement_faithfulness: The target is bounded in the proper-degree argument. The composition lemma assumes
  finitely many closed C1 pieces and uniformly bounded parameter derivatives.
dependencies: Proper homotopy, degree, locality of weak derivatives and dominated convergence.
antecedents: Classical degree-one global inversion and piecewise smooth chain rules.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Preserving the target and composing at collapsed strata

## Source manuscripts and claim

- [Strong diffeomorphic approximation in three dimensions for 1≤p≤2](../papers/P-000526.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Strong diffeomorphic approximation in three dimensions for p>2](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026)

The family claims strong diffeomorphic approximation in three-dimensional Sobolev spaces.

## Extracted instruments

- [MI-000798: Keep the exact target by a boundary-distance tolerance and degree one](../instruments/MI-000798.md)
- [MI-000799: Pass derivatives through a finite-piece map when the parameter rank collapses](../instruments/MI-000799.md)

## Dependencies and antecedents

Proper homotopy, degree, locality of weak derivatives and dominated convergence.

Classical degree-one global inversion and piecewise smooth chain rules.

## Review and formalization scope

Read complete proper-degree, tangential-composition and local-tolerance proofs. One companion is inventory-only. The rank-sensitive approximation, topological replacements and global Sobolev construction are not certified.

No family scope is supplied; no Lean verification is claimed.

The target is bounded in the proper-degree argument. The composition lemma assumes finitely many closed C1 pieces and uniformly bounded parameter derivatives.

[Batch record](../../batches/B086/README.md)
