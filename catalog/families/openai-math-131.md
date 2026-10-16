---
id: openai-math-131
record_type: family
title: Slice projection comparison and rare-correction exact sampling
source_family: '131'
source_collection: openai/math
batch_id: B010
subject: Theoretical computer science
source_paper_ids:
- P-000114
instrument_ids:
- MI-000186
- MI-000187
headline: The source claims polynomial mixing of the specified lazy switch chain for every graphical degree
  sequence, and derives an expected-polynomial exact uniform sampler.
central_instrument: Equality-indicator errors on a fixed-cardinality Boolean slice are dominated by the
  transposition generator. An established rare-correction method converts a sufficiently accurate rational
  law into exact uniform sampling.
novelty_assessment: Johnson-slice harmonic decomposition and approximate-to-perfect sampling have established
  antecedents. The selected candidate comparison concerns summed equality projections; the exact sampler
  explicitly reuses the earlier rare-correction principle.
formalization_summary: SwitchChain.lean states mixing time at tolerance 1/4 at most 2n^8, a gap at least
  1/(24 n^2 binom(n,4)) for nonsingleton fibers, the exponential TV estimate and switch connectivity,
  for n>=4. Exact sampling is outside these selected Comparator declarations. The scope documents and
  Comparator statements were compared; no Lean solution was built or kernel-checked. The auxiliary instruments
  are not separate certified Comparator results.
statement_faithfulness: The chain is half lazy, then selects a four-vertex set uniformly and one of six
  ordered pairs of distinct perfect matchings. A valid specified switch has probability 1/(12 binom(n,4)).
  Exact sampling has expected, not worst-case, polynomial time.
dependencies: Uniform fixed-cardinality slices; centered pair-equality indicators; a pair-coefficient
  Gram decomposition; transposition eigenvalues; rational transition kernels; exact integer arithmetic
  and a rare exhaustive branch.
antecedents: Filmus develops the harmonic analysis of Boolean slices. Gobel, Liu, Manurangsi and Pappik
  give approximate-to-perfect sampling reductions, including the rare residual-distribution construction
  reused here.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Slice projection comparison and rare-correction exact sampling

## Source manuscript and claim

[Polynomial mixing of the switch chain for every graphical degree sequence](../papers/P-000114.md), by OpenAI, September 25, 2026.

The source claims polynomial mixing of the specified lazy switch chain for every graphical degree sequence, and derives an expected-polynomial exact uniform sampler.

## Extracted instruments

- [MI-000186: Pair-equality projections are dominated by the slice transposition generator](../instruments/MI-000186.md)
- [MI-000187: An exponentially rare residual branch corrects a rational approximate sampler exactly](../instruments/MI-000187.md)

## Dependencies and antecedents

Uniform fixed-cardinality slices; centered pair-equality indicators; a pair-coefficient Gram decomposition; transposition eigenvalues; rational transition kernels; exact integer arithmetic and a rare exhaustive branch.

Filmus develops the harmonic analysis of Boolean slices. Gobel, Liu, Manurangsi and Pappik give approximate-to-perfect sampling reductions, including the rare residual-distribution construction reused here. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the slice comparison and exact-sampling section, and the final variance-to-gap accounting. The graph-fiber interaction, three-row comparison and complete global spectral-gap proof were not audited.

SwitchChain.lean states mixing time at tolerance 1/4 at most 2n^8, a gap at least 1/(24 n^2 binom(n,4)) for nonsingleton fibers, the exponential TV estimate and switch connectivity, for n>=4. Exact sampling is outside these selected Comparator declarations. The scope documents and Comparator statements were compared; no Lean solution was built or kernel-checked. The auxiliary instruments are not separate certified Comparator results.

The chain is half lazy, then selects a four-vertex set uniformly and one of six ordered pairs of distinct perfect matchings. A valid specified switch has probability 1/(12 binom(n,4)). Exact sampling has expected, not worst-case, polynomial time.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/131.md) · [Batch record](../../batches/B010/README.md)
