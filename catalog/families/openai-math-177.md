---
id: openai-math-177
record_type: family
title: Partial homology resolutions and skeleton weight transfer
source_family: '177'
source_collection: openai/math
batch_id: B015
subject: Combinatorics
source_paper_ids:
- P-000133
instrument_ids:
- MI-000226
- MI-000227
headline: The source constructs, for every dimension d>=3, finite pure connected complexes of growing
  size with uniformly bounded top-dimensional vertex degree and positive F2 coboundary expansion in every
  degree below d.
central_instrument: Acyclic chains with odd-order stabilizers compute low-degree group homology. Bounded
  chamber multiplicities compare the intrinsic weights of a complex and its skeleton, with a controlled
  loss in expansion.
novelty_assessment: Projective resolutions, averaging over invertible-order stabilizers and incidence
  double counting are established. These are useful explicit interfaces, not new homological principles
  or certification of the congruence construction.
formalization_summary: CoboundaryExpanders.lean states the d>=3 result with normalized chamber-incidence
  weights, actual coboundaries, a uniform top-face degree bound and vertex counts tending to infinity.
  The scope document and Comparator statement were read. No Lean solution was built or kernel-checked;
  the auxiliary tools are not separate certified targets.
statement_faithfulness: The homology comparison uses chains of simplex orbits, which need not be an ordinary
  simplicial quotient without additional checks. Expansion against cocycles becomes expansion against
  coboundaries only after cohomology vanishes.
dependencies: Averaging idempotents, induced projective modules, partial resolutions, coinvariants, incidence
  double counting and weighted support norms.
antecedents: Brown's Lectures on the cohomology of groups explains projective resolutions, coinvariants
  and stabilizer-based equivariant homology. Skeleton weight comparison follows directly from normalized
  chamber sampling.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Partial homology resolutions and skeleton weight transfer

## Source manuscript and claim

[Bounded-degree coboundary expanders in every dimension](../papers/P-000133.md), by OpenAI, September 24, 2026.

The source constructs, for every dimension d>=3, finite pure connected complexes of growing size with uniformly bounded top-dimensional vertex degree and positive F2 coboundary expansion in every degree below d.

## Extracted instruments

- [MI-000226: A partially acyclic complex with odd-order stabilizers computes low-degree group homology](../instruments/MI-000226.md)
- [MI-000227: Chamber multiplicities control skeleton weights and the loss in expansion](../instruments/MI-000227.md)

## Dependencies and antecedents

Averaging idempotents, induced projective modules, partial resolutions, coinvariants, incidence double counting and weighted support norms.

Brown's Lectures on the cohomology of groups explains projective resolutions, coinvariants and stabilizer-based equivariant homology. Skeleton weight comparison follows directly from normalized chamber sampling. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the projective-chain lemma and skeleton-weight proof. Infinite-building acyclicity, stabilization, congruence homology and the quantitative cosystolic input were not audited.

CoboundaryExpanders.lean states the d>=3 result with normalized chamber-incidence weights, actual coboundaries, a uniform top-face degree bound and vertex counts tending to infinity. The scope document and Comparator statement were read. No Lean solution was built or kernel-checked; the auxiliary tools are not separate certified targets.

The homology comparison uses chains of simplex orbits, which need not be an ordinary simplicial quotient without additional checks. Expansion against cocycles becomes expansion against coboundaries only after cohomology vanishes.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/177.md) · [Batch record](../../batches/B015/README.md)
