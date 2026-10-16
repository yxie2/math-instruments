---
id: openai-math-284
record_type: family
title: Adaptive direct products and fractional quantum tournaments
source_family: '284'
source_collection: openai/math
batch_id: B016
subject: Mathematical physics
source_paper_ids:
- P-000138
instrument_ids:
- MI-000236
- MI-000237
headline: The source claims a nearly quartic separation between bounded-error randomized and quantum query
  complexity of total Boolean functions, approaching the known general quartic upper bound.
central_instrument: A product of one-instance value functions survives adaptive interleaving under individual
  query caps. Complementary probabilistic comparisons yield a fractional-weight tournament with bounded
  quantum sampling cost.
novelty_assessment: The adaptive-product proof is an established Drucker-style argument. Amplitude amplification
  and tournament search are established; the fractional comparison interface with exact conditional sampling
  is the selected refinement. The total-function separation was not certified.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  proof was certified for these extracted tools.
statement_faithfulness: The direct product requires independent inputs and a cap on each instance. The
  tournament requires complementary pair probabilities and reversible fresh workspaces, but no transitive
  order or uniform gap between other candidates.
dependencies: Posterior factorization, finite decision-tree value functions, product supermartingales,
  complementary pair sums and bounded amplitude amplification preserving the conditional successful state.
antecedents: Drucker, Improved direct product theorems for randomized query complexity; Brassard-Hoyer-Mosca-Tapp
  amplitude amplification; tournament-query algorithms including Mande-Paraashar-Saurabh.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Adaptive direct products and fractional quantum tournaments

## Source manuscript and claim

[A Nearly Quartic Separation Between Randomized and Quantum Query Complexity](../papers/P-000138.md), by OpenAI, October 5, 2026.

The source claims a nearly quartic separation between bounded-error randomized and quantum query complexity of total Boolean functions, approaching the known general quartic upper bound.

## Extracted instruments

- [MI-000236: Independent instances obey a direct product under adaptive individual query caps](../instruments/MI-000236.md)
- [MI-000237: Complementary fractional comparisons support a bounded quantum tournament](../instruments/MI-000237.md)

## Dependencies and antecedents

Posterior factorization, finite decision-tree value functions, product supermartingales, complementary pair sums and bounded amplitude amplification preserving the conditional successful state.

Drucker, Improved direct product theorems for randomized query complexity; Brassard-Hoyer-Mosca-Tapp amplitude amplification; tournament-query algorithms including Mande-Paraashar-Saurabh. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the adaptive direct-product proof and the complete bounded-amplification and fractional-tournament proofs. The Forrelation input, pointer construction, certificate analysis and final separation exponents were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean proof was certified for these extracted tools.

The direct product requires independent inputs and a cap on each instance. The tournament requires complementary pair probabilities and reversible fresh workspaces, but no transitive order or uniform gap between other candidates.

[Batch record](../../batches/B016/README.md)
