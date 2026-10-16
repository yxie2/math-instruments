---
id: openai-math-375
record_type: family
title: Defect-weighted stability and overlap-safe test functions
source_family: '375'
source_collection: openai/math
batch_id: B028
subject: Partial differential equations
source_paper_ids:
- P-000185
instrument_ids:
- MI-000332
- MI-000333
headline: The source claims stable rigidity for the quartic Allen-Cahn equation in dimension seven without
  an energy-growth assumption, and monotone rigidity in dimension eight.
central_instrument: The inverse transition profile makes departure from planarity a nonnegative defect.
  Taking the square root of the sum of branch squares pushes immersed tests to physical space while subtracting
  a nonnegative gradient variance.
novelty_assessment: The inverse-profile equations and stability test already occur explicitly in Liu-Luo-Wang-Wei-Wei-Wu,
  Lemma 2.1, which was checked in the primary preprint. The branch variance is an elementary norm-gradient
  identity. Their use does not certify the source higher-dimensional rigidity claims.
formalization_summary: No family-specific scope document or Comparator target is listed. No Lean artifact
  was built or kernel-checked.
statement_faithfulness: The equation and constants concern the scalar quartic potential. The inverse profile
  is used only for |v|<1. Physical stability allows all compact scalar tests; overlapping normal tubes
  require branch aggregation rather than an assumed globally injective tube.
dependencies: Modica gradient bound, chain rule, ground-state transform, strong minimum principle, local
  inverse branches and the area formula.
antecedents: Liu, Luo, Wang, Juncheng Wei, Yong Wei and Wu, arXiv:2609.21680, Lemma 2.1; classical quadratic-form
  transforms and norm-gradient inequalities.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Defect-weighted stability and overlap-safe test functions

## Source manuscript and claim

[A positive resolution of De Giorgi's conjecture in dimension eight](../papers/P-000185.md), by OpenAI, September 26, 2026.

The source claims stable rigidity for the quartic Allen-Cahn equation in dimension seven without an energy-growth assumption, and monotone rigidity in dimension eight.

## Extracted instruments

- [MI-000332: Use an inverse profile to turn stability into a weighted defect inequality](../instruments/MI-000332.md)
- [MI-000333: Push overlapping lifted tests down by their Euclidean norm](../instruments/MI-000333.md)

## Dependencies and antecedents

Modica gradient bound, chain rule, ground-state transform, strong minimum principle, local inverse branches and the area formula.

Liu, Luo, Wang, Juncheng Wei, Yong Wei and Wu, arXiv:2609.21680, Lemma 2.1; classical quadratic-form transforms and norm-gradient inequalities. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete inverse-profile/stability calculation and the lifted-test pushdown proof, plus both main theorem statements. Sharp normal comparison, global reach budgets and density removal were not audited.

No family-specific scope document or Comparator target is listed. No Lean artifact was built or kernel-checked.

The equation and constants concern the scalar quartic potential. The inverse profile is used only for |v|<1. Physical stability allows all compact scalar tests; overlapping normal tubes require branch aggregation rather than an assumed globally injective tube.

[Batch record](../../batches/B028/README.md)
