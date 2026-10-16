---
id: openai-math-099
record_type: family
title: Alphabet compression and finite partition histograms
source_family: 099
source_collection: openai/math
batch_id: B073
subject: Convex and metric geometry
source_paper_ids:
- P-000455
- P-000456
instrument_ids:
- MI-000686
- MI-000687
headline: The family claims matching exponential-order bounds for embedding edit distance into l1.
central_instrument: Pairwise collision control removes alphabet size; independent cuts turn an l1 metric
  into an exact exponential collision kernel.
novelty_assessment: Directly checked antecedents are identified below. No exhaustive novelty determination
  or certification of a source headline is claimed.
formalization_summary: Read the scope and both listed Comparators. EditDistance targets matching exponential-order
  bounds uniformly over finite alphabets. FiniteCircle includes specific binary code inequalities, finite
  witnesses and a histogram upper construction. Other listed Comparators were not inspected. Inspected
  Comparator target bodies contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: The first card is conditional on a bounded-alphabet embedding. The second concerns
  a finite l1 metric and lists with repetitions; the partition distribution is fixed for the whole point
  set.
dependencies: Longest common subsequences, random hashing, l1 direct sums, threshold cuts and finite probability.
antecedents: Ostrovsky-Rabani binary edit-distance embeddings and classical cut representations of l1
  metrics.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Alphabet compression and finite partition histograms

## Source manuscripts and claim

- [Edit Distance in l1: Matching Bounds up to Constants in the Exponent](../papers/P-000455.md): selected passages extracted.
- [Finite-Circle Obstructions, Binary Codes, and Histogram Embeddings for Edit Distance](../papers/P-000456.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Tree Constructions for the l1 Distortion of Binary Edit Distance](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026)

The family claims matching exponential-order bounds for embedding edit distance into l1.

## Extracted instruments

- [MI-000686: Remove alphabet size by collision-controlled hashing and a direct sum](../instruments/MI-000686.md)
- [MI-000687: Convert finite l1 cuts into exponential collisions and histogram bounds](../instruments/MI-000687.md)

## Dependencies and antecedents

Longest common subsequences, random hashing, l1 direct sums, threshold cuts and finite probability.

Ostrovsky-Rabani binary edit-distance embeddings and classical cut representations of l1 metrics.

## Review and formalization scope

Read the complete uniform-upper proof and the partition and histogram proofs. Two of three manuscripts receive extractions; the tree-construction manuscript remains inventory-only. The delimiter-code input and the lower-bound constructions are not certified.

Read the scope and both listed Comparators. EditDistance targets matching exponential-order bounds uniformly over finite alphabets. FiniteCircle includes specific binary code inequalities, finite witnesses and a histogram upper construction. Other listed Comparators were not inspected. Inspected Comparator target bodies contain sorry; no separate solution or Lean build was checked.

The first card is conditional on a bounded-alphabet embedding. The second concerns a finite l1 metric and lists with repetitions; the partition distribution is fixed for the whole point set.

[Batch record](../../batches/B073/README.md)
