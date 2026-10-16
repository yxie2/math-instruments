---
id: openai-math-171
record_type: family
title: Balanced mixtures, scattered moments and retained-event posteriors
source_family: '171'
source_collection: openai/math
batch_id: B015
subject: Combinatorics
source_paper_ids:
- P-000131
instrument_ids:
- MI-000221
- MI-000222
- MI-000223
headline: The source claims an absolute C with the diagonal hypercube Ramsey bound R(Q_n)<=C 2^n for every
  n>=0, using non-induced monochromatic copies.
central_instrument: Robust survival under label deletion yields mixtures with small coordinate loads.
  Separated product tests control aggregate moments, and posterior comparisons retain the event mass instead
  of conditioning it away.
novelty_assessment: Convex separation, Kakutani fixed points, moment expansion and Bayes cancellation
  are established. These extracted interfaces preserve the source's bookkeeping and are not a certification
  of the cube-embedding construction.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  statement or proof was certified for these extracted tools.
statement_faithfulness: Output rules in the fixed-point argument must be independent of the mixed profiles.
  Moment bounds retain the success indicator. A gated posterior exception has small joint event mass,
  not necessarily small conditional probability given that event.
dependencies: Finite convex separation, fixed-point correspondences, bounded local dependence, moment
  expansion, nonnegative likelihoods and Bayes formula.
antecedents: The source explicitly uses Kakutani's fixed-point theorem and standard probabilistic comparisons.
  The general mixture and posterior principles are not claimed as new.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Balanced mixtures, scattered moments and retained-event posteriors

## Source manuscript and claim

[The hypercube Ramsey number has linear order](../papers/P-000131.md), by OpenAI, September 23, 2026.

The source claims an absolute C with the diagonal hypercube Ramsey bound R(Q_n)<=C 2^n for every n>=0, using non-induced monochromatic copies.

## Extracted instruments

- [MI-000221: Robust witness menus admit balanced mixtures and simultaneous feasible profiles](../instruments/MI-000221.md)
- [MI-000222: Separated product comparisons yield aggregate moments despite nearby dependencies](../instruments/MI-000222.md)
- [MI-000223: Posterior domination retains the mass of a required event](../instruments/MI-000223.md)

## Dependencies and antecedents

Finite convex separation, fixed-point correspondences, bounded local dependence, moment expansion, nonnegative likelihoods and Bayes formula.

The source explicitly uses Kakutani's fixed-point theorem and standard probabilistic comparisons. The general mixture and posterior principles are not claimed as new. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete balanced-profile, scattered-moment and gated-posterior proofs. The long regime analysis, near-product samplers, resampling application and final cube embedding were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean statement or proof was certified for these extracted tools.

Output rules in the fixed-point argument must be independent of the mixed profiles. Moment bounds retain the success indicator. A gated posterior exception has small joint event mass, not necessarily small conditional probability given that event.

[Batch record](../../batches/B015/README.md)
