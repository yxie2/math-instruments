---
id: openai-math-091
record_type: family
title: Moment-coordinate estimates for logarithmic Brunn–Minkowski
source_family: 091
source_collection: openai/math
batch_id: B003
subject: Convex and metric geometry
source_paper_ids:
- P-000086
instrument_ids:
- MI-000125
- MI-000126
headline: The source claims the logarithmic Brunn–Minkowski inequality for all origin-symmetric convex
  bodies, with the symmetric Lp and scalar B-property consequences. The extracted mechanisms concern the
  analytic variance argument.
central_instrument: A tensor square decomposition and density of double-divergence tests give a separate
  variance budget for each homogeneous slab penalty.
novelty_assessment: Candidate refinements within established moment-map and Brascamp–Lieb methods; targeted
  comparison does not certify priority or the full conjecture proof.
formalization_summary: The supplied scope document and LogBrunnMinkowski Comparator quantify over all
  dimensions n>=1 and full-dimensional origin-symmetric bodies. They target the volume inequality, not
  separate certified statements of these extracted analytic lemmas. No Lean solution was built.
statement_faithfulness: 'The Wulff intersection is essential: the geometric mean of support functions
  need not be a support function. The analytic density lemma requires an integration formula and a Hessian
  identity, as well as an upper bound on the matrix field.'
dependencies: Moment-measure existence and regularity; moment-map Stein kernels; weighted integration
  by parts; local elliptic regularity; cutoff approximation and soft-slab limits.
antecedents: Klartag supplies the moment-Hessian diffusion; Fathi identifies the Stein kernel; Kolesnikov–Livshyts–Rotem
  develop the related transport-Hessian and strengthened Brascamp–Lieb framework.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Moment-coordinate estimates for logarithmic Brunn–Minkowski

## Source manuscript and claim

[The logarithmic Brunn–Minkowski conjecture](../papers/P-000086.md), by OpenAI, None.

The source claims the logarithmic Brunn–Minkowski inequality for all origin-symmetric convex bodies, with the symmetric Lp and scalar B-property consequences. The extracted mechanisms concern the analytic variance argument.

## Extracted instruments

- [MI-000125: A moment-coordinate tensor square decomposition gives summandwise variance control](../instruments/MI-000125.md)
- [MI-000126: Removing affine obstructions from double-divergence tests without a global lower bound](../instruments/MI-000126.md)

## Dependencies and antecedents

Moment-measure existence and regularity; moment-map Stein kernels; weighted integration by parts; local elliptic regularity; cutoff approximation and soft-slab limits.

Klartag supplies the moment-Hessian diffusion; Fathi identifies the Stein kernel; Kolesnikov–Livshyts–Rotem develop the related transport-Hessian and strengthened Brascamp–Lieb framework. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the reduction, adjoint identities, density proof, tensor proof and variance closure. Checked the tensor symmetrization algebra with exact finite arithmetic and the Gaussian model of the test operator. The moment-map construction and its regularity inputs were not independently reconstructed.

The supplied scope document and LogBrunnMinkowski Comparator quantify over all dimensions n>=1 and full-dimensional origin-symmetric bodies. They target the volume inequality, not separate certified statements of these extracted analytic lemmas. No Lean solution was built.

The Wulff intersection is essential: the geometric mean of support functions need not be a support function. The analytic density lemma requires an integration formula and a Hessian identity, as well as an upper bound on the matrix field.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/091.md) · [Batch record](../../batches/B003/README.md)
