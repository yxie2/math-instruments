---
id: openai-math-095
record_type: family
title: Singular epigraph sections and angular Gram factorizations
source_family: 095
source_collection: openai/math
batch_id: B072
subject: Convex and metric geometry
source_paper_ids:
- P-000453
- P-000454
instrument_ids:
- MI-000684
- MI-000685
headline: The family contains a general no-semidefinite-lift claim, an earlier nonspectrahedral-cone claim
  and a lift construction for that earlier cone.
central_instrument: A determinant cone projects exactly to a pseudoinverse epigraph, including its range
  condition. An explicit angular Gram factor yields linear pencils on fixed slices.
novelty_assessment: Selected mechanisms are compared with established antecedents where directly checked.
  No exhaustive novelty determination or certification of a source headline is claimed.
formalization_summary: Read the scope and complete HyperbolicCones Comparator. It targets the explicit
  degree-20 polynomial in 23 variables and excludes a direct homogeneous symmetric linear pencil of every
  positive size. This does not exclude semidefinite lifts. It belongs to the earlier nonspectrahedral
  manuscript, which is inventory-only in this batch; the newer no-lift manuscript uses a different Q construction.
  Each inspected Comparator has a sorry target body. No separate solution or Lean build was checked.
statement_faithfulness: A fixed-y Gram factor is not necessarily jointly linear in y. Fixed angular slices
  do not themselves give one global lift. The no-lift and explicit-lift manuscripts use different quadratic
  matrix constructions.
dependencies: Positive semidefinite block matrices, adjugates, polynomial continuation, Moore-Penrose
  inverses and trigonometric realification.
antecedents: Classical Schur complements and Gram factorizations; the angular example uses the Choi-Lam
  quadratic matrix.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Singular epigraph sections and angular Gram factorizations

## Source manuscripts and claim

- [Hyperbolicity Cones Without Semidefinite Lifts](../papers/P-000453.md): selected passages extracted.
- [An Exact Semidefinite Lift of a Nonspectrahedral Hyperbolicity Cone](../papers/P-000454.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [A nonspectrahedral hyperbolicity cone](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026)

The family contains a general no-semidefinite-lift claim, an earlier nonspectrahedral-cone claim and a lift construction for that earlier cone.

## Extracted instruments

- [MI-000684: Project a determinant cone to an exact pseudoinverse epigraph](../instruments/MI-000684.md)
- [MI-000685: Linearize a quadratic matrix on angular planes by an explicit Gram factor](../instruments/MI-000685.md)

## Dependencies and antecedents

Positive semidefinite block matrices, adjugates, polynomial continuation, Moore-Penrose inverses and trigonometric realification.

Classical Schur complements and Gram factorizations; the angular example uses the Choi-Lam quadratic matrix.

## Review and formalization scope

Read the full general determinant/hyperbolicity and affine-section proofs and the complete explicit angular-factor and slice-pencil proofs. Two of three manuscripts receive extractions; the earlier nonspectrahedral manuscript remains inventory-only. Neither the no-lift obstruction nor the global lift construction is certified.

Read the scope and complete HyperbolicCones Comparator. It targets the explicit degree-20 polynomial in 23 variables and excludes a direct homogeneous symmetric linear pencil of every positive size. This does not exclude semidefinite lifts. It belongs to the earlier nonspectrahedral manuscript, which is inventory-only in this batch; the newer no-lift manuscript uses a different Q construction. Each inspected Comparator has a sorry target body. No separate solution or Lean build was checked.

A fixed-y Gram factor is not necessarily jointly linear in y. Fixed angular slices do not themselves give one global lift. The no-lift and explicit-lift manuscripts use different quadratic matrix constructions.

[Batch record](../../batches/B072/README.md)
