---
id: openai-math-151
record_type: family
title: Entropy localization and ordered radial itineraries
source_family: '151'
source_collection: openai/math
batch_id: B051
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000284
instrument_ids:
- MI-000506
- MI-000507
headline: The source claims a noninvertible C1 counterexample to the homological entropy lower bound,
  detected in second homology.
central_instrument: Compactness turns pointwise attraction into a uniform small frequency of exceptional
  blocks. Ordered radial itineraries have only linearly many possibilities before taking finite products.
novelty_assessment: The localization conclusion follows from the classical variational principle; the
  direct coding and radial chain count are elementary explicit proofs, not claimed as new entropy theorems.
formalization_summary: The target is a nonbijective C1 map on a circle times a finite product of two-spheres,
  of dimension at least five, with zero topological entropy and a nonzero H2 eigenvector of eigenvalue
  two. The scope document and all linked Comparator definitions and targets were read. Their target proofs
  contain sorry; no solution or Lean project was built.
statement_faithfulness: Attraction is pointwise to a compact forward-invariant set and need not have a
  uniform final entry time. Radial monotonicity concerns the initial radius, not monotonicity of each
  orbit in time.
dependencies: Compactness, continuity, separated-set entropy, finite block covers and chains in a finite
  product order.
antecedents: The variational principle for topological entropy, with Misiurewicz giving a classical proof;
  zero entropy of monotone interval maps.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Entropy localization and ordered radial itineraries

## Source manuscripts and claim

- [A C^1 Counterexample to the Entropy Conjecture](../papers/P-000284.md): selected passages extracted.

The source claims a noninvertible C1 counterexample to the homological entropy lower bound, detected in second homology.

## Extracted instruments

- [MI-000506: Localize zero entropy under pointwise attraction](../instruments/MI-000506.md)
- [MI-000507: Bound radial orbit descriptions by a chain of label vectors](../instruments/MI-000507.md)

## Dependencies and antecedents

Compactness, continuity, separated-set entropy, finite block covers and chains in a finite product order.

The variational principle for topological entropy, with Misiurewicz giving a classical proof; zero entropy of monotone interval maps.

## Review and formalization scope

Read both complete entropy lemmas and the introduction specifying noninvertibility and intermediate-degree homology. The construction, C1 regularity, attraction and homological eigenvalue are outside these checks.

The target is a nonbijective C1 map on a circle times a finite product of two-spheres, of dimension at least five, with zero topological entropy and a nonzero H2 eigenvector of eigenvalue two. The scope document and all linked Comparator definitions and targets were read. Their target proofs contain sorry; no solution or Lean project was built.

Attraction is pointwise to a compact forward-invariant set and need not have a uniform final entry time. Radial monotonicity concerns the initial radius, not monotonicity of each orbit in time.

[Batch record](../../batches/B051/README.md)
