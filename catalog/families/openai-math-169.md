---
id: openai-math-169
record_type: family
title: Insertion coordinates and commuting graph alphabets
source_family: '169'
source_collection: openai/math
batch_id: B044
subject: Combinatorics
source_paper_ids:
- P-000248
instrument_ids:
- MI-000458
- MI-000459
headline: The source claims elementary positivity of chromatic quasisymmetric functions for natural unit
  interval graphs.
central_instrument: Largest-letter insertion gives independent inversion digits. A two-color path involution
  proves quantum-torus independent-set sums commute.
novelty_assessment: The commutation proof explicitly adapts Shareshian-Wachs Lemma 4.4 and Theorem 4.5.
  These preliminary graph tools do not establish the later positivity claim.
formalization_summary: Read ElementaryPositivity.lean in full and the scope document. elementaryPositivityWitness
  contains sorry and asks for a permutation-indexed expansion over N[q] for every finite color alphabet.
  No Lean build.
statement_faithfulness: The graph must be a natural unit interval graph, not an arbitrary graph. Commuting
  positive elementary generators do not imply positive monomial evaluations.
dependencies: Monotone extensive endpoint functions, inversion counts, ordered bipartite path components
  and skew quantum-torus weights.
antecedents: Shareshian-Wachs, Chromatic quasisymmetric functions, Lemma 4.4 and Theorem 4.5; noncommutative
  poset symmetric functions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Insertion coordinates and commuting graph alphabets

## Source manuscript and claim

[Elementary positivity of chromatic quasisymmetric functions](../papers/P-000248.md), by OpenAI, September 24, 2026.

The source claims elementary positivity of chromatic quasisymmetric functions for natural unit interval graphs.

## Extracted instruments

- [MI-000458: Encode admissible permutations by independent inversion digits](../instruments/MI-000458.md)
- [MI-000459: Prove graph-alphabet commutation by switching odd path components](../instruments/MI-000459.md)

## Dependencies and antecedents

Monotone extensive endpoint functions, inversion counts, ordered bipartite path components and skew quantum-torus weights.

Shareshian-Wachs, Chromatic quasisymmetric functions, Lemma 4.4 and Theorem 4.5; noncommutative poset symmetric functions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete graph-alphabet section. Compared the two-color antecedent directly. The wall recursion, triangle construction and positivity witness were not audited.

Read ElementaryPositivity.lean in full and the scope document. elementaryPositivityWitness contains sorry and asks for a permutation-indexed expansion over N[q] for every finite color alphabet. No Lean build.

The graph must be a natural unit interval graph, not an arbitrary graph. Commuting positive elementary generators do not imply positive monomial evaluations.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/169.md) · [Batch record](../../batches/B044/README.md)
