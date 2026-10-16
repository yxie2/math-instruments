---
id: openai-math-124
record_type: family
title: Priority-list compression under local pruning and boundary capacity
source_family: '124'
source_collection: openai/math
batch_id: B035
subject: Theoretical computer science
source_paper_ids:
- P-000214
instrument_ids:
- MI-000390
- MI-000391
headline: The source claims a deterministic polynomial-time optimal algorithm for three-machine unit-job
  scheduling with arbitrary acyclic precedence constraints.
central_instrument: Suffix carries preserve global qualifier order; pruning preserves a specific one-sided
  comparison. Disjoint upward-closed injections are bounded by the capacity of a shared boundary slot.
novelty_assessment: Order filtering and injection into a finite witness set are elementary established
  tools. Their organization in the source scheduling hierarchy is recorded without certifying that hierarchy
  or the global algorithm.
formalization_summary: 'Read ThreeMachine.lean: one finite deterministic machine returns an optimal schedule
  or exact deadline answer on explicitly encoded acyclic instances, with polynomial bound exponent 150020.
  The target contains sorry; no Lean build was performed.'
statement_faithfulness: Priority keys use the largest membership index and a rank from a linear extension.
  Pruning comparison requires the first job to belong to the retained child set. The five-entry count
  holds after pruning; a temporary update can have six entries.
dependencies: Finite posets, upward-closed sets, lexicographic keys, disjointness and successor witnesses
  in a three-job boundary.
antecedents: Elementary order and finite-capacity arguments; no first-priority claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Priority-list compression under local pruning and boundary capacity

## Source manuscript and claim

[A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](../papers/P-000214.md), by OpenAI, None.

The source claims a deterministic polynomial-time optimal algorithm for three-machine unit-job scheduling with arbitrary acyclic precedence constraints.

## Extracted instruments

- [MI-000390: Preserve a global priority suffix while pruning only locally relevant list entries](../instruments/MI-000390.md)
- [MI-000391: Bound surviving upward-closed injections by a shared boundary slot](../instruments/MI-000391.md)

## Dependencies and antecedents

Finite posets, upward-closed sets, lexicographic keys, disjointness and successor witnesses in a three-job boundary.

Elementary order and finite-capacity arguments; no first-priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read suffix-carry, pruning, update-label and list-length proofs, with schedule/poset definitions. Global boundary invariants, history flattening and the structural hierarchy were not audited.

Read ThreeMachine.lean: one finite deterministic machine returns an optimal schedule or exact deadline answer on explicitly encoded acyclic instances, with polynomial bound exponent 150020. The target contains sorry; no Lean build was performed.

Priority keys use the largest membership index and a rank from a linear extension. Pruning comparison requires the first job to belong to the retained child set. The five-entry count holds after pruning; a temporary update can have six entries.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/124.md) · [Batch record](../../batches/B035/README.md)
