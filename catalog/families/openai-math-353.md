---
id: openai-math-353
record_type: family
title: Separated affine-maximal equations and a stationary cap identity
source_family: '353'
source_collection: openai/math
batch_id: B063
subject: Differential geometry
source_paper_ids:
- P-000377
- P-000378
instrument_ids:
- MI-000608
- MI-000609
headline: The sources claim a smooth nonquadratic entire affine-maximal graph in dimension ten and rigidity
  for Euclidean-complete graphs in dimensions three through nine.
central_instrument: A square-root ansatz separates a fourth-order equation into two second-order equations.
  A compact cap variation controls an inverse-Hessian weight.
novelty_assessment: The ansatz has the classical singular Trudinger-Wang example as a direct antecedent.
  Affine area and its stationarity are classical. Exact priority for the source general reduction and
  cap identity is unresolved.
formalization_summary: AffineBernstein covers smooth positive-Hessian graphs on nonempty open convex domains,
  complete in the induced Euclidean path metric, for dimensions 3 through 9. It concludes full domain
  and a positive-definite quadratic polynomial plus affine term, and an affine-image paraboloid description.
  It does not cover the smooth dimension-ten companion or the immersed-hypersurface extension. All three
  available scope documents and all three linked Comparators in this batch were read in full. Their target
  theorems have sorry proof bodies. No separate solution or Lean project was built.
statement_faithfulness: The reduction assumes positive F,P and positive Hessian of F. It does not itself
  prove global existence. The cap identity requires compactly supported restrictions of the test and its
  derivatives.
dependencies: Hessian block diagonalization, determinant weights, radial divergence form, divergence-free
  cofactors and affine-area first variation.
antecedents: Trudinger-Wang affine maximal equation and singular dimension-ten graph; Calabi affine area.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Separated affine-maximal equations and a stationary cap identity

## Source manuscripts and claim

- [A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten](../papers/P-000377.md): selected passages extracted.
- [The affine Bernstein theorem in dimensions three through nine](../papers/P-000378.md): selected passages extracted.

The sources claim a smooth nonquadratic entire affine-maximal graph in dimension ten and rigidity for Euclidean-complete graphs in dimensions three through nine.

## Extracted instruments

- [MI-000608: Separate the affine maximal equation with a square-root graph ansatz](../instruments/MI-000608.md)
- [MI-000609: Derive an inverse-Hessian cap identity from affine stationarity](../instruments/MI-000609.md)

## Dependencies and antecedents

Hessian block diagonalization, determinant weights, radial divergence form, divergence-free cofactors and affine-area first variation.

Trudinger-Wang affine maximal equation and singular dimension-ten graph; Calabi affine area.

## Review and formalization scope

Read the complete separated-variable reduction, radial divergence calculation, affine stationarity and cap-identity proofs. The invariant-box continuation and global Bernstein rigidity proofs remain unaudited.

AffineBernstein covers smooth positive-Hessian graphs on nonempty open convex domains, complete in the induced Euclidean path metric, for dimensions 3 through 9. It concludes full domain and a positive-definite quadratic polynomial plus affine term, and an affine-image paraboloid description. It does not cover the smooth dimension-ten companion or the immersed-hypersurface extension. All three available scope documents and all three linked Comparators in this batch were read in full. Their target theorems have sorry proof bodies. No separate solution or Lean project was built.

The reduction assumes positive F,P and positive Hessian of F. It does not itself prove global existence. The cap identity requires compactly supported restrictions of the test and its derivatives.

[Batch record](../../batches/B063/README.md)
