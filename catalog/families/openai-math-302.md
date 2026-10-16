---
id: openai-math-302
record_type: family
title: Compatible simplex slices and boundary restoration
source_family: '302'
source_collection: openai/math
batch_id: B083
subject: Operator algebras
source_paper_ids:
- P-000510
instrument_ids:
- MI-000766
- MI-000767
headline: The family claims filtered-product vanishing and boundary compression in complex cobordism,
  with a radius-of-comparison companion.
central_instrument: Distribute a simplex into slices with few nonvertex values; normalize nonzero slots
  while fixing every original boundary vector.
novelty_assessment: The finite mechanisms are separated from the headline claims. Exact priority of source-specific
  formulations is not established.
formalization_summary: No family scope is supplied in the inventory. No Lean verification is claimed.
statement_faithfulness: Simplex naturality is for monotone maps. Boundary restoration assumes a compact
  input, a uniform perturbation below one half and avoidance of sparse slot vectors.
dependencies: Interval intersection lengths, adjacent-block merging, order statistics of continuous functions
  and compactness.
antecedents: Classical cumulative-mass slicing and cutoff/radial normalization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Compatible simplex slices and boundary restoration

## Source manuscripts and claim

- [Filtered products and boundary-preserving compression in complex cobordism](../papers/P-000510.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Radius of comparison equals half the mean dimension](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026)

The family claims filtered-product vanishing and boundary compression in complex cobordism, with a radius-of-comparison companion.

## Extracted instruments

- [MI-000766: Slice a simplex naturally while limiting the number of nonvertex outputs](../instruments/MI-000766.md)
- [MI-000767: Restore whole cube-boundary slots after avoiding a sparse arrangement](../instruments/MI-000767.md)

## Dependencies and antecedents

Interval intersection lengths, adjacent-block merging, order statistics of continuous functions and compactness.

Classical cumulative-mass slicing and cutoff/radial normalization.

## Review and formalization scope

Read the complete simplex-slicing and boundary-restoration proofs and their notation. One companion is inventory-only. The compatible stable lift, nilpotence and stable avoidance arguments are not certified.

No family scope is supplied in the inventory. No Lean verification is claimed.

Simplex naturality is for monotone maps. Boundary restoration assumes a compact input, a uniform perturbation below one half and avoidance of sparse slot vectors.

[Batch record](../../batches/B083/README.md)
