---
id: openai-math-050
record_type: family
title: From a degenerate squared seminorm to a dynamical measure obstruction
source_family: '050'
source_collection: openai/math
batch_id: B026
subject: Algebraic and complex geometry
source_paper_ids:
- P-000178
instrument_ids:
- MI-000318
- MI-000319
headline: The source claims a rank-two algebraic bundle G on P1 times P1 whose coordinatewise power pullbacks,
  twisted by O(1,1), are ample for every positive power but have no strictly Griffiths-positive smooth
  metric for all sufficiently large powers.
central_instrument: A nonzero plurisubharmonic squared seminorm on a negative line bundle produces a positive
  curvature measure retaining zero-set atoms. Two finite-order projective maps with a loxodromic product
  exclude any invariant finite positive measure.
novelty_assessment: Singular metric curvature and projective invariant-measure obstructions are established.
  The source combines them with explicit matrices and a proposed quadratic-limit construction. That compactness
  construction and the global Griffiths counterexample are not certified.
formalization_summary: Read the family scope and QuadricBundles.lean, including algebraic transition charts,
  symmetric-section embedding, power pullback twist and strict positivity expressed using the dual metric
  Hessian. The target asserts eventual nonexistence with no effective threshold; the separate explicit
  very-ampleness bound is not selected. These are inspected target statements with sorry placeholders;
  no Lean solution was built or kernel-checked.
statement_faithfulness: Zeros of the seminorm may contribute curvature atoms and cannot be excised. The
  invariant-measure argument needs a finite positive measure. No numerical threshold for the source bundle
  family follows from this extraction.
dependencies: Levi determinant, decreasing radial regularization, local integrability, distributional
  curvature, degree of O(-b), loxodromic annuli and finite permutations of a two-point support.
antecedents: Raufi and Berndtsson-Paun singular Hermitian metric theory; classical Furstenberg-type concentration
  of projective invariant measures.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# From a degenerate squared seminorm to a dynamical measure obstruction

## Source manuscript and claim

[Ample rank-two bundles on the quadric surface without Griffiths-positive metrics](../papers/P-000178.md), by OpenAI, September 24, 2026.

The source claims a rank-two algebraic bundle G on P1 times P1 whose coordinatewise power pullbacks, twisted by O(1,1), are ample for every positive power but have no strictly Griffiths-positive smooth metric for all sufficiently large powers.

## Extracted instruments

- [MI-000318: Keep the zero-set atoms when turning a squared seminorm into curvature](../instruments/MI-000318.md)
- [MI-000319: Two odd-order projective maps with a loxodromic product admit no finite invariant measure](../instruments/MI-000319.md)

## Dependencies and antecedents

Levi determinant, decreasing radial regularization, local integrability, distributional curvature, degree of O(-b), loxodromic annuli and finite permutations of a two-point support.

Raufi and Berndtsson-Paun singular Hermitian metric theory; classical Furstenberg-type concentration of projective invariant measures. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full ruling reduction, logarithmic-curvature proof, invariant-measure proof and explicit matrix lemma. The construction of the quadratic limit and the ampleness proof were not audited.

Read the family scope and QuadricBundles.lean, including algebraic transition charts, symmetric-section embedding, power pullback twist and strict positivity expressed using the dual metric Hessian. The target asserts eventual nonexistence with no effective threshold; the separate explicit very-ampleness bound is not selected. These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

Zeros of the seminorm may contribute curvature atoms and cannot be excised. The invariant-measure argument needs a finite positive measure. No numerical threshold for the source bundle family follows from this extraction.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/050.md) · [Batch record](../../batches/B026/README.md)
