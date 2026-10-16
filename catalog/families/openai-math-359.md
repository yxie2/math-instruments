---
id: openai-math-359
record_type: family
title: A conditional bounded-coordinate obstruction and holomorphic Fourier extraction
source_family: '359'
source_collection: openai/math
batch_id: B063
subject: Differential geometry
source_paper_ids:
- P-000381
- P-000382
instrument_ids:
- MI-000612
- MI-000613
headline: The sources claim a negatively pinched Kahler threefold without bounded coordinates and a separate
  one-sided-curvature construction with the holomorphic Liouville property.
central_instrument: Cauchy estimates on a Hartogs zero section turn a nowhere-zero Jacobian into a forbidden
  pluriharmonic minorant. Root-of-unity averaging isolates homogeneous Taylor degrees with a uniform tail.
novelty_assessment: Both mechanisms use classical complex analysis. Exact priority for the source Hartogs
  obstruction interface was not established; root-of-unity filtering is classical finite Fourier orthogonality.
formalization_summary: PinchedKahler states existence of a nonempty contractible domain in C^3 with a
  complete negatively pinched Kahler metric and no bounded holomorphic coordinates. It separately targets
  a controlled no-minorant potential and the Hartogs metric transfer, with explicit chart Hessian and
  derivative bounds. It does not cover the one-sided-curvature Liouville companion. All three available
  scope documents and all three linked Comparators in this batch were read in full. Their target theorems
  have sorry proof bodies. No separate solution or Lean project was built.
statement_faithfulness: The Jacobian argument assumes a globally nowhere-zero determinant and a no-minorant
  potential. It does not imply all bounded holomorphic functions are constant. Fourier tails require h<N
  and a specified radial margin.
dependencies: Cauchy estimates, determinant expansion, holomorphic logarithms on a simply connected base,
  homogeneous Taylor series and geometric sums.
antecedents: Classical Cauchy and logarithm arguments; root-of-unity Fourier filters.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# A conditional bounded-coordinate obstruction and holomorphic Fourier extraction

## Source manuscripts and claim

- [A negatively pinched Kähler threefold without bounded holomorphic coordinates](../papers/P-000381.md): selected passages extracted.
- [One-sided negative sectional curvature and the holomorphic Liouville property](../papers/P-000382.md): selected passages extracted.

The sources claim a negatively pinched Kahler threefold without bounded coordinates and a separate one-sided-curvature construction with the holomorphic Liouville property.

## Extracted instruments

- [MI-000612: Turn bounded Hartogs coordinates into a forbidden holomorphic real-part bound](../instruments/MI-000612.md)
- [MI-000613: Extract one Taylor residue class with a root-of-unity filter](../instruments/MI-000613.md)

## Dependencies and antecedents

Cauchy estimates, determinant expansion, holomorphic logarithms on a simply connected base, homogeneous Taylor series and geometric sums.

Classical Cauchy and logarithm arguments; root-of-unity Fourier filters.

## Review and formalization scope

Read the complete bounded-map obstruction and the two geometric inputs it assumes, and the complete root-of-unity extraction lemma. Construction of the no-minorant potential, metric pinching, phase grids and the global Liouville example remain unaudited.

PinchedKahler states existence of a nonempty contractible domain in C^3 with a complete negatively pinched Kahler metric and no bounded holomorphic coordinates. It separately targets a controlled no-minorant potential and the Hartogs metric transfer, with explicit chart Hessian and derivative bounds. It does not cover the one-sided-curvature Liouville companion. All three available scope documents and all three linked Comparators in this batch were read in full. Their target theorems have sorry proof bodies. No separate solution or Lean project was built.

The Jacobian argument assumes a globally nowhere-zero determinant and a no-minorant potential. It does not imply all bounded holomorphic functions are constant. Fourier tails require h<N and a specified radial margin.

[Batch record](../../batches/B063/README.md)
