---
id: openai-math-142
record_type: family
title: Dynamic evaluation and extraction of norms from idempotents
source_family: '142'
source_collection: openai/math
batch_id: B040
subject: Theoretical computer science
source_paper_ids:
- P-000234
instrument_ids:
- MI-000430
- MI-000431
headline: The source claims deterministic polynomial-time factorization over prime fields.
central_instrument: A divergent field branch becomes a factor in a product algebra. A supplied rank-one
  idempotent in a split cyclic algebra yields a norm solution by linear algebra.
novelty_assessment: Dynamic evaluation is explicitly classical. The idempotent-to-norm step is standard
  cyclic-algebra linear algebra; obtaining the idempotent is the separate difficult input.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: The simultaneous-execution input polynomial is square-free and split over the
  prime field. The norm extraction assumes a cyclic field extension and a supplied rank-one idempotent
  in the split algebra.
dependencies: Gcds, extended Euclidean inversion, product algebras, cyclic algebras and finite-dimensional
  linear systems.
antecedents: Della Dora-Dicrescenzo-Duval dynamic evaluation; classical cyclic-algebra norm criterion.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Dynamic evaluation and extraction of norms from idempotents

## Source manuscript and claim

[Deterministic Polynomial Factorization over Prime Fields](../papers/P-000234.md), by OpenAI, October 4, 2026.

The source claims deterministic polynomial-time factorization over prime fields.

## Extracted instruments

- [MI-000430: Turn divergent field decisions into polynomial factors](../instruments/MI-000430.md)
- [MI-000431: Extract a cyclic norm solution from a supplied rank-one idempotent](../instruments/MI-000431.md)

## Dependencies and antecedents

Gcds, extended Euclidean inversion, product algebras, cyclic algebras and finite-dimensional linear systems.

Della Dora-Dicrescenzo-Duval dynamic evaluation; classical cyclic-algebra norm criterion. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete simultaneous-execution proof and complete idempotent-to-norm proof with its cyclic-algebra setup. Root extraction, idempotent construction, geometric separation and global complexity were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

The simultaneous-execution input polynomial is square-free and split over the prime field. The norm extraction assumes a cyclic field extension and a supplied rank-one idempotent in the split algebra.

[Batch record](../../batches/B040/README.md)
