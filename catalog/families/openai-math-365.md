---
id: openai-math-365
record_type: family
title: Uniform harmonic jet frames and radius-aware interpolation
source_family: '365'
source_collection: openai/math
batch_id: B086
subject: Partial differential equations
source_paper_ids:
- P-000525
instrument_ids:
- MI-000796
- MI-000797
headline: The family studies boundary determination of metrics and connections and scalar-conductivity
  nonuniqueness.
central_instrument: Use a finite family of affine and quadratic limiting jets to obtain a uniform right
  inverse; convert weighted L2 moments to derivative bounds without differentiating the radius.
novelty_assessment: Classical ingredients are distinguished from source-specific uses. Exact priority
  of the extracted formulations is not established.
formalization_summary: Read the full scope and Conductivity Comparator. They concern bounded measurable
  scalar-conductivity nonuniqueness, not the selected smooth metric/connection recovery manuscript. The
  target has sorry; no separate solution or Lean build was checked.
statement_faithfulness: The selected harmonic columns and their smooth scaled limits are inputs. Interpolation
  uses uniform high derivatives and a Lipschitz fractional power of the radius.
dependencies: Finite-dimensional right inverses, compactness, Taylor expansion and polynomial norm equivalence.
antecedents: Classical stable spanning and local interpolation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Uniform harmonic jet frames and radius-aware interpolation

## Source manuscripts and claim

- [Determination of a metric and a unitary connection from one boundary patch](../papers/P-000525.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Smooth anisotropic uniqueness in the Calderón problem from one boundary patch](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026)
- [Nonuniqueness for bounded measurable scalar conductivities in three dimensions](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026)

The family studies boundary determination of metrics and connections and scalar-conductivity nonuniqueness.

## Extracted instruments

- [MI-000796: Stabilize a finite family of harmonic jets by a smooth right inverse](../instruments/MI-000796.md)
- [MI-000797: Convert weighted moments into derivative bounds on a comparable-radius ball](../instruments/MI-000797.md)

## Dependencies and antecedents

Finite-dimensional right inverses, compactness, Taylor expansion and polynomial norm equivalence.

Classical stable spanning and local interpolation.

## Review and formalization scope

Read complete jet-spanning and pointwise-interpolation proofs, including their scaled-column setup. Two companions are inventory-only. The construction of harmonic columns, transfer density and inverse-boundary theorem are not certified.

Read the full scope and Conductivity Comparator. They concern bounded measurable scalar-conductivity nonuniqueness, not the selected smooth metric/connection recovery manuscript. The target has sorry; no separate solution or Lean build was checked.

The selected harmonic columns and their smooth scaled limits are inputs. Interpolation uses uniform high derivatives and a Lipschitz fractional power of the radius.

[Batch record](../../batches/B086/README.md)
