---
id: openai-math-136
record_type: family
title: Unconditioned sampling and clipped replica consensus
source_family: '136'
source_collection: openai/math
batch_id: B044
subject: Theoretical computer science
source_paper_ids:
- P-000247
instrument_ids:
- MI-000456
- MI-000457
headline: The source claims a quasilinear PCP theorem for PPAD.
central_instrument: Stationary expander sampling controls all reserved roles before selection. A spectral
  gap controls replica disagreement and mean residual even after clipping.
novelty_assessment: Classical covariance decay and nonexpansive projection arguments; their exact sampling
  and averaging contracts are the reusable content. No novelty certification.
formalization_summary: No formalization scope document is listed in the pinned inventory. No Lean build.
statement_faithfulness: Confidence is averaged over the starting coordinate, not uniform at each start
  or conditioned on a selected answer path. Clipping and averaging cannot be exchanged.
dependencies: Stationary Markov covariance decay, Chebyshev bounds, finite union bounds, orthogonal averaging
  and nonexpansive clipping.
antecedents: Classical expander sampling and spectral-gap consensus estimates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Unconditioned sampling and clipped replica consensus

## Source manuscript and claim

[The PCP-for-PPAD conjecture: a quasilinear reduction](../papers/P-000247.md), by OpenAI, September 25, 2026.

The source claims a quasilinear PCP theorem for PPAD.

## Extracted instruments

- [MI-000456: Concentrate reserved sampling roles before adaptive selection](../instruments/MI-000456.md)
- [MI-000457: Recover replica consensus and mean residual after clipping](../instruments/MI-000457.md)

## Dependencies and antecedents

Stationary Markov covariance decay, Chebyshev bounds, finite union bounds, orthogonal averaging and nonexpansive clipping.

Classical expander sampling and spectral-gap consensus estimates. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete averaged-walk and clipping lemmas and the replica-gap hypotheses. The code, composition, geometry and PPAD reduction were not audited.

No formalization scope document is listed in the pinned inventory. No Lean build.

Confidence is averaged over the starting coordinate, not uniform at each start or conditioned on a selected answer path. Clipping and averaging cannot be exchanged.

[Batch record](../../batches/B044/README.md)
