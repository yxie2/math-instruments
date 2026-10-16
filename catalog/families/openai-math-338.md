---
id: openai-math-338
record_type: family
title: Hermitian contact certificates and volume-preserving jet realization
source_family: '338'
source_collection: openai/math
batch_id: B038
subject: Differential geometry
source_paper_ids:
- P-000223
instrument_ids:
- MI-000408
- MI-000409
headline: The source claims uniformization of complete Kahler manifolds with positive holomorphic bisectional
  curvature.
central_instrument: A determinant-maximizing Hermitian form has a finite contact resolution. Divergence-free
  shear fields realize constant-volume jets by polynomial automorphisms with fixed-dimensional bounds.
novelty_assessment: The source explicitly attributes these mechanisms to John ellipsoid contacts and Andersen
  shear generation. The selected interfaces are classical adaptations, not independently new uniformization
  results.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build was performed.
statement_faithfulness: The logarithmic optimal value is lower semicontinuous; continuity of the optimizing
  matrix is not asserted. Jet degree is fixed before the uniform degree/coefficient bounds are chosen.
dependencies: Strict log-determinant concavity, finite-dimensional cone separation, divergence-free homogeneous
  vector fields and polynomial shear composition.
antecedents: John 1948; Andersen volume-preserving automorphisms; Forstneric-Larusson proof of Theorem
  3.1.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Hermitian contact certificates and volume-preserving jet realization

## Source manuscript and claim

[Uniformization of complete Kähler manifolds with positive bisectional curvature](../papers/P-000223.md), by OpenAI, None.

The source claims uniformization of complete Kahler manifolds with positive holomorphic bisectional curvature.

## Extracted instruments

- [MI-000408: Certify a Hermitian determinant optimum by finitely many contact directions](../instruments/MI-000408.md)
- [MI-000409: Realize a constant-volume finite jet by polynomial shears](../instruments/MI-000409.md)

## Dependencies and antecedents

Strict log-determinant concavity, finite-dimensional cone separation, divergence-free homogeneous vector fields and polynomial shear composition.

John 1948; Andersen volume-preserving automorphisms; Forstneric-Larusson proof of Theorem 3.1. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete optimizer/contact lemma and constant-volume jet realization proof. Disc envelopes, curvature-flow inequalities, dynamical basin estimates and global uniformization were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build was performed.

The logarithmic optimal value is lower semicontinuous; continuity of the optimizing matrix is not asserted. Jet degree is fixed before the uniform degree/coefficient bounds are chosen.

[Batch record](../../batches/B038/README.md)
