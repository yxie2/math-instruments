---
id: openai-math-025
record_type: family
title: Marked Egyptian-fraction prefixes and indexed exceptional-set descent
source_family: '025'
source_collection: openai/math
batch_id: B017
subject: Number theory
source_paper_ids:
- P-000142
instrument_ids:
- MI-000244
- MI-000245
headline: The source claims that the worst minimum number of distinct unit fractions for numerator 1<=a<b
  has order log log b, and gives counting and prescribed-denominator consequences.
central_instrument: A modified greedy prefix protects an exact prescribed denominator by making the remainder
  smaller than every reserved reciprocal. Indexed predecessor moments control exceptional sets through
  a logarithmic-depth residue descent.
novelty_assessment: Greedy Egyptian fractions, Holder inequalities and nonlinear recurrence unrolling
  are established. The marked prefix and quantitative descent are candidate interfaces. Exact-marker padding
  is expressly credited to van Doorn-Tang; the uniform short-expansion theorem is not certified by this
  extraction.
formalization_summary: The scope document and EgyptianFractions.lean and ShortEgyptianFractions.lean were
  read. They state the double-logarithmic length order, finite counting and denominator bounds, exact-marker
  padding and occurrence, and quantitative prescribed-denominator consequences. These are Comparator targets,
  not certified proof builds. No Lean solution was built or kernel-checked, and the auxiliary cards are
  not all separate formalization targets.
statement_faithfulness: The marked prefix keeps its numerator and denominator unreduced and skips the
  marker at most once. An odd divisibility marker is weaker than an exact denominator marker. Descent
  counts retain list indices even when divisor values repeat.
dependencies: Greedy rational subtraction, a protected remainder gap, known exact-marker padding, indexed
  bipartite counts, truncated divisor moments, Holder and a sublinear-power recurrence.
antecedents: Van Doorn-Tang, The smallest denominator not contained in a unit fraction decomposition of
  1 with fixed length, Lemma 2.1, supplies padding. The source credits Erdos's prime-factor splitting
  method for its separate divisor-moment input.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Marked Egyptian-fraction prefixes and indexed exceptional-set descent

## Source manuscript and claim

[Short Egyptian fractions](../papers/P-000142.md), by OpenAI, September 25, 2026.

The source claims that the worst minimum number of distinct unit fractions for numerator 1<=a<b has order log log b, and gives counting and prescribed-denominator consequences.

## Extracted instruments

- [MI-000244: A greedy prefix protects an exact Egyptian-fraction denominator](../instruments/MI-000244.md)
- [MI-000245: Indexed predecessor moments control exceptional sets through residue descent](../instruments/MI-000245.md)

## Dependencies and antecedents

Greedy rational subtraction, a protected remainder gap, known exact-marker padding, indexed bipartite counts, truncated divisor moments, Holder and a sublinear-power recurrence.

Van Doorn-Tang, The smallest denominator not contained in a unit fraction decomposition of 1 with fixed length, Lemma 2.1, supplies padding. The source credits Erdos's prime-factor splitting method for its separate divisor-moment input. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full marked-prefix and exact-padding proofs and the complete backward exceptional-set argument. The divisor-moment statement and dense-set reduction were inspected, but the divisor-moment proof, residue estimates and common auxiliary-denominator construction were not audited.

The scope document and EgyptianFractions.lean and ShortEgyptianFractions.lean were read. They state the double-logarithmic length order, finite counting and denominator bounds, exact-marker padding and occurrence, and quantitative prescribed-denominator consequences. These are Comparator targets, not certified proof builds. No Lean solution was built or kernel-checked, and the auxiliary cards are not all separate formalization targets.

The marked prefix keeps its numerator and denominator unreduced and skips the marker at most once. An odd divisibility marker is weaker than an exact denominator marker. Descent counts retain list indices even when divisor values repeat.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/025.md) · [Batch record](../../batches/B017/README.md)
