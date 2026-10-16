---
id: openai-math-343
record_type: family
title: Convex coordinate rearrangement and boundary-preserving area deformation
source_family: '343'
source_collection: openai/math
batch_id: B029
subject: Differential geometry
source_paper_ids:
- P-000189
instrument_ids:
- MI-000340
- MI-000341
headline: The source claims that closed symplectic balls in dimension 2n, n>=3, pack into the interior
  of a ball exactly under strict volume and pairwise capacity inequalities.
central_instrument: Coordinatewise increasing rearrangement preserves convexity on a downward polytope.
  Compactly supported area primitives and horizontal Moser fields preserve outer moment faces during deformation.
novelty_assessment: The global packing criterion was a conjecture in Siegel-Yao, distinct from their stabilized
  packing results. The extracted mechanisms use established rearrangement, compactly supported cohomology
  and Moser methods; their concrete boundary constraints are recorded without certifying the claimed packing
  theorem.
formalization_summary: Read both BallPacking.lean and BallPackingNecessity.lean, plus the scope. They
  use capacity pi times squared radius, positive capacities, embeddings on neighborhoods of closed balls,
  disjoint closed images in the open target, and strict volume and pairwise inequalities. The inspected
  Comparator contains a sorry target, not a proof built or kernel-checked here.
statement_faithfulness: The rearrangement domain has nonnegative face normals; that downward property
  is used to preserve previous coordinate monotonicity. The arithmetic rearrangement is separate from
  a Hamiltonian realization. Horizontal primitives are required for the moment-face preservation argument.
dependencies: Convex sublevel intervals, Fubini, relative primitives for zero-integral two-forms, exterior
  algebra and the Moser equation.
antecedents: Siegel-Yao, On Symplectic Packing Problems in Higher Dimensions, arXiv:2312.13224, for the
  conjectural context; classical rearrangement and Moser deformation methods.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Convex coordinate rearrangement and boundary-preserving area deformation

## Source manuscript and claim

[Symplectic Ball Packings in Higher Dimensions](../papers/P-000189.md), by OpenAI, None.

The source claims that closed symplectic balls in dimension 2n, n>=3, pack into the interior of a ball exactly under strict volume and pairwise capacity inequalities.

## Extracted instruments

- [MI-000340: Rearrange convex functions increasingly without losing convexity on a downward polytope](../instruments/MI-000340.md)
- [MI-000341: Construct relative area primitives and preserve moment faces in a Moser deformation](../instruments/MI-000341.md)

## Dependencies and antecedents

Convex sublevel intervals, Fubini, relative primitives for zero-integral two-forms, exterior algebra and the Moser equation.

Siegel-Yao, On Symplectic Packing Problems in Higher Dimensions, arXiv:2312.13224, for the conjectural context; classical rearrangement and Moser deformation methods. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete coordinate-rearrangement proof, relative-area primitive proof and Moser-with-outer-faces proof. Hamiltonian realization, fixed-point comparison, normal-cone transfer and higher-dimensional packing assembly were not audited.

Read both BallPacking.lean and BallPackingNecessity.lean, plus the scope. They use capacity pi times squared radius, positive capacities, embeddings on neighborhoods of closed balls, disjoint closed images in the open target, and strict volume and pairwise inequalities. The inspected Comparator contains a sorry target, not a proof built or kernel-checked here.

The rearrangement domain has nonnegative face normals; that downward property is used to preserve previous coordinate monotonicity. The arithmetic rearrangement is separate from a Hamiltonian realization. Horizontal primitives are required for the moment-face preservation argument.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/343.md) · [Batch record](../../batches/B029/README.md)
