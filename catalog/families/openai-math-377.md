---
id: openai-math-377
record_type: family
title: Quadratic envelopes with moving centers and barycentric constraints
source_family: '377'
source_collection: openai/math
batch_id: B028
subject: Partial differential equations
source_paper_ids:
- P-000186
instrument_ids:
- MI-000334
- MI-000335
headline: The source claims dimension-dependent uniform interior C1,alpha estimates for bounded infinity-harmonic
  functions in every dimension at least three, with a nonexplicit exponent at most one third.
central_instrument: Quadratic envelopes obey a semigroup law and a moving-center convexity correction
  for the limiting PDE. A variance-penalized barycentric envelope has a finite-support dual certificate
  and a sharp Jensen-defect bound.
novelty_assessment: Quadratic infimum/supremum convolutions and concave-envelope duality are classical.
  Evans-Savin already use the same limiting PDE and quadratic slice slopes. The source moving-center correction
  and constrained envelope formulation are extracted without certifying its higher-dimensional regularity
  theorem.
formalization_summary: No family-specific scope document or Comparator target is listed. No Lean artifact
  was built or kernel-checked.
statement_faithfulness: The envelope assertions require subquadratic growth uniformly on compact time
  intervals. The viscosity equation is the limiting equation F[f]=D2f[(grad_x f,1),(grad_x f,1)], not
  the original infinity-Laplacian. Finite-configuration duality does not by itself prove the subsequent
  PDE subsolution rule.
dependencies: Coercive quadratic optimization, viscosity upper tests, completion of squares, convex separation
  and finite-dimensional convex hulls.
antecedents: Evans-Savin, C1,alpha regularity for infinity harmonic functions in two dimensions, Sections
  2.4 and 3.1; classical Hopf-Lax and concave-envelope constructions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Quadratic envelopes with moving centers and barycentric constraints

## Source manuscript and claim

[Uniform Interior $`C^{1,\alpha}`$ Estimates for Infinity-Harmonic Functions](../papers/P-000186.md), by OpenAI, October 4, 2026.

The source claims dimension-dependent uniform interior C1,alpha estimates for bounded infinity-harmonic functions in every dimension at least three, with a nonexplicit exponent at most one third.

## Extracted instruments

- [MI-000334: Add an explicit correction when moving a quadratic-envelope center](../instruments/MI-000334.md)
- [MI-000335: Enforce a barycenter while optimizing a variance-penalized envelope](../instruments/MI-000335.md)

## Dependencies and antecedents

Coercive quadratic optimization, viscosity upper tests, completion of squares, convex separation and finite-dimensional convex hulls.

Evans-Savin, C1,alpha regularity for infinity harmonic functions in two dimensions, Sections 2.4 and 3.1; classical Hopf-Lax and concave-envelope constructions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete quadratic-envelope and barycentric-envelope proofs, the limiting PDE definition and the main theorem. Common-time subsolution rules, contact propagation, final Liouville rigidity and the full compactness reduction were not audited.

No family-specific scope document or Comparator target is listed. No Lean artifact was built or kernel-checked.

The envelope assertions require subquadratic growth uniformly on compact time intervals. The viscosity equation is the limiting equation F[f]=D2f[(grad_x f,1),(grad_x f,1)], not the original infinity-Laplacian. Finite-configuration duality does not by itself prove the subsequent PDE subsolution rule.

[Batch record](../../batches/B028/README.md)
