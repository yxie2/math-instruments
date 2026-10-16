---
id: openai-math-291
record_type: family
title: Covariance normalization and uniform tracial comparison
source_family: '291'
source_collection: openai/math
batch_id: B082
subject: Operator algebras
source_paper_ids:
- P-000509
instrument_ids:
- MI-000764
- MI-000765
headline: The family claims equivariant Jiang-Su stability and several related absorption results.
central_instrument: Normalize Gaussian quadratics by a covariance square root; obtain uniform trace estimates
  by compactness of finite covariance matrices rather than of extreme traces.
novelty_assessment: Classical mechanisms are credited. Novelty of the source-specific assembly is not
  established.
formalization_summary: The scope and selected UniformGamma definitions and complete main target were inspected;
  the long quotient and trace constructions were not read in full. That target concerns uniform Gamma
  from tracial real rank zero, not the selected equivariant absorption headline. It contains sorry; no
  separate solution or Lean build was checked.
statement_faithfulness: The covariance matrix may be singular and need not be invariant under translations.
  The ordered mixed-moment convergence is a separate source input.
dependencies: Powers-Stormer-type trace estimate, Gaussian characteristic functions, polynomial approximation,
  moment determinacy and Krein-Milman.
antecedents: Classical square-root trace continuity, method of moments and compactness-by-contradiction.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Covariance normalization and uniform tracial comparison

## Source manuscripts and claim

- [Equivariant Jiang–Su Stability for Amenable Actions in the Unital Stably Finite Case](../papers/P-000509.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Cuntz comparison and Jiang–Su absorption](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026)
- [Nuclear dimension and Jiang–Su stability without elementary subquotients](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026)
- [Tracial projection methods and uniform property Gamma](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026)

The family claims equivariant Jiang-Su stability and several related absorption results.

## Extracted instruments

- [MI-000764: Normalize Gaussian quadratics without a lower covariance eigenvalue bound](../instruments/MI-000764.md)
- [MI-000765: Upgrade sequential covariance limits to uniform trace estimates](../instruments/MI-000765.md)

## Dependencies and antecedents

Powers-Stormer-type trace estimate, Gaussian characteristic functions, polynomial approximation, moment determinacy and Krein-Milman.

Classical square-root trace continuity, method of moments and compactness-by-contradiction.

## Review and formalization scope

Read the entire Gaussian-quadratics section, including its uniformity proof. Three companions are inventory-only. The commuting-row construction, joint central limit input and absorption step are not certified.

The scope and selected UniformGamma definitions and complete main target were inspected; the long quotient and trace constructions were not read in full. That target concerns uniform Gamma from tracial real rank zero, not the selected equivariant absorption headline. It contains sorry; no separate solution or Lean build was checked.

The covariance matrix may be singular and need not be invariant under translations. The ordered mixed-moment convergence is a separate source input.

[Batch record](../../batches/B082/README.md)
