---
id: openai-math-167
record_type: family
title: Distinct-pair cancellation and predictions from fresh tests
source_family: '167'
source_collection: openai/math
batch_id: B058
subject: Combinatorics
source_paper_ids:
- P-000335
- P-000336
instrument_ids:
- MI-000566
- MI-000567
headline: The sources claim a weak pinned planar distance theorem and a fixed power saving for planar
  unit distances.
central_instrument: A deliberately off-diagonal coupling preserves the needed marginals and cancels singleton
  cells exactly. A random strict history prefix converts endpoint mutual information into bounded center-test
  prediction error.
novelty_assessment: Finite-population corrections, KL chain rules and Pinsker are classical. The exact
  coupling and posterior/fresh-test interface are recorded as source implementations; no priority claim
  or geometric headline certification is made.
formalization_summary: PinnedDistances states uniform decay of the supremal fraction of repeated distance
  fibers of size at least n^s for each s>0. Its target does not separately state the many-pins corollary.
  PlanarUnitDistances separately asserts constants C>0 and 1<=beta<4/3 bounding every finite planar set
  by C*n^beta unordered unit pairs. Every linked Comparator and the scope document were read in full.
  The headline Comparator proof bodies contain sorry; this does not describe the separate solution files.
  No solution or Lean project was built.
statement_faithfulness: The cell identity assumes a uniform subset with at least two elements. Its integrated
  conclusion needs the source additive-overlap identity. Prediction uses a conditional-independent wedge,
  each endpoint own posterior, natural-log KL and a fresh test independent of the retained prefix.
dependencies: Sampling without replacement, signed measures, finite-population corrections, relative entropy,
  conditional expectation and Cauchy-Schwarz.
antecedents: Classical sampling identities; Ahlswede wringing and the standard KL chain rule and Pinsker
  inequality.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Distinct-pair cancellation and predictions from fresh tests

## Source manuscripts and claim

- [The weak pinned planar distance theorem](../papers/P-000335.md): selected passages extracted.
- [A power saving for planar unit distances](../papers/P-000336.md): selected passages extracted.

The sources claim a weak pinned planar distance theorem and a fixed power saving for planar unit distances.

## Extracted instruments

- [MI-000566: Cancel singleton tails with an exact distinct-pair coupling](../instruments/MI-000566.md)
- [MI-000567: Predict bounded center tests from a short strict history prefix](../instruments/MI-000567.md)

## Dependencies and antecedents

Sampling without replacement, signed measures, finite-population corrections, relative entropy, conditional expectation and Cauchy-Schwarz.

Classical sampling identities; Ahlswede wringing and the standard KL chain rule and Pinsker inequality.

## Review and formalization scope

Read the complete variance lemma and its off-diagonal construction, and the complete arbitrary finite-law prediction device proof. The geometric hierarchy, its integrated overlap identity and the global distance arguments are not certified.

PinnedDistances states uniform decay of the supremal fraction of repeated distance fibers of size at least n^s for each s>0. Its target does not separately state the many-pins corollary. PlanarUnitDistances separately asserts constants C>0 and 1<=beta<4/3 bounding every finite planar set by C*n^beta unordered unit pairs. Every linked Comparator and the scope document were read in full. The headline Comparator proof bodies contain sorry; this does not describe the separate solution files. No solution or Lean project was built.

The cell identity assumes a uniform subset with at least two elements. Its integrated conclusion needs the source additive-overlap identity. Prediction uses a conditional-independent wedge, each endpoint own posterior, natural-log KL and a fresh test independent of the retained prefix.

[Batch record](../../batches/B058/README.md)
