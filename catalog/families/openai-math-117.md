---
id: openai-math-117
record_type: family
title: Masked parity mixing and multiscale triangle repair
source_family: '117'
source_collection: openai/math
batch_id: B050
subject: Theoretical computer science
source_paper_ids:
- P-000275
- P-000276
instrument_ids:
- MI-000496
- MI-000497
headline: The sources claim constant-factor hardness and near-square-root-logarithmic integrality gaps
  for uniform sparsest cut.
central_instrument: Four interpolation masks combine a rank-one walk with a missing-two-permutations bound.
  A scale integral of Gaussian kernels repairs negative angles while preserving short chart distances.
novelty_assessment: Classical character diagonalization, interpolation and Schoenberg kernels are explicit
  cores. The precise combined interfaces are source arguments; no exhaustive historical priority claim.
formalization_summary: The supplied scope is an existential sequence of uniform sparsest-cut integrality
  gaps of order sqrt(log n)/(log log n)^3. It does not include the companion computational-hardness claim.
  The scope document and all linked Comparator definitions and targets were read. Their main target proofs
  contain sorry; no solution or Lean project was built.
statement_faithfulness: The mask argument uses characteristic two and four distinct times. Triangle repair
  requires a local defect bound and chartwise L1 distances; a global defect bound alone gives no short-distance
  guarantee.
dependencies: A quadratic-evaluation zero bound supplied by a pencil, finite-field characters and scalar-invariant
  directions; positive-definite Gaussian kernels and the triangle inequality for extended chart distances.
antecedents: Alon-Chung centered-indicator spectral estimates; Schoenberg Gaussian positive definiteness.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Masked parity mixing and multiscale triangle repair

## Source manuscripts and claim

- [Constant-factor hardness of uniform sparsest cut](../papers/P-000275.md): selected passages extracted.
- [Near-square-root logarithmic integrality gaps for uniform sparsest cut](../papers/P-000276.md): selected passages extracted.

The sources claim constant-factor hardness and near-square-root-logarithmic integrality gaps for uniform sparsest cut.

## Extracted instruments

- [MI-000496: Mix four parity positions by deleting only two mask permutations](../instruments/MI-000496.md)
- [MI-000497: Repair squared-distance triangles by integrating local Gaussian kernels](../instruments/MI-000497.md)

## Dependencies and antecedents

A quadratic-evaluation zero bound supplied by a pencil, finite-field characters and scalar-invariant directions; positive-definite Gaussian kernels and the triangle inequality for extended chart distances.

Alon-Chung centered-indicator spectral estimates; Schoenberg Gaussian positive definiteness.

## Review and formalization scope

Read the full matrix-walk and masked-pair lemmas, and the full companion triangle-repair proof. The evaluation-pencil construction, complete hardness reduction and gap construction remain unverified here.

The supplied scope is an existential sequence of uniform sparsest-cut integrality gaps of order sqrt(log n)/(log log n)^3. It does not include the companion computational-hardness claim. The scope document and all linked Comparator definitions and targets were read. Their main target proofs contain sorry; no solution or Lean project was built.

The mask argument uses characteristic two and four distinct times. Triangle repair requires a local defect bound and chartwise L1 distances; a global defect bound alone gives no short-distance guarantee.

[Batch record](../../batches/B050/README.md)
