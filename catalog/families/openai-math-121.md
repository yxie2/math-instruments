---
id: openai-math-121
record_type: family
title: Nonconservative tree curvature and entropy bounds with fixed block masses
source_family: '121'
source_collection: openai/math
batch_id: B035
subject: Theoretical computer science
source_paper_ids:
- P-000213
instrument_ids:
- MI-000388
- MI-000389
headline: The source claims an almost-linear randomized (1+epsilon)-approximation scheme for unit-cost
  edit distance.
central_instrument: A tree energy telescope charges both mass discrepancy and endpoint perturbation. Optimistic
  entropy minimization tolerates large blockwise cost decrements when only within-block ranges are small.
novelty_assessment: Weighted variance and optimistic regularized learning are established. The extraction
  isolates the mass-slack and fixed-block hypotheses; no full edit-distance algorithm certification.
formalization_summary: 'Inspected the final EditApproximation.lean target: distortion success at least
  2/3, zero on every execution for equal strings, almost-linear expected work for polynomially bounded
  integer alphabets, and every-execution polynomial space. It contains sorry; the long supporting construction
  was not audited or built.'
statement_faithfulness: The comparison tree is fixed before refinement randomness. Warmup masses may fail
  to add; those discrepancies must be charged. The entropy feasible set has fixed mass in each block and
  contains a positive vector.
dependencies: Weighted variance, signed mass telescopes, entropy/KL optimality, fixed block sums and monotone
  cost decrements.
antecedents: Classical energy telescoping; Rakhlin-Sridharan optimistic FTRL and exponential weighting.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Nonconservative tree curvature and entropy bounds with fixed block masses

## Source manuscript and claim

[An Almost-Linear Approximation Scheme for Edit Distance](../papers/P-000213.md), by OpenAI, September 24, 2026.

The source claims an almost-linear randomized (1+epsilon)-approximation scheme for unit-cost edit distance.

## Extracted instruments

- [MI-000388: Telescope weighted curvature when parent and child masses do not conserve](../instruments/MI-000388.md)
- [MI-000389: Use fixed block masses to remove large predictable cost offsets from entropy regret](../instruments/MI-000389.md)

## Dependencies and antecedents

Weighted variance, signed mass telescopes, entropy/KL optimality, fixed block sums and monotone cost decrements.

Classical energy telescoping; Rakhlin-Sridharan optimistic FTRL and exponential weighting. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the comparison-cost and complete curvature proof, and the full fixed-block entropy proof. The seed scheme, band computation, numerical optimizer and running-time argument were not audited.

Inspected the final EditApproximation.lean target: distortion success at least 2/3, zero on every execution for equal strings, almost-linear expected work for polynomially bounded integer alphabets, and every-execution polynomial space. It contains sorry; the long supporting construction was not audited or built.

The comparison tree is fixed before refinement randomness. Warmup masses may fail to add; those discrepancies must be charged. The entropy feasible set has fixed mass in each block and contains a positive vector.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/121.md) · [Batch record](../../batches/B035/README.md)
