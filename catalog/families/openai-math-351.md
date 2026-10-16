---
id: openai-math-351
record_type: family
title: Evolving-radius derivatives and heat perturbation estimates
source_family: '351'
source_collection: openai/math
batch_id: B086
subject: Differential geometry
source_paper_ids:
- P-000522
instrument_ids:
- MI-000790
- MI-000791
headline: The family studies bounded scalar curvature and finite-time Ricci-flow curvature blowup, with
  four-dimensional and degenerating-tree companions.
central_instrument: Retain the evolving-arclength commutator before applying a slope maximum principle;
  absorb a small principal-coefficient perturbation without differentiating it.
novelty_assessment: Classical ingredients are distinguished from source-specific uses. Exact priority
  of the extracted formulations is not established.
formalization_summary: No family scope is supplied; no Lean verification is claimed.
statement_faithfulness: Smoothness on compact time slabs and pole data are required for the slope argument.
  The heat estimate assumes a uniformly small deviation from its constant principal coefficient.
dependencies: Doubly warped curvature formulas, maximum principles, parabolic Lp estimates, interpolation
  and embedding.
antecedents: Classical warped Ricci-flow equations and perturbative parabolic regularity.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Evolving-radius derivatives and heat perturbation estimates

## Source manuscripts and claim

- [A closed Ricci flow with bounded scalar curvature and finite-time curvature blowup](../papers/P-000522.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Bounded scalar curvature and smooth extension of four-dimensional Ricci flow](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026)
- [Path selection and an elliptic inequality on degenerating Ricci-flat trees](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026)

The family studies bounded scalar curvature and finite-time Ricci-flow curvature blowup, with four-dimensional and degenerating-tree companions.

## Extracted instruments

- [MI-000790: Keep the arclength commutator when deriving a warping-slope barrier](../instruments/MI-000790.md)
- [MI-000791: Absorb a small heat-operator perturbation without coefficient derivatives](../instruments/MI-000791.md)

## Dependencies and antecedents

Doubly warped curvature formulas, maximum principles, parabolic Lp estimates, interpolation and embedding.

Classical warped Ricci-flow equations and perturbative parabolic regularity.

## Review and formalization scope

Read the complete elementary slope-bound and heat-perturbation proofs, including the fixed-point/fixed-radius distinction. Two companions are inventory-only. The global flow construction and bounded-scalar-curvature blowup claim are not certified.

No family scope is supplied; no Lean verification is claimed.

Smoothness on compact time slabs and pole data are required for the slope argument. The heat estimate assumes a uniformly small deviation from its constant principal coefficient.

[Batch record](../../batches/B086/README.md)
