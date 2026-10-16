---
id: openai-math-236
record_type: family
title: Compatible innovation couplings and a critical Osgood comparison
source_family: '236'
source_collection: openai/math
batch_id: B005
subject: Probability and statistical mechanics
source_paper_ids:
- P-000095
instrument_ids:
- MI-000146
- MI-000147
headline: The source claims the sharp factor-of-IID threshold tanh(beta) <= 1/sqrt(d-1) for the free Ising
  law on a d-regular tree, including equality. This extraction separates its recovery mechanism from the
  conditional analytic estimate at criticality.
central_instrument: Compatible conditional copies reduce recovery to a discrepancy variance; a small-field
  logarithmic gain and discrepancy-dependent path cutoff yield an integrable Osgood coefficient.
novelty_assessment: Conditional-copy compatibility and the point-mass recovery principle are established
  stochastic tools. The source’s critical small-field and cutoff combination is a candidate specialized
  refinement. The full critical theorem and priority are not independently certified.
formalization_summary: FreeIsing targets d>=3, beta>=0 and equivalence between the free-law IID factor
  property and the threshold, including equality. Its equivariance is almost sure for each fixed automorphism;
  the manuscript additionally supplies an everywhere-equivariant spin version. The Comparator was inspected,
  not built.
statement_faithfulness: The law is the free zero-field Ising law. Nonreconstruction alone is not a factor
  construction. Recovery is measurable and has no finitary coding or algorithmic guarantee.
dependencies: Posterior innovations; compatible disintegration on Polish path spaces; transport of stochastic
  integrals; critical field tails and weighted path estimates; an absolutely continuous Osgood comparison.
antecedents: Nam, Sly and Zhang previously built Ising IID factors beyond the uniqueness regime using
  Brownian observations. Kurtz supplies the general compatibility and strong-solution framework; Osgood
  comparison is classical. The correlation obstruction above the threshold is also an established input.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Compatible innovation couplings and a critical Osgood comparison

## Source manuscript and claim

[The sharp factor-of-IID threshold for the free Ising model on regular trees](../papers/P-000095.md), by OpenAI, September 26, 2026.

The source claims the sharp factor-of-IID threshold tanh(beta) <= 1/sqrt(d-1) for the free Ising law on a d-regular tree, including equality. This extraction separates its recovery mechanism from the conditional analytic estimate at criticality.

## Extracted instruments

- [MI-000146: Compatible conditional copies turn innovation uniqueness into measurable recovery](../instruments/MI-000146.md)
- [MI-000147: Small-field gains and an adaptive path cutoff make a critical Osgood estimate integrable](../instruments/MI-000147.md)

## Dependencies and antecedents

Posterior innovations; compatible disintegration on Polish path spaces; transport of stochastic integrals; critical field tails and weighted path estimates; an absolutely continuous Osgood comparison.

Nam, Sly and Zhang previously built Ising IID factors beyond the uniqueness regime using Brownian observations. Kurtz supplies the general compatibility and strong-solution framework; Osgood comparison is classical. The correlation obstruction above the threshold is also an established input. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the compatible-copy construction and transport, recovery proof, critical moment and small-log-loss argument, cutoff sums and final Osgood comparison. The earlier posterior field equations, critical information estimate and weighted path estimates remain inputs rather than a fully audited proof chain.

FreeIsing targets d>=3, beta>=0 and equivalence between the free-law IID factor property and the threshold, including equality. Its equivariance is almost sure for each fixed automorphism; the manuscript additionally supplies an everywhere-equivariant spin version. The Comparator was inspected, not built.

The law is the free zero-field Ising law. Nonreconstruction alone is not a factor construction. Recovery is measurable and has no finitary coding or algorithmic guarantee.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/236.md) · [Batch record](../../batches/B005/README.md)
