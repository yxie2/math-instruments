---
id: openai-math-267
record_type: family
title: Thermal coherences and noninteger trace powers
source_family: '267'
source_collection: openai/math
batch_id: B081
subject: Mathematical physics
source_paper_ids:
- P-000505
instrument_ids:
- MI-000756
- MI-000757
headline: The family claims condensation and depletion estimates for dilute interacting Bose gases.
central_instrument: Preserve the full thermal kernel through purification and common-measure affinity;
  use exterior powers of an evolution to control all positive real trace powers.
novelty_assessment: Classical ingredients are credited; novelty of the source assembly is not established.
formalization_summary: The scope was read in full. Selected HardSphere definitions and its complete main
  target were inspected; the intervening construction was not read in full. The target concerns pure and
  ground-supported mixed ground states, not positive temperature. It contains sorry; no separate solution
  or Lean build was checked.
statement_faithfulness: The purification kernel is nonnegative. The continuum sandwich uses a form-domain
  product rule, not an assumed operator-domain identity.
dependencies: Positive heat kernels, semigroup composition, Holder inequality, differential energy estimates,
  exterior powers and log-majorization.
antecedents: Classical square-root purification, Hellinger affinity and log-majorization. The source also
  cites companions within this same family.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Thermal coherences and noninteger trace powers

## Source manuscripts and claim

- [Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas](../papers/P-000505.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026)
- [Quantum Depletion for Fixed Bounded Repulsive Potentials](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026)
- [A density-uniform condensate bound for dilute Bose gases](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026)
- [Ground-state condensation in the dilute hard-sphere gas](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026)

The family claims condensation and depletion estimates for dilute interacting Bose gases.

## Extracted instruments

- [MI-000756: Retain thermal coherences in a nonnegative purification and compare by a common measure](../instruments/MI-000756.md)
- [MI-000757: Extend a heat-kernel sandwich estimate to every positive real trace power](../instruments/MI-000757.md)

## Dependencies and antecedents

Positive heat kernels, semigroup composition, Holder inequality, differential energy estimates, exterior powers and log-majorization.

Classical square-root purification, Hellinger affinity and log-majorization. The source also cites companions within this same family.

## Review and formalization scope

Read complete purification and affinity proofs and the all-q sandwich proof. Four companions are inventory-only, including the source-cited ground-state and density-uniform antecedents. Their proofs were not independently audited.

The scope was read in full. Selected HardSphere definitions and its complete main target were inspected; the intervening construction was not read in full. The target concerns pure and ground-supported mixed ground states, not positive temperature. It contains sorry; no separate solution or Lean build was checked.

The purification kernel is nonnegative. The continuum sandwich uses a form-domain product rule, not an assumed operator-domain identity.

[Batch record](../../batches/B081/README.md)
