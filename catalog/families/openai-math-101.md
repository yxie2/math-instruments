---
id: openai-math-101
record_type: family
title: Jacobian compatibility and cone transfer in sharp entropy geometry
source_family: '101'
source_collection: openai/math
batch_id: B003
subject: Convex and metric geometry
source_paper_ids:
- P-000089
instrument_ids:
- MI-000133
- MI-000134
headline: The source claims the sharp entropy lower bound for all log-concave densities and the simplex
  extremum for isotropic constants, with equality classifications. This extraction selects the local matrix-rigidity
  step and the established cone transfer.
central_instrument: The first two nonconstant terms of a nonlinear matrix Jacobian force commuting coefficients;
  exponential cone measures then transfer entropy equality to simplex geometry.
novelty_assessment: Local Jacobian compatibility is a candidate reusable algebraic step with priority
  unresolved. The cone construction and entropy–isotropic-constant reduction have explicit earlier sources
  and are catalogued as established tools.
formalization_summary: No family-specific formalization scope document is listed for family 101 in the
  pinned release inventory. No Lean proof or statement comparison is asserted for this paper.
statement_faithfulness: The local rigidity lemma assumes a linear symmetric matrix field with a sum-of-squares
  normalization. The cone transfer is conditional on the entropy bound; checking it does not prove the
  source’s global entropy theorem.
dependencies: Weak Jacobian compatibility, analytic matrix functional calculus, simultaneous diagonalization,
  Gaussian-to-exponential quantile transport, gamma moments and convex-cone geometry.
antecedents: Fradelizi–Marín Sola connect the entropy and simplex conjectures; the cone construction has
  earlier Fradelizi–Meyer and Klartag antecedents. Classical optimal transport underlies the source’s
  larger proof.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Jacobian compatibility and cone transfer in sharp entropy geometry

## Source manuscript and claim

[A sharp entropy bound and the simplex inequality for isotropic constants](../papers/P-000089.md), by OpenAI, October 5, 2026.

The source claims the sharp entropy lower bound for all log-concave densities and the simplex extremum for isotropic constants, with equality classifications. This extraction selects the local matrix-rigidity step and the established cone transfer.

## Extracted instruments

- [MI-000133: Nonlinear Jacobian compatibility forces a linear symmetric matrix field to commute](../instruments/MI-000133.md)
- [MI-000134: An exponential cone density transfers entropy gaps to isotropic-constant gaps](../instruments/MI-000134.md)

## Dependencies and antecedents

Weak Jacobian compatibility, analytic matrix functional calculus, simultaneous diagonalization, Gaussian-to-exponential quantile transport, gamma moments and convex-cone geometry.

Fradelizi–Marín Sola connect the entropy and simplex conjectures; the cone construction has earlier Fradelizi–Meyer and Klartag antecedents. Classical optimal transport underlies the source’s larger proof. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the rigidity and cone-transfer sections in full. Checked the coefficient cancellation forcing commutation, the covariance normalization and the exact cone constants. The global transport normalization, scalar certificates and sharp entropy inequality were not independently audited.

No family-specific formalization scope document is listed for family 101 in the pinned release inventory. No Lean proof or statement comparison is asserted for this paper.

The local rigidity lemma assumes a linear symmetric matrix field with a sum-of-squares normalization. The cone transfer is conditional on the entropy bound; checking it does not prove the source’s global entropy theorem.

[Batch record](../../batches/B003/README.md)
