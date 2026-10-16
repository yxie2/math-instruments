---
id: openai-math-244
record_type: family
title: Local-to-global injection assembly and covariant selectors
source_family: '244'
source_collection: openai/math
batch_id: B021
subject: Mathematical logic
source_paper_ids:
- P-000157
instrument_ids:
- MI-000276
- MI-000277
headline: The source claims Con(ZF) implies Con(ZF plus the Partition Principle plus choice for ordinal-indexed
  families plus failure of Choice), together with a separate transitive-model construction.
central_instrument: Disjoint ordinal slices assemble local injections without choosing hidden presentations.
  A least distinguishing pattern chooses a group coset covariantly, provided all pattern objects live
  in one fixed wellordered ground set.
novelty_assessment: The ordinal slicing method is explicitly related to Ryan-Smith local reflections of
  choice. Least-pattern selection is an elementary equivariance mechanism. The model-specific detector,
  monoid, forcing and preservation inputs remain unaudited.
formalization_summary: Read the two selected targets and their relevant theory and ground-model definitions.
  PartitionConsistency uses syntactic consistency of full pure-set ZF and ordinal-indexed choice. PartitionPrinciple
  assumes an externally countable transitive ground satisfying its listed axioms and containing an internal
  strongly inaccessible cardinal; that is a separate construction target. These are target statements
  with sorry placeholders; no Lean solution was built or kernel-checked.
statement_faithfulness: A reverse injection need not be a section of the given surjection. Surjective
  presentations are not silently replaced by injective presentations. A selector needs injective patterns
  and unchanged wellordered pattern objects under transport.
dependencies: ZF separation and replacement, ordinal-indexed choice, quotient classification, countable
  detectors, eventual equality, regularity bounds and equivariant transport.
antecedents: Ryan-Smith, Local reflections of choice, Propositions 3.17 and 3.20; standard group actions
  and canonical least-code selection.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Local-to-global injection assembly and covariant selectors

## Source manuscript and claim

[The Partition Principle does not imply Choice](../papers/P-000157.md), by OpenAI, September 24, 2026.

The source claims Con(ZF) implies Con(ZF plus the Partition Principle plus choice for ordinal-indexed families plus failure of Choice), together with a separate transitive-model construction.

## Extracted instruments

- [MI-000276: Ordinal slices assemble reverse injections from a classified seed](../instruments/MI-000276.md)
- [MI-000277: Least separating patterns select a coset covariantly](../instruments/MI-000277.md)

## Dependencies and antecedents

ZF separation and replacement, ordinal-indexed choice, quotient classification, countable detectors, eventual equality, regularity bounds and equivariant transport.

Ryan-Smith, Local reflections of choice, Propositions 3.17 and 3.20; standard group actions and canonical least-code selection. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full all-set reduction and covariant coset-selector argument. The forcing construction, no-new-countable-sequences theorem, detector existence and consistency interpretation were not audited.

Read the two selected targets and their relevant theory and ground-model definitions. PartitionConsistency uses syntactic consistency of full pure-set ZF and ordinal-indexed choice. PartitionPrinciple assumes an externally countable transitive ground satisfying its listed axioms and containing an internal strongly inaccessible cardinal; that is a separate construction target. These are target statements with sorry placeholders; no Lean solution was built or kernel-checked.

A reverse injection need not be a section of the given surjection. Surjective presentations are not silently replaced by injective presentations. A selector needs injective patterns and unchanged wellordered pattern objects under transport.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/244.md) · [Batch record](../../batches/B021/README.md)
