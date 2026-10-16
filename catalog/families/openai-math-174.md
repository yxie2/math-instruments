---
id: openai-math-174
record_type: family
title: Isotropic representations and spanning-tree separation
source_family: '174'
source_collection: openai/math
batch_id: B060
subject: Combinatorics
source_paper_ids:
- P-000347
- P-000348
instrument_ids:
- MI-000578
- MI-000579
headline: The two sources claim a constant-factor strong thin-tree theorem and a deterministic polynomial-time
  construction, including binary multiplicities.
central_instrument: Regularize a determinant potential to obtain an isotropic representation without changing
  any subset rank. Convert partition inequalities into minimum-spanning-tree inequalities through the
  Kruskal integral.
novelty_assessment: The determinant potential and Cauchy-Binet lower bound have classical Barthe antecedents.
  The separation mechanism is a spanning-tree polyhedral argument. No new priority or complete thin-tree
  proof is certified.
formalization_summary: StrongThinTree asserts a universal positive constant for finite loopless multigraphs
  with at least two vertices. AlgorithmicThinTrees defines a finite-stack machine, explicit and binary-multiplicity
  encodings, polynomial fuel in input length, and a thin-tree output; it also includes the one-vertex
  empty-output case. All four scope documents and all six linked Comparators in this batch were read in
  full. Their headline targets have sorry proof bodies. No separate solution or Lean project was built.
statement_faithfulness: Edges remain indexed when parallel. The representation assumes an explicit union
  of q disjoint spanning trees and permits positive slack rho. The separator concerns connected finite
  graphs and nonnegative rational capacities.
dependencies: Cauchy-Binet, arithmetic-geometric mean, positive definite square roots, regularized minimization,
  Nash-Williams-Tutte packing, Kruskal and optimization-separation equivalence.
antecedents: Barthe determinant minimization; classical spanning-tree packing and separation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Isotropic representations and spanning-tree separation

## Source manuscripts and claim

- [The strong thin tree conjecture](../papers/P-000347.md): selected passages extracted.
- [A polynomial-time construction of strong thin trees](../papers/P-000348.md): selected passages extracted.

The two sources claim a constant-factor strong thin-tree theorem and a deterministic polynomial-time construction, including binary multiplicities.

## Extracted instruments

- [MI-000578: Regularize a determinant potential while preserving every subset rank](../instruments/MI-000578.md)
- [MI-000579: Separate partition capacity constraints using minimum spanning trees](../instruments/MI-000579.md)

## Dependencies and antecedents

Cauchy-Binet, arithmetic-geometric mean, positive definite square roots, regularized minimization, Nash-Williams-Tutte packing, Kruskal and optimization-separation equivalence.

Barthe determinant minimization; classical spanning-tree packing and separation.

## Review and formalization scope

Read both complete representation and projected-trace proofs, and the complete partition-separation argument in the algorithmic companion. The spectral selection and full bit-complexity construction were not audited.

StrongThinTree asserts a universal positive constant for finite loopless multigraphs with at least two vertices. AlgorithmicThinTrees defines a finite-stack machine, explicit and binary-multiplicity encodings, polynomial fuel in input length, and a thin-tree output; it also includes the one-vertex empty-output case. All four scope documents and all six linked Comparators in this batch were read in full. Their headline targets have sorry proof bodies. No separate solution or Lean project was built.

Edges remain indexed when parallel. The representation assumes an explicit union of q disjoint spanning trees and permits positive slack rho. The separator concerns connected finite graphs and nonnegative rational capacities.

[Batch record](../../batches/B060/README.md)
