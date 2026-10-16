---
id: openai-math-262
record_type: family
title: Fixed matrix channels, trace defects and Gaussian conjugation averages
source_family: '262'
source_collection: openai/math
batch_id: B055
subject: Mathematical physics
source_paper_ids:
- P-000306
- P-000307
- P-000308
instrument_ids:
- MI-000537
- MI-000538
- MI-000539
headline: The sources claim sharp scalar and finite-matrix one-dimensional Lieb-Thirring constants for
  1/2<gamma<3/2, with all matrix equality cases classified.
central_instrument: Differential inequalities fix row spaces before an auxiliary matrix is chosen measurably.
  A Hilbert-Schmidt square retains the noncommutative trace defect. An integrated tangent kernel is a
  probability average of conjugations.
novelty_assessment: Gronwall, matrix Riccati equations, divided differences, Gaussian mixtures and trace
  duality have classical antecedents. The exact source assembly and equality classification are not certified
  by these selected checks.
formalization_summary: The inspected Comparator states only the scalar nonnegative-potential inequality,
  the full unlimited negative-eigenvalue moment, both optimal constants and attainment at the explicit
  scalar profile. Its target proof contains sorry. It does not state the finite-matrix extension or classification
  of every matrix equality case. The scope document and every linked Comparator were read in full. No
  solution or Lean project was built.
statement_faithfulness: Channel rigidity is conditional on the source pointwise equality relations. The
  integrated comparison assumes uniform positivity of the complete symbol and N>=0, not positivity of
  the perturbation alone. Gaussian averaging requires 0<sigma<1.
dependencies: Absolute continuity, Gronwall, orthogonal projections, matrix ODE uniqueness; half-line
  boundary maps, resolvent integrals, trace squares and scalar power duality; gamma and Gaussian probability
  mixtures.
antecedents: Benguria-Loss matrix Riccati method; Daleckii-Krein functional-calculus derivatives as stated
  by Hiai; classical positive-definite Gaussian kernels.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Fixed matrix channels, trace defects and Gaussian conjugation averages

## Source manuscripts and claim

- [Equality cases in the sharp one-dimensional matrix Lieb–Thirring inequality](../papers/P-000306.md): selected passages extracted.
- [Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials](../papers/P-000307.md): selected passages extracted.
- [Sharp one-dimensional Lieb–Thirring constants](../papers/P-000308.md): selected passages extracted.

The sources claim sharp scalar and finite-matrix one-dimensional Lieb-Thirring constants for 1/2<gamma<3/2, with all matrix equality cases classified.

## Extracted instruments

- [MI-000537: Fix matrix channels before choosing a regular auxiliary coefficient](../instruments/MI-000537.md)
- [MI-000538: Retain a noncommutative square in integrated trace duality](../instruments/MI-000538.md)
- [MI-000539: Recognize an integrated divided-difference kernel as random unitary conjugation](../instruments/MI-000539.md)

## Dependencies and antecedents

Absolute continuity, Gronwall, orthogonal projections, matrix ODE uniqueness; half-line boundary maps, resolvent integrals, trace squares and scalar power duality; gamma and Gaussian probability mixtures.

Benguria-Loss matrix Riccati method; Daleckii-Krein functional-calculus derivatives as stated by Hiai; classical positive-definite Gaussian kernels.

## Review and formalization scope

Read both fixed-subspace proofs and the Riccati profile step, the complete integrated trace comparison, and the complete rank-one comparison including its Gaussian mixture. The earlier compactness-to-equality passage, matrix-field path construction and full spectral inequalities remain unverified.

The inspected Comparator states only the scalar nonnegative-potential inequality, the full unlimited negative-eigenvalue moment, both optimal constants and attainment at the explicit scalar profile. Its target proof contains sorry. It does not state the finite-matrix extension or classification of every matrix equality case. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

Channel rigidity is conditional on the source pointwise equality relations. The integrated comparison assumes uniform positivity of the complete symbol and N>=0, not positivity of the perturbation alone. Gaussian averaging requires 0<sigma<1.

[Batch record](../../batches/B055/README.md)
