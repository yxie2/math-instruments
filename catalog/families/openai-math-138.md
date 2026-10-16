---
id: openai-math-138
record_type: family
title: Subset-sum deficiency and prefix recomputation budgets
source_family: '138'
source_collection: openai/math
batch_id: B075
subject: Theoretical computer science
source_paper_ids:
- P-000471
- P-000472
instrument_ids:
- MI-000702
- MI-000703
headline: The family claims faster worst-case Subset Sum algorithms, including a low-space implementation.
central_instrument: Support deficiency has bounded changes under sampling; prefix recomputation can be
  charged separately to distinct entries and raw occurrences.
novelty_assessment: Selected local mechanisms are distinguished from the manuscripts headline claims.
  Primary comparisons identify established antecedents; exhaustive priority is not established.
formalization_summary: The pinned inventory has no family scope document or linked Comparator for this
  family. No formal verification is claimed.
statement_faithfulness: The support argument permits arbitrary integer weights. Prefix accounting requires
  filtering incompatible masks before tuple generation and retains duplicate and invalid occurrence identities.
dependencies: Finite sumsets, sampling without replacement, martingale differences and binary prefix trees.
antecedents: Classical support compression, bounded differences and output-sensitive enumeration.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Subset-sum deficiency and prefix recomputation budgets

## Source manuscripts and claim

- [Subset Sum in Time $`O(2^{0.49n})`$ ](../papers/P-000471.md): selected passages extracted.
- [A Low-Space Algorithm for Worst-Case Subset Sum](../papers/P-000472.md): selected passages extracted.

The family claims faster worst-case Subset Sum algorithms, including a low-space implementation.

## Extracted instruments

- [MI-000702: Measure subset-sum compression by a bounded-difference deficiency](../instruments/MI-000702.md)
- [MI-000703: Separate task starts, raw matches and reused arrays in prefix recomputation](../instruments/MI-000703.md)

## Dependencies and antecedents

Finite sumsets, sampling without replacement, martingale differences and binary prefix trees.

Classical support compression, bounded differences and output-sensitive enumeration.

## Review and formalization scope

Read the complete deficiency and random-restriction proofs, and the parent schedule, validity proof and full prefix-accounting proof. Both manuscripts receive extractions. Filtering moments, modular recovery and the claimed running-time exponents are not certified.

The pinned inventory has no family scope document or linked Comparator for this family. No formal verification is claimed.

The support argument permits arbitrary integer weights. Prefix accounting requires filtering incompatible masks before tuple generation and retains duplicate and invalid occurrence identities.

[Batch record](../../batches/B075/README.md)
