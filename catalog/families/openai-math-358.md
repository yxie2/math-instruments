---
id: openai-math-358
record_type: family
title: Torus shear obstructions and boundary-penalty duality
source_family: '358'
source_collection: openai/math
batch_id: B052
subject: Differential geometry
source_paper_ids:
- P-000290
instrument_ids:
- MI-000518
- MI-000519
headline: The source claims a closed smooth three-manifold with no conjugate points but no metric of nonpositive
  sectional curvature.
central_instrument: A torus shear conflicts with orthogonality forced by centralizer commutators. Optimizing
  a boundary penalty subtracts a rank-one term from a dual-energy bound.
novelty_assessment: The topology obstruction is explicitly classical Leeb/Kapovich-Leeb geometry. The
  penalty identity is Cauchy-Schwarz and a Schur-complement calculation; the source uses it in a uniform
  geodesic estimate.
formalization_summary: The target asserts a closed connected orientable smooth three-manifold with a smooth
  metric having no conjugate points for all geodesics and Jacobi fields, but no smooth nonpositive-sectional-curvature
  metric. The additional no-focal-points and CAT(0) consequences are outside the target. The scope document
  and linked Comparator were read in full. The target proof contains sorry; no solution or Lean project
  was built.
statement_faithfulness: The CAT(0) obstruction requires a proper cocompact action on a proper space and
  an embedded Z2 torus subgroup. The dual penalty uses mu>0 and an actual bound of the endpoint functional
  by the bulk energy.
dependencies: Amalgamated product injections, flat torus/minset structure and centralizer characters;
  Hilbert-space duality, Cauchy-Schwarz and quadratic minimization.
antecedents: Leeb two-piece graph-manifold incompatibility; classical minset splitting and rank-one inverse
  formulas.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Torus shear obstructions and boundary-penalty duality

## Source manuscripts and claim

- [A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric](../papers/P-000290.md): selected passages extracted.

The source claims a closed smooth three-manifold with no conjugate points but no metric of nonpositive sectional curvature.

## Extracted instruments

- [MI-000518: Obstruct nonpositive curvature by incompatible torus orthogonality](../instruments/MI-000518.md)
- [MI-000519: Optimize a boundary penalty in the dual energy norm](../instruments/MI-000519.md)

## Dependencies and antecedents

Amalgamated product injections, flat torus/minset structure and centralizer characters; Hilbert-space duality, Cauchy-Schwarz and quadratic minimization.

Leeb two-piece graph-manifold incompatibility; classical minset splitting and rank-one inverse formulas.

## Review and formalization scope

Read the full topology obstruction and its two corollaries, and the full turning-duality proof with its energy setup. The neck construction, returning-geodesic uniform bounds and global no-conjugate-points argument were not certified.

The target asserts a closed connected orientable smooth three-manifold with a smooth metric having no conjugate points for all geodesics and Jacobi fields, but no smooth nonpositive-sectional-curvature metric. The additional no-focal-points and CAT(0) consequences are outside the target. The scope document and linked Comparator were read in full. The target proof contains sorry; no solution or Lean project was built.

The CAT(0) obstruction requires a proper cocompact action on a proper space and an embedded Z2 torus subgroup. The dual penalty uses mu>0 and an actual bound of the endpoint functional by the bulk energy.

[Batch record](../../batches/B052/README.md)
