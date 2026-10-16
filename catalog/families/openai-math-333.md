---
id: openai-math-333
record_type: family
title: Prescribe loop averages and transverse derivatives independently of amplitude
source_family: '333'
source_collection: openai/math
batch_id: B029
subject: Differential geometry
source_paper_ids:
- P-000187
instrument_ids:
- MI-000336
- MI-000337
headline: The source claims a smooth isometric immersion of every closed smooth Riemannian surface into
  Euclidean four-space, without an orientability assumption.
central_instrument: Positive densities prescribe the average of a loop while allowing smooth parameter
  patching. Thin transverse supports prescribe a large derivative along finitely intersecting curves while
  keeping the function small.
novelty_assessment: Convex barycentric weights, partitions of unity and localized jet extension are classical.
  The extracted lemmas package their parameter and support constraints for the source velocity-loop construction;
  no global immersion theorem is certified.
formalization_summary: Read SurfaceImmersion.lean and its scope. The target requires a compact smooth
  surface and a smooth map whose differential preserves the metric at every tangent space; it asks for
  an immersion, not an embedding. The inspected Comparator contains a sorry target, not a proof built
  or kernel-checked here.
statement_faithfulness: A target average must be in the two-dimensional interior of the path convex hull.
  The derivative lemma excludes shared curve arcs and requires only finitely many vertical tangencies
  and intersections near the compact set.
dependencies: Finite convex combinations, a right inverse for three linear constraints, smooth partitions
  of unity and transverse defining functions.
antecedents: Classical convex-hull and smooth extension constructions; no exhaustive priority claim established.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Prescribe loop averages and transverse derivatives independently of amplitude

## Source manuscript and claim

[Smooth isometric immersions of closed surfaces into Euclidean four-space](../papers/P-000187.md), by OpenAI, None.

The source claims a smooth isometric immersion of every closed smooth Riemannian surface into Euclidean four-space, without an orientability assumption.

## Extracted instruments

- [MI-000336: Prescribe the mean of a loop by a smoothly varying positive density](../instruments/MI-000336.md)
- [MI-000337: Prescribe a transverse derivative on curves while keeping the function uniformly small](../instruments/MI-000337.md)

## Dependencies and antecedents

Finite convex combinations, a right inverse for three linear constraints, smooth partitions of unity and transverse defining functions.

Classical convex-hull and smooth extension constructions; no exhaustive priority claim established. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete loop-density and small-value/prescribed-derivative proofs and their application to reparametrization. Primitive metric realization, preservation at crossings and exact smooth correction were not audited.

Read SurfaceImmersion.lean and its scope. The target requires a compact smooth surface and a smooth map whose differential preserves the metric at every tangent space; it asks for an immersion, not an embedding. The inspected Comparator contains a sorry target, not a proof built or kernel-checked here.

A target average must be in the two-dimensional interior of the path convex hull. The derivative lemma excludes shared curve arcs and requires only finitely many vertical tangencies and intersections near the compact set.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/333.md) · [Batch record](../../batches/B029/README.md)
