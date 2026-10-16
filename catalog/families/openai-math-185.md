---
id: openai-math-185
record_type: family
title: Self-dual covering reductions and ordinal descent along a double ray
source_family: '185'
source_collection: openai/math
batch_id: B012
subject: Combinatorics
source_paper_ids:
- P-000122
instrument_ids:
- MI-000202
- MI-000203
headline: The source claims countable self-dual infinite matroids with neither an independent covering
  nor a packing/covering partition, and related failures of unrestricted intersection and individual covering
  and packing conjectures.
central_instrument: Self-duality turns a mixed packing/covering witness into an independent covering.
  A local basis interface propagates ultrafilter membership and strict ordinal decrease along one side
  of a double ray.
novelty_assessment: Restriction-contraction duality, direct sums and well-founded descent are established.
  The source-specific candidate is their local-to-global assembly. This batch treats the ultrafilter-ranked
  local matroid as an explicit input, not a verified construction.
formalization_summary: InfiniteMatroid.lean states a countable self-dual pair with no independent covering
  and no mixed partition. InfiniteMatroidCorollaries.lean adds a partitional description and intersection,
  individual covering and packing consequences. These are unrestricted infinite-matroid statements in
  a setting with Choice, not finitary statements. Scope documents and Comparator declarations were compared.
  No Lean solution was built or kernel-checked; the extracted auxiliary results are not separately certified
  targets.
statement_faithfulness: Self-duality is equality with the dual on the same labeled ground set. The ordinal
  descent needs strict decrease on every selected step; finite windows cannot certify an infinite counterexample.
dependencies: Infinite-matroid maximal extension and duality; restriction closure; countable direct sums;
  an ultrafilter; an antitone ordinal rank; basis extensions and well-foundedness.
antecedents: Bowler and Carmesin establish packing/covering and intersection equivalences. Bowler and
  Geschke construct self-dual uniform infinite matroids with additional set-theoretic hypotheses; that
  is background, not verification of the source local construction in ZFC.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Self-dual covering reductions and ordinal descent along a double ray

## Source manuscript and claim

[A Counterexample to the Infinite Matroid Packing/Covering Conjecture](../papers/P-000122.md), by OpenAI, September 24, 2026.

The source claims countable self-dual infinite matroids with neither an independent covering nor a packing/covering partition, and related failures of unrestricted intersection and individual covering and packing conjectures.

## Extracted instruments

- [MI-000202: Self-duality converts a mixed packing-covering witness into a full independent cover](../instruments/MI-000202.md)
- [MI-000203: A local ultrafilter rank interface excludes independent covers on a double ray](../instruments/MI-000203.md)

## Dependencies and antecedents

Infinite-matroid maximal extension and duality; restriction closure; countable direct sums; an ultrafilter; an antitone ordinal rank; basis extensions and well-foundedness.

Bowler and Carmesin establish packing/covering and intersection equivalences. Bowler and Geschke construct self-dual uniform infinite matroids with additional set-theoretic hypotheses; that is background, not verification of the source local construction in ZFC. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the self-dual reduction, closure facts and complete double-ray assembly proof. The filter, local-basis and preceding local-matroid construction were not audited; their stated interface is retained as a hypothesis.

InfiniteMatroid.lean states a countable self-dual pair with no independent covering and no mixed partition. InfiniteMatroidCorollaries.lean adds a partitional description and intersection, individual covering and packing consequences. These are unrestricted infinite-matroid statements in a setting with Choice, not finitary statements. Scope documents and Comparator declarations were compared. No Lean solution was built or kernel-checked; the extracted auxiliary results are not separately certified targets.

Self-duality is equality with the dual on the same labeled ground set. The ordinal descent needs strict decrease on every selected step; finite windows cannot certify an infinite counterexample.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/185.md) · [Batch record](../../batches/B012/README.md)
