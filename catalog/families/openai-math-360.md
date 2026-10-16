---
id: openai-math-360
record_type: family
title: Globalizing local injectivity and restoring a missing determinant direction
source_family: '360'
source_collection: openai/math
batch_id: B053
subject: Differential geometry
source_paper_ids:
- P-000293
- P-000294
instrument_ids:
- MI-000524
- MI-000525
headline: The sources claim convex injectivity domains and uniform bi-Holder optimal transport under weak
  MTW curvature.
central_instrument: Local injectivity plus a homotopy to a homeomorphism gives a global homeomorphism
  on closed connected manifolds. An oblique projection exposes the precise rank-one determinant gain.
novelty_assessment: The globalization is classical covering-space theory. The determinant estimate is
  elementary Schur-complement algebra applied to the source limiting configuration.
formalization_summary: The linked global-support Comparator states convexity of open tangent injectivity
  domains under weak MTW; the scope document reports additional support and finite-target results that
  are not separate theorems in that inspected Comparator. The transport target has one exponent and constant
  for bounded positive densities on each fixed manifold, with almost-everywhere uniqueness. Both target
  proofs contain sorry. The scope document and every linked Comparator were read in full. No solution
  or Lean project was built.
statement_faithfulness: The topology step needs compact boundaryless manifolds of the same dimension and
  an induced surjection on fundamental groups. The matrix step assumes positive definiteness and all stated
  transverse domination hypotheses.
dependencies: Invariance of domain, compactness and covering-space lifting; Loewner order, oblique projection
  and Schur complements.
antecedents: Hatcher covering-space index and lifting results; classical determinant identities.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Globalizing local injectivity and restoring a missing determinant direction

## Source manuscripts and claim

- [Global Support and Convex Injectivity Domains under Weak MTW](../papers/P-000293.md): selected passages extracted.
- [Uniform Bi-Holder Transport from Weak MTW](../papers/P-000294.md): selected passages extracted.

The sources claim convex injectivity domains and uniform bi-Holder optimal transport under weak MTW curvature.

## Extracted instruments

- [MI-000524: Globalize a locally injective map through its homotopy class](../instruments/MI-000524.md)
- [MI-000525: Recover the missing determinant direction after an oblique projection](../instruments/MI-000525.md)

## Dependencies and antecedents

Invariance of domain, compactness and covering-space lifting; Loewner order, oblique projection and Schur complements.

Hatcher covering-space index and lifting results; classical determinant identities.

## Review and formalization scope

Read the complete covering-homeomorphism proof and the complete oblique-projection determinant proof, with the latter configuration assumptions. The preceding local-injectivity proof and limiting matrix construction were not certified.

The linked global-support Comparator states convexity of open tangent injectivity domains under weak MTW; the scope document reports additional support and finite-target results that are not separate theorems in that inspected Comparator. The transport target has one exponent and constant for bounded positive densities on each fixed manifold, with almost-everywhere uniqueness. Both target proofs contain sorry. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

The topology step needs compact boundaryless manifolds of the same dimension and an induced surjection on fundamental groups. The matrix step assumes positive definiteness and all stated transverse domination hypotheses.

[Batch record](../../batches/B053/README.md)
