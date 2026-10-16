---
id: openai-math-367
record_type: family
title: Exact tensor projections and sharp contraction estimates
source_family: '367'
source_collection: openai/math
batch_id: B028
subject: Partial differential equations
source_paper_ids:
- P-000183
instrument_ids:
- MI-000328
- MI-000329
headline: The source claims that seven is the critical dimension for nonflat one-homogeneous one-phase
  Bernoulli global minimizers, with the resulting sharp singular-set dimension bound.
central_instrument: Integer multiples of orthogonal trace-free projections certify nonnegative tensor
  blocks. Sharp spectral and contraction bounds turn tensor graph terms into controlled scalar coefficients.
novelty_assessment: Symmetrization, trace removal, Schur-type tensor decompositions and constrained eigenvalue
  optimization are classical. This extraction records explicit five-dimensional normalizations and sharp
  constants, not a certification of the source universal certificate or dimension theorem.
formalization_summary: Read BernoulliNonflatInSeven.lean and its scope. The target only asserts existence
  of a nonzero nonflat one-homogeneous global minimizer in dimension seven, with arbitrary Sobolev competitors
  and volume-one Bernoulli energy. Classification through dimension six and the singular-set bound are
  outside it. The inspected Comparator contains a sorry placeholder; no Lean proof was built or kernel-checked.
statement_faithfulness: The tensor space is Euclidean dimension five. The matrices are scaled projections,
  not idempotent projections unless divided by their stated scale. The matrix A is symmetric trace-free
  with Frobenius norm one.
dependencies: Slot permutations, orthogonal symmetrization, trace adjoints, finite-dimensional Lagrange
  multipliers and Cauchy-Schwarz.
antecedents: Classical orthogonal tensor decomposition and constrained trace inequalities; no historical
  first-priority claim for these constants was established.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Exact tensor projections and sharp contraction estimates

## Source manuscript and claim

[The critical dimension for one-phase Bernoulli minimizers](../papers/P-000183.md), by OpenAI, September 24, 2026.

The source claims that seven is the critical dimension for nonflat one-homogeneous one-phase Bernoulli global minimizers, with the resulting sharp singular-set dimension bound.

## Extracted instruments

- [MI-000328: Certify tensor Gram blocks using integer-scaled orthogonal projections](../instruments/MI-000328.md)
- [MI-000329: Retain trace-free structure to obtain sharp five-dimensional contraction constants](../instruments/MI-000329.md)

## Dependencies and antecedents

Slot permutations, orthogonal symmetrization, trace adjoints, finite-dimensional Lagrange multipliers and Cauchy-Schwarz.

Classical orthogonal tensor decomposition and constrained trace inequalities; no historical first-priority claim for these constants was established. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete positive-projection and tensor-bound proofs and the main theorem. The coefficient tables, graph collection, universal certificate and geometric exclusion arguments were not audited.

Read BernoulliNonflatInSeven.lean and its scope. The target only asserts existence of a nonzero nonflat one-homogeneous global minimizer in dimension seven, with arbitrary Sobolev competitors and volume-one Bernoulli energy. Classification through dimension six and the singular-set bound are outside it. The inspected Comparator contains a sorry placeholder; no Lean proof was built or kernel-checked.

The tensor space is Euclidean dimension five. The matrices are scaled projections, not idempotent projections unless divided by their stated scale. The matrix A is symmetric trace-free with Frobenius norm one.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/367.md) · [Batch record](../../batches/B028/README.md)
