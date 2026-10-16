---
id: openai-math-373
record_type: family
title: Separate a deterministic selection obstruction from equality of optimal values
source_family: '373'
source_collection: openai/math
batch_id: B027
subject: Partial differential equations
source_paper_ids:
- P-000182
instrument_ids:
- MI-000326
- MI-000327
headline: The source claims a smooth compactly supported probability density on R3, with smooth compactly
  supported square root, whose three-marginal Coulomb optimum is attained by a coupling but by no deterministic
  pair of maps, while the two infima agree.
central_instrument: A source component carrying twice each copied target density cannot select any branch
  deterministically. A separate cell-mass construction approximates a separated coupling by graph plans
  with exact marginals and controlled cost.
novelty_assessment: 'Equality of Monge and Kantorovich infima for Coulomb cost predates this source: Colombo-Di
  Marino prove a stronger cyclic formulation. The elementary selection obstruction is distinguished from
  the unreviewed Coulomb support certificate needed for the claimed nonattainment example.'
formalization_summary: Read CoulombCounterexample.lean and its scope. Its target includes smoothness of
  rho and sqrt(rho), compact support, finite attained Kantorovich value, strict failure of every deterministic
  optimizer, equal infima and finite epsilon-approximating graph plans. The inspected Comparator ends
  in sorry. It is a target statement, not a Lean proof built or kernel-checked here.
statement_faithfulness: A missing deterministic optimizer is compatible with equal infima. The obstruction
  concerns every measurable branch subset, not merely total component masses. The approximation preserves
  marginals exactly and uses uniform component separation to avoid the Coulomb singularity.
dependencies: Borel images under homeomorphisms, pushforward measure inequalities, nonatomic splitting,
  Borel transport between densities and a separated-cost oscillation estimate.
antecedents: Colombo-Di Marino, Equality between Monge and Kantorovich multimarginal problems with Coulomb
  cost; Rosenblatt conditional distribution transforms.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Separate a deterministic selection obstruction from equality of optimal values

## Source manuscript and claim

[A counterexample to the Monge ansatz for the three-marginal Coulomb cost](../papers/P-000182.md), by OpenAI, September 25, 2026.

The source claims a smooth compactly supported probability density on R3, with smooth compactly supported square root, whose three-marginal Coulomb optimum is attained by a coupling but by no deterministic pair of maps, while the two infima agree.

## Extracted instruments

- [MI-000326: Rule out deterministic branches by testing selected subsets](../instruments/MI-000326.md)
- [MI-000327: Approximate separated couplings by graph plans with exact cell masses](../instruments/MI-000327.md)

## Dependencies and antecedents

Borel images under homeomorphisms, pushforward measure inequalities, nonatomic splitting, Borel transport between densities and a separated-cost oscillation estimate.

Colombo-Di Marino, Equality between Monge and Kantorovich multimarginal problems with Coulomb cost; Rosenblatt conditional distribution transforms. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete splitting and equal-infima sections, including the Borel conditional-quantile transport proof, plus the introduction. The dual Coulomb certificate, local minimizing branches and forcing of optimal support were not audited.

Read CoulombCounterexample.lean and its scope. Its target includes smoothness of rho and sqrt(rho), compact support, finite attained Kantorovich value, strict failure of every deterministic optimizer, equal infima and finite epsilon-approximating graph plans. The inspected Comparator ends in sorry. It is a target statement, not a Lean proof built or kernel-checked here.

A missing deterministic optimizer is compatible with equal infima. The obstruction concerns every measurable branch subset, not merely total component masses. The approximation preserves marginals exactly and uses uniform component separation to avoid the Coulomb singularity.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/373.md) · [Batch record](../../batches/B027/README.md)
