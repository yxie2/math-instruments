---
id: openai-math-063
record_type: family
title: Alternating trace forms detect independent directions without semisimplicity
source_family: '063'
source_collection: openai/math
batch_id: B033
subject: Algebraic and complex geometry
source_paper_ids:
- P-000205
instrument_ids:
- MI-000372
- MI-000373
headline: The source claims the generalized Mukai inequality and its equality classification.
central_instrument: An alternating matrix-valued differential trace survives a parameter-dependent conjugation.
  A polynomial selector isolates one joint eigenvalue tuple and turns a nonzero wedge into independent
  graded operator directions.
novelty_assessment: The trace mechanism has Hochschild generalized-trace and inner-conjugation antecedents.
  No first-priority claim; the source spectral-production and geometric classification arguments remain
  unaudited.
formalization_summary: No formalization scope document is listed for this family in the pinned release
  inventory. No Lean build was performed.
statement_faithfulness: All A_j commute, A_0 commutes with them, the field has characteristic zero, and
  the differential is taken over C. A_0 need not commute with dA_j or be an idempotent.
dependencies: Kahler differentials, graded matrix products, simultaneous triangularization, polynomial
  interpolation on finitely many tuples and bounded gradings.
antecedents: Khalkhali, Very Basic Noncommutative Geometry, generalized trace and Lemma 4.1 on inner automorphisms;
  the manuscript supplies an elementary differential-form proof.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Alternating trace forms detect independent directions without semisimplicity

## Source manuscript and claim

[The generalized Mukai conjecture](../papers/P-000205.md), by OpenAI, September 24, 2026.

The source claims the generalized Mukai inequality and its equality classification.

## Extracted instruments

- [MI-000372: Remove derivatives of a moving triangular basis by alternating the trace](../instruments/MI-000372.md)
- [MI-000373: Select a joint eigenvalue wedge and force independent graded operator directions](../instruments/MI-000373.md)

## Dependencies and antecedents

Kahler differentials, graded matrix products, simultaneous triangularization, polynomial interpolation on finitely many tuples and bounded gradings.

Khalkhali, Very Basic Noncommutative Geometry, generalized trace and Lemma 4.1 on inner automorphisms; the manuscript supplies an elementary differential-form proof. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full alternating-trace, spectral-selector and independent-correspondence proofs and the quantum-operator setup. The argument producing an algebraically independent eigenvalue tuple and the descendant positivity argument were not audited.

No formalization scope document is listed for this family in the pinned release inventory. No Lean build was performed.

All A_j commute, A_0 commutes with them, the field has characteristic zero, and the differential is taken over C. A_0 need not commute with dA_j or be an idempotent.

[Batch record](../../batches/B033/README.md)
