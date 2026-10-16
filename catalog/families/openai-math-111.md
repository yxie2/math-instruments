---
id: openai-math-111
record_type: family
title: One-sample simulation, marked pivots and a shared rank budget
source_family: '111'
source_collection: openai/math
batch_id: B010
subject: Theoretical computer science
source_paper_ids:
- P-000111
instrument_ids:
- MI-000179
- MI-000180
- MI-000181
headline: The source claims a constant-competitive one-sample matroid prophet rule against an adversary
  that sees all samples, realized values and random bits, and an order-oblivious matroid secretary consequence.
central_instrument: A fixed-vector expected-worst-order guarantee survives sample/value gluing. A marked-pivot
  count removes dependence on timeline length, while one common generator set pays for rank losses across
  all layers.
novelty_assessment: The secretary-to-prophet reduction, submodular rank telescoping and hyperplane-region
  counting are established. The selected candidate combination is the marked-pivot bound and its role
  in controlling adaptive residuals. Neither the full constant guarantee nor historical priority is certified
  here.
formalization_summary: MatroidProphet.lean states the 2^(-310) one-sample bound with only offline-optimum
  integrability and fully informed measurable arrival orders. MatroidSecretary.lean also states the fixed-vector
  expected minimum and adversarial-tail secretary bounds at 2^(-293). Prefix feasibility and finite seed
  laws are explicit. The scope documents and Comparator statements were compared; no Lean solution was
  built or kernel-checked. The auxiliary instruments are not separate certified Comparator results.
statement_faithfulness: The minimum over arrival orders must be inside the seed expectation. The sampling
  coordinates are mutually independent, with each sample matching its value law. A fixed seed mask may
  select coordinates but may not depend on their sampled values.
dependencies: Finite matroid rank and closure; greedy occurrence bases; fundamental circuits; strict hyperplane
  sign patterns; product-distribution gluing; one common generator set across a nested filtration.
antecedents: Azar, Kleinberg and Weinberg give the order-oblivious secretary-to-single-sample reduction.
  Greedy bases, rank submodularity and hyperplane arrangement bounds are classical ingredients.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# One-sample simulation, marked pivots and a shared rank budget

## Source manuscript and claim

[One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary](../papers/P-000111.md), by OpenAI, September 23, 2026.

The source claims a constant-competitive one-sample matroid prophet rule against an adversary that sees all samples, realized values and random bits, and an order-oblivious matroid secretary consequence.

## Extracted instruments

- [MI-000179: Sample/value gluing preserves an expected worst-order guarantee](../instruments/MI-000179.md)
- [MI-000180: Marked matroid pivots admit a timeline-independent pattern bound](../instruments/MI-000180.md)
- [MI-000181: One common generator set pays for all layered rank losses](../instruments/MI-000181.md)

## Dependencies and antecedents

Finite matroid rank and closure; greedy occurrence bases; fundamental circuits; strict hyperplane sign patterns; product-distribution gluing; one common generator set across a nested filtration.

Azar, Kleinberg and Weinberg give the order-oblivious secretary-to-single-sample reduction. Greedy bases, rank submodularity and hyperplane arrangement bounds are classical ingredients. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the simulation lemma, the entire marked-pivot proof and the common-generator rank accounting. The density-path construction, residual concentration and full competitive-ratio proof were not audited.

MatroidProphet.lean states the 2^(-310) one-sample bound with only offline-optimum integrability and fully informed measurable arrival orders. MatroidSecretary.lean also states the fixed-vector expected minimum and adversarial-tail secretary bounds at 2^(-293). Prefix feasibility and finite seed laws are explicit. The scope documents and Comparator statements were compared; no Lean solution was built or kernel-checked. The auxiliary instruments are not separate certified Comparator results.

The minimum over arrival orders must be inside the seed expectation. The sampling coordinates are mutually independent, with each sample matching its value law. A fixed seed mask may select coordinates but may not depend on their sampled values.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/111.md) · [Batch record](../../batches/B010/README.md)
