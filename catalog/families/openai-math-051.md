---
id: openai-math-051
record_type: family
title: Boundary-unitary frames convert disc curvature into determinant and trace identities
source_family: '051'
source_collection: openai/math
batch_id: B033
subject: Algebraic and complex geometry
source_paper_ids:
- P-000204
instrument_ids:
- MI-000370
- MI-000371
headline: The source claims canonical ampleness for compact hyperbolic Kahler manifolds.
central_instrument: The determinant of a boundary-unitary frame records a Green-weighted Ricci integral.
  A Sobolev radial estimate permits a trace boundary limit without assuming boundary derivatives.
novelty_assessment: Green identities, determinant curvature and Sobolev trace estimates are classical.
  The selected boundary bookkeeping is reusable; the global ampleness conclusion is not certified.
formalization_summary: No formalization scope document is listed for this family in the pinned release
  inventory. No Lean build was performed.
statement_faithfulness: Assume the source holomorphic frame and centered variation have been constructed,
  with uniform positivity and W1,p regularity for p>2. Curvature has sign R_h=-ddc log det h.
dependencies: Holomorphic frames, Green identities, local potentials of closed (1,1)-forms, radial Sobolev
  estimates and finite-area integrability.
antecedents: Classical determinant curvature, planar Green formulas and Sobolev trace arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Boundary-unitary frames convert disc curvature into determinant and trace identities

## Source manuscript and claim

[Canonical ampleness of compact hyperbolic Kähler manifolds](../papers/P-000204.md), by OpenAI, September 23, 2026.

The source claims canonical ampleness for compact hyperbolic Kahler manifolds.

## Extracted instruments

- [MI-000370: Recover the central frame determinant from a Green-weighted Ricci integral](../instruments/MI-000370.md)
- [MI-000371: Pass from trace to log-determinant derivatives through a Sobolev boundary sequence](../instruments/MI-000371.md)

## Dependencies and antecedents

Holomorphic frames, Green identities, local potentials of closed (1,1)-forms, radial Sobolev estimates and finite-area integrability.

Classical determinant curvature, planar Green formulas and Sobolev trace arguments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the conventions and full determinant/trace Hessian proofs, including the nonsmooth boundary passage. Frame existence, the maximizing-disc construction and ampleness arguments were not audited.

No formalization scope document is listed for this family in the pinned release inventory. No Lean build was performed.

Assume the source holomorphic frame and centered variation have been constructed, with uniform positivity and W1,p regularity for p>2. Curvature has sign R_h=-ddc log det h.

[Batch record](../../batches/B033/README.md)
