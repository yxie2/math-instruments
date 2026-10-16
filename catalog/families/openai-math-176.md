---
id: openai-math-176
record_type: family
title: Planted resampling and ratio-maximizing graph cores
source_family: '176'
source_collection: openai/math
batch_id: B015
subject: Combinatorics
source_paper_ids:
- P-000132
instrument_ids:
- MI-000224
- MI-000225
headline: The source claims the second Kahn-Kalai graph-containment comparison, with a universal multiple
  of the actual expectation threshold times 1+log2 of the target edge count.
central_instrument: Planted-set posterior resampling creates a smaller recoverable fragment and controls
  outside-coordinate tests. Maximizing normalized containment probabilities produces rapidly growing conditionally
  spread edge blocks.
novelty_assessment: The source explicitly credits Mossel, Niles-Weed, Sun and Zadik for planted posterior
  resampling and Tran for ratio-maximizing cores. The selected refinements are the outside-test bound,
  capacity constants and hierarchy interface, not invention of these methods.
formalization_summary: SecondKahnKalai.lean defines actual non-induced copy counts and Bernoulli containment
  and expectation thresholds, and states constants 2048 exp(50) and 6144 exp(50) in the edge-count and
  vertex-count bounds. The scope document and Comparator statement were read. No Lean solution was built
  or kernel-checked; the auxiliary tools are not separate certified targets.
statement_faithfulness: Duplicate labels remain distinct indexed choices. At fixed product sample W the
  target law need not be the prior. The graph hierarchy has spread child laws, not an assumed spread law
  on an entire path.
dependencies: Bayes resampling, small-denominator truncation, spread intersection bounds, symmetry of
  unlabelled copy counts and normalized containment maximization.
antecedents: Mossel, Niles-Weed, Sun and Zadik, A Bayesian proof of the spread lemma, and its 2022 preprint;
  Tran, Fractional expectation thresholds and the second Kahn-Kalai conjecture, Section 3.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Planted resampling and ratio-maximizing graph cores

## Source manuscript and claim

[The second Kahn–Kalai conjecture](../papers/P-000132.md), by OpenAI, September 24, 2026.

The source claims the second Kahn-Kalai graph-containment comparison, with a universal multiple of the actual expectation threshold times 1+log2 of the target edge count.

## Extracted instruments

- [MI-000224: Planted posterior resampling gives recoverable fragments and outside-coordinate control](../instruments/MI-000224.md)
- [MI-000225: Normalized containment maximizers give small cores with conditionally spread extensions](../instruments/MI-000225.md)

## Dependencies and antecedents

Bayes resampling, small-denominator truncation, spread intersection bounds, symmetry of unlabelled copy counts and normalized containment maximization.

Mossel, Niles-Weed, Sun and Zadik, A Bayesian proof of the spread lemma, and its 2022 preprint; Tran, Fractional expectation thresholds and the second Kahn-Kalai conjecture, Section 3. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full local resampling and graph hierarchy proofs. The simultaneous tree reduction and iteration proving the global threshold bound were not audited.

SecondKahnKalai.lean defines actual non-induced copy counts and Bernoulli containment and expectation thresholds, and states constants 2048 exp(50) and 6144 exp(50) in the edge-count and vertex-count bounds. The scope document and Comparator statement were read. No Lean solution was built or kernel-checked; the auxiliary tools are not separate certified targets.

Duplicate labels remain distinct indexed choices. At fixed product sample W the target law need not be the prior. The graph hierarchy has spread child laws, not an assumed spread law on an entire path.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/176.md) · [Batch record](../../batches/B015/README.md)
