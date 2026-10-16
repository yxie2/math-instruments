---
id: openai-math-023
record_type: family
title: Exceptional factor groupings and exact separation at a stopping bin
source_family: '023'
source_collection: openai/math
batch_id: B017
subject: Number theory
source_paper_ids:
- P-000140
instrument_ids:
- MI-000240
- MI-000241
headline: The source claims an unconditional sharp first moment of normalized cubic Gauss sums over all
  primary Eisenstein primes, with main term (6/5)c_* X^(5/6)/log X and cancellation in every fixed nonzero
  angular mode.
central_instrument: An elementary partition lemma isolates the three nearly equal factors where grouping
  loses its gap. Bin-symmetric stopping and reciprocal binomial weights keep the resulting coefficient
  variables separate.
novelty_assessment: Subset grouping, multiplicative expansions and symmetry weights are elementary. The
  source-specific candidate interface is exact stopping-bin separation compatible with its restricted
  analytic coefficient classes. The global Gauss-sum estimates and historical normalization issue were
  not certified.
formalization_summary: The scope document and PattersonFirstMoment.lean were read. Its targets use all
  primary Eisenstein primes, the (6/5)c_* normalization, every fixed integer angular comparison and nonzero-mode
  cancellation. These are Comparator targets, not certified proof builds. No Lean solution was built or
  kernel-checked, and the auxiliary cards are not all separate formalization targets.
statement_faithfulness: Squarefree support is needed to kill overlaps introduced by independent coefficient
  sums. The reciprocal binomial weight is exact only because all factors in the last bin have the same
  surrogate size. The rational-prime coefficient is half the all-primary coefficient under the source
  pairing convention.
dependencies: Compactness of bounded-length exponent partitions, multiplicative prime expansions, finite-bin
  stopping, binomial symmetrization and squarefree-supported kernels.
antecedents: 'The source compares with Dunn-Radziwill, Bias in cubic Gauss sums: Patterson''s conjecture,
  and classical Type I/Type II decompositions. The selected finite identities do not establish the claimed
  unconditional analytic extension.'
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Exceptional factor groupings and exact separation at a stopping bin

## Source manuscript and claim

[An unconditional first moment for cubic Gauss sums](../papers/P-000140.md), by OpenAI, September 25, 2026.

The source claims an unconditional sharp first moment of normalized cubic Gauss sums over all primary Eisenstein primes, with main term (6/5)c_* X^(5/6)/log X and cancellation in every fixed nonzero angular mode.

## Extracted instruments

- [MI-000240: Three equal factors are the sole obstruction to a middle-third grouping](../instruments/MI-000240.md)
- [MI-000241: Bin-symmetric stopping separates multiplicative coefficients exactly](../instruments/MI-000241.md)

## Dependencies and antecedents

Compactness of bounded-length exponent partitions, multiplicative prime expansions, finite-bin stopping, binomial symmetrization and squarefree-supported kernels.

The source compares with Dunn-Radziwill, Bias in cubic Gauss sums: Patterson's conjecture, and classical Type I/Type II decompositions. The selected finite identities do not establish the claimed unconditional analytic extension. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the prime detector, factor-grouping proof and complete stopping-bin separation proof, plus the normalization discussion and Comparator targets. The Voronoi, exceptional-moment, corrected-dispersion and sharp-cutoff arguments were not audited.

The scope document and PattersonFirstMoment.lean were read. Its targets use all primary Eisenstein primes, the (6/5)c_* normalization, every fixed integer angular comparison and nonzero-mode cancellation. These are Comparator targets, not certified proof builds. No Lean solution was built or kernel-checked, and the auxiliary cards are not all separate formalization targets.

Squarefree support is needed to kill overlaps introduced by independent coefficient sums. The reciprocal binomial weight is exact only because all factors in the last bin have the same surrogate size. The rational-prime coefficient is half the all-primary coefficient under the source pairing convention.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/023.md) · [Batch record](../../batches/B017/README.md)
