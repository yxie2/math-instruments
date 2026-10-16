---
id: openai-math-345
record_type: family
title: Finite-cut module counts and bounded-death comparison
source_family: '345'
source_collection: openai/math
batch_id: B047
subject: Differential geometry
source_paper_ids:
- P-000257
instrument_ids:
- MI-000476
- MI-000477
headline: The source claims infinitely many closed-geodesic images on every Riemannian sphere.
central_instrument: A nonnegative graded polynomial module separates free rank from twice its torsion-generator
  count. Bounded death plus short-window injectivity gives injectivity into the global limit.
novelty_assessment: Classical graded module and persistence arguments. The source geometric hypotheses
  and closed-geodesic theorem are not certified.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean project was built.
statement_faithfulness: The module calculation needs a grading bounded below and positive degree of U.
  The persistence step uses a uniform death horizon and excludes every local event in the necessary degree
  window.
dependencies: Finite-dimensional quotient H/UH, nonnegative grading, a specified Gysin exact sequence,
  uniform ordinary death, and bounded local degree support.
antecedents: Graded Nakayama induction, modules over a polynomial PID, exact-sequence dimension counts
  and the elementary factorization of a persistence map through a later cut.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite-cut module counts and bounded-death comparison

## Source manuscripts and claim

- [Infinitely many closed geodesic images on every Riemannian sphere](../papers/P-000257.md): selected passages extracted.

The source claims infinitely many closed-geodesic images on every Riemannian sphere.

## Extracted instruments

- [MI-000476: Separate free rank and torsion in a graded finite-cut count](../instruments/MI-000476.md)
- [MI-000477: Use a bounded death horizon to turn local persistence into global injectivity](../instruments/MI-000477.md)

## Dependencies and antecedents

Finite-dimensional quotient H/UH, nonnegative grading, a specified Gysin exact sequence, uniform ordinary death, and bounded local degree support.

Graded Nakayama induction, modules over a polynomial PID, exact-sequence dimension counts and the elementary factorization of a persistence map through a later cut.

## Review and formalization scope

Read the complete finite-cut module lemma and complete degree-gap comparison proof. Extracted the algebraic rank calculation and its preliminary ordinary persistence step only. Localization, Gysin construction, uniform ordinary death and the later transient budget were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean project was built.

The module calculation needs a grading bounded below and positive degree of U. The persistence step uses a uniform death horizon and excludes every local event in the necessary degree window.

[Batch record](../../batches/B047/README.md)
