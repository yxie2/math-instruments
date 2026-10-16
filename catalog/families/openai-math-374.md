---
id: openai-math-374
record_type: family
title: Cell moments, inverse-free energy testing and sharp transport instability
source_family: '374'
source_collection: openai/math
batch_id: B009
subject: Partial differential equations
source_paper_ids:
- P-000110
instrument_ids:
- MI-000176
- MI-000177
- MI-000178
headline: The source claims a uniform W2-to-L2 exponent one third for Brenier maps from the uniform measure
  on any fixed compact convex body with interior in dimension at least two, and sharpness on a fixed cube
  with three target atoms.
central_instrument: A midpoint coupling controls cell moment derivatives by mass derivatives. Testing
  the mass Laplacian in a specially chosen direction bounds intercept velocities without estimating its
  inverse. A thin tilted cell gives an explicit matching obstruction.
novelty_assessment: Brenier optimality, triangular rearrangement, displacement concavity, Laguerre-cell
  calculus and convex-gradient interpolation are established. The uniform cell-moment estimate, its dual
  energy use and the fixed-cube three-atom example are selected candidate source-specific contributions.
  Priority and the full Borel-target theorem are not independently certified.
formalization_summary: Brenier.lean states both target-uniform one-third stability, including existence
  and unique optimal plans, and failure of every larger exponent for exactly three positive atoms in a
  fixed cube, for each dimension at least two. The family scope and Comparator declarations were compared.
  No Lean solution was built or kernel-checked; the auxiliary cards are not separate Comparator targets.
statement_faithfulness: The source density is uniform on a convex body; the compact target container need
  not be convex. Constants may depend on that body and container but not atom count, masses or site separation.
  The finite cell estimates require positive masses and distinct interior-time sites. This is W2 stability,
  distinct from W1 estimates.
dependencies: Finite affine maximum potentials; positive-mass cell calculus and connected face Laplacian;
  triangular midpoint coupling; a quadratic concave test; weighted derivative norms; optimal-coupling
  monotonicity; convex-gradient interpolation and a separate finite-to-Borel limiting argument.
antecedents: Knothe and McCann supply the midpoint-coupling background, Kitagawa-Merigot-Thibert the cell
  Laplacian, and Delalande-Merigot convex-gradient interpolation. Letrouit gives instability examples
  on other source sets and formulates the convex-source square-root conjecture; its scope is compared
  directly.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Cell moments, inverse-free energy testing and sharp transport instability

## Source manuscript and claim

[Sharp One-Third Stability of Brenier Maps](../papers/P-000110.md), by OpenAI, None.

The source claims a uniform W2-to-L2 exponent one third for Brenier maps from the uniform measure on any fixed compact convex body with interior in dimension at least two, and sharpness on a fixed cube with three target atoms.

## Extracted instruments

- [MI-000176: A midpoint coupling controls first-moment derivatives by cell-mass derivatives](../instruments/MI-000176.md)
- [MI-000177: Test a mass Laplacian in its range to avoid an inverse-norm loss](../instruments/MI-000177.md)
- [MI-000178: A thin tilted cell separates transport-map movement from target movement](../instruments/MI-000178.md)

## Dependencies and antecedents

Finite affine maximum potentials; positive-mass cell calculus and connected face Laplacian; triangular midpoint coupling; a quadratic concave test; weighted derivative norms; optimal-coupling monotonicity; convex-gradient interpolation and a separate finite-to-Borel limiting argument.

Knothe and McCann supply the midpoint-coupling background, Kitagawa-Merigot-Thibert the cell Laplacian, and Delalande-Merigot convex-gradient interpolation. Letrouit gives instability examples on other source sets and formulates the convex-source square-root conjecture; its scope is compared directly. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full three-atom example, midpoint and moment proofs, cell differential and positive-mass arguments, fixed-mass path estimate and finite-target gradient interpolation. The final extension from finite to arbitrary Borel targets was not audited.

Brenier.lean states both target-uniform one-third stability, including existence and unique optimal plans, and failure of every larger exponent for exactly three positive atoms in a fixed cube, for each dimension at least two. The family scope and Comparator declarations were compared. No Lean solution was built or kernel-checked; the auxiliary cards are not separate Comparator targets.

The source density is uniform on a convex body; the compact target container need not be convex. Constants may depend on that body and container but not atom count, masses or site separation. The finite cell estimates require positive masses and distinct interior-time sites. This is W2 stability, distinct from W1 estimates.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/374.md) · [Batch record](../../batches/B009/README.md)
