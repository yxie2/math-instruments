---
id: openai-math-335
record_type: family
title: Weighted graph identities and constraint-preserving rounding
source_family: '335'
source_collection: openai/math
batch_id: B084
subject: Differential geometry
source_paper_ids:
- P-000516
instrument_ids:
- MI-000778
- MI-000779
headline: The family claims a scalar-curvature integral bound for real simplicial volume and a rational-inessentiality
  companion.
central_instrument: Keep the full derivative term in a weighted graph identity; round all local coefficients
  in one common integer kernel.
novelty_assessment: Classical ingredients are identified; exact priority of the source-specific formulations
  is not established.
formalization_summary: No family scope is supplied; no Lean verification is claimed.
statement_faithfulness: The graph is smooth and the rounding starts with a finite profile encoding and
  bounded integer incidence rows. Neither setup is automatic from the algebra.
dependencies: Gauss and weighted Jacobi identities; finite-dimensional integer linear algebra and unbiased
  rounding.
antecedents: Weighted scalar curvature and classical lattice rounding in a rational linear subspace.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Weighted graph identities and constraint-preserving rounding

## Source manuscripts and claim

- [An integral scalar curvature bound for real simplicial volume](../papers/P-000516.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Positive scalar curvature forces rational inessentiality](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026)

The family claims a scalar-curvature integral bound for real simplicial volume and a rational-inessentiality companion.

## Extracted instruments

- [MI-000778: Preserve weighted volume while tracking a graph scalar-curvature defect](../instruments/MI-000778.md)
- [MI-000779: Round one coefficient vector inside all its integer constraints](../instruments/MI-000779.md)

## Dependencies and antecedents

Gauss and weighted Jacobi identities; finite-dimensional integer linear algebra and unbiased rounding.

Weighted scalar curvature and classical lattice rounding in a rational linear subspace.

## Review and formalization scope

Read the complete graph identity and joint-kernel rounding proof. The companion is inventory-only. The global curvature deformation and simplicial-volume theorem are not certified.

No family scope is supplied; no Lean verification is claimed.

The graph is smooth and the rounding starts with a finite profile encoding and bounded integer incidence rows. Neither setup is automatic from the algebra.

[Batch record](../../batches/B084/README.md)
