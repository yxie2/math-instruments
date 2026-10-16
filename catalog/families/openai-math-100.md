---
id: openai-math-100
record_type: family
title: Sheared square coverings and simplex chords
source_family: '100'
source_collection: openai/math
batch_id: B073
subject: Convex and metric geometry
source_paper_ids:
- P-000457
- P-000458
instrument_ids:
- MI-000688
- MI-000689
headline: The family claims finite cylinder approximations of ruled and radial swept sets.
central_instrument: Monotone rounding produces full square coverings under strong shear; simplex intersections
  determine projection area from the longest chord.
novelty_assessment: Directly checked antecedents are identified below. No exhaustive novelty determination
  or certification of a source headline is claimed.
formalization_summary: Read the scope and complete RuledCovering Comparator, including its hyperbolic,
  physical, logarithmic-cell, product, orthogonal-grid, nilpotent and singular statements. The other listed
  covering Comparators were not inspected. Inspected Comparator target bodies contain sorry; no separate
  solution or Lean build was checked.
statement_faithfulness: Square covering requires 0<=alpha beta<1, not separate bounds on the shears. The
  projection identity is for a full-dimensional simplex, not an arbitrary convex body.
dependencies: Integer monotone maps, trace-zero planar matrices, barycentric coordinates and layer-cake
  integration.
antecedents: Lattice fixed-point arguments and the established Martini-Weissbach simplex identity.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Sheared square coverings and simplex chords

## Source manuscripts and claim

- [Finite cylinder approximation of ruled sets](../papers/P-000457.md): selected passages extracted.
- [Finite triangular approximation of radial sweeps](../papers/P-000458.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Finite angular cylinder covers below the half-area bound](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026)
- [Slope-field perturbations of the two-cylinder covering](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026)

The family claims finite cylinder approximations of ruled and radial swept sets.

## Extracted instruments

- [MI-000688: Cover the plane by squares centered on a strongly sheared lattice](../instruments/MI-000688.md)
- [MI-000689: Compute simplex shadow area from its longest parallel chord](../instruments/MI-000689.md)

## Dependencies and antecedents

Integer monotone maps, trace-zero planar matrices, barycentric coordinates and layer-cake integration.

Lattice fixed-point arguments and the established Martini-Weissbach simplex identity.

## Review and formalization scope

Read the full lattice-covering, zero-diagonal-basis and affine-cover proofs, and the full simplex projection proof. Two of four manuscripts receive extractions; the angular-cover and slope-field manuscripts remain inventory-only. Nonlinear localization and full swept-set covering results are not certified.

Read the scope and complete RuledCovering Comparator, including its hyperbolic, physical, logarithmic-cell, product, orthogonal-grid, nilpotent and singular statements. The other listed covering Comparators were not inspected. Inspected Comparator target bodies contain sorry; no separate solution or Lean build was checked.

Square covering requires 0<=alpha beta<1, not separate bounds on the shears. The projection identity is for a full-dimensional simplex, not an arbitrary convex body.

[Batch record](../../batches/B073/README.md)
