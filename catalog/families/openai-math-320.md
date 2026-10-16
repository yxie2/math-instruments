---
id: openai-math-320
record_type: family
title: Subspace-preserving homology projections and first-order cycle lifting
source_family: '320'
source_collection: openai/math
batch_id: B041
subject: Topology
source_paper_ids:
- P-000238
instrument_ids:
- MI-000438
- MI-000439
headline: The source claims nonhomeomorphic closed aspherical four-manifolds with the same homotopy type.
central_instrument: A homology projection can preserve a chosen graded subspace even when it is not a
  subcomplex. A vanishing commutator obstruction lifts selected cycles over square-zero parameters.
novelty_assessment: Both are elementary splitting and first-order deformation arguments. Their role in
  the source tensor contraction is conditional; the manifold counterexample is not certified.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: The projection is noncanonical and is chosen for one specified subspace. The lift
  is first order with t squared zero; a higher-order extension requires new obstruction checks.
dependencies: Finite-dimensional graded linear algebra, chain homotopies, induced commutators and square-zero
  deformation.
antecedents: Classical splitting of complexes over a field and first-order obstruction theory.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Subspace-preserving homology projections and first-order cycle lifting

## Source manuscript and claim

[Nonhomeomorphic closed aspherical four-manifolds with the same homotopy type](../papers/P-000238.md), by OpenAI, October 4, 2026.

The source claims nonhomeomorphic closed aspherical four-manifolds with the same homotopy type.

## Extracted instruments

- [MI-000438: Choose a homology projection preserving a subspace that is not a subcomplex](../instruments/MI-000438.md)
- [MI-000439: Lift a kernel cycle through a square-zero perturbation using a commutator](../instruments/MI-000439.md)

## Dependencies and antecedents

Finite-dimensional graded linear algebra, chain homotopies, induced commutators and square-zero deformation.

Classical splitting of complexes over a field and first-order obstruction theory. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete subspace-projection and kernel-cycle-lifting proofs and their differential definitions. The finite specialization argument was also read, but the global endpoint-assignment and manifold construction were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

The projection is noncanonical and is chosen for one specified subspace. The lift is first order with t squared zero; a higher-order extension requires new obstruction checks.

[Batch record](../../batches/B041/README.md)
