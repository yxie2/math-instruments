---
id: openai-math-348
record_type: family
title: Inverse-weight variance and exact polynomial certificates
source_family: '348'
source_collection: openai/math
batch_id: B085
subject: Differential geometry
source_paper_ids:
- P-000520
instrument_ids:
- MI-000786
- MI-000787
headline: The family claims rigidity and classification of Einstein four-manifolds under curvature assumptions.
central_instrument: Dualize a strengthened Laplacian estimate into weighted variance; certify polynomial
  and matrix signs through Bernstein coefficients.
novelty_assessment: Classical mechanisms are identified explicitly; exact priority of source-specific
  interfaces is not established.
formalization_summary: Read the scope and selected EinsteinFour definitions (1-45) and target/classification
  portion (151-222). The intermediate coordinate curvature definitions were not read in full. Its strictly
  positive-curvature target differs from the selected nonnegative-curvature boundary argument. Targets
  have sorry; no separate solution or Lean build was checked.
statement_faithfulness: The inverse-weight variance conclusion is conditional on the full differential
  estimate. Nonnegative Bernstein coefficients are sufficient, not necessary, at a fixed degree.
dependencies: Poisson solvability, integration by parts, weighted Cauchy-Schwarz and nonnegative polynomial
  partitions of unity.
antecedents: Classical Poisson duality and Bernstein positivity certificates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Inverse-weight variance and exact polynomial certificates

## Source manuscripts and claim

- [Zero-Plane Rigidity for Einstein Four-Manifolds](../papers/P-000520.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [An L² Einstein Gap for Nonnegatively Curved Four-Manifolds](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026)
- [Positively curved Einstein four-manifolds](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Positively-curved-Einstein-four-manifolds-September-23-2026)

The family claims rigidity and classification of Einstein four-manifolds under curvature assumptions.

## Extracted instruments

- [MI-000786: Turn a weighted Laplacian estimate into an inverse-weight variance bound](../instruments/MI-000786.md)
- [MI-000787: Certify scalar and matrix polynomial signs by normalized Bernstein coefficients](../instruments/MI-000787.md)

## Dependencies and antecedents

Poisson solvability, integration by parts, weighted Cauchy-Schwarz and nonnegative polynomial partitions of unity.

Classical Poisson duality and Bernstein positivity certificates.

## Review and formalization scope

Read complete weighted-variance and Bernstein-conversion proofs, with the curvature-block notation. Two companions are inventory-only. The full geometric contraction chain and the large source-specific certificate tables were not independently verified.

Read the scope and selected EinsteinFour definitions (1-45) and target/classification portion (151-222). The intermediate coordinate curvature definitions were not read in full. Its strictly positive-curvature target differs from the selected nonnegative-curvature boundary argument. Targets have sorry; no separate solution or Lean build was checked.

The inverse-weight variance conclusion is conditional on the full differential estimate. Nonnegative Bernstein coefficients are sufficient, not necessary, at a fixed degree.

[Batch record](../../batches/B085/README.md)
