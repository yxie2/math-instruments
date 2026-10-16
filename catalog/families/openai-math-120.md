---
id: openai-math-120
record_type: family
title: Sparse matching reductions with explicit witness decoding
source_family: '120'
source_collection: openai/math
batch_id: B035
subject: Theoretical computer science
source_paper_ids:
- P-000212
instrument_ids:
- MI-000386
- MI-000387
headline: The source claims almost-linear-time exact maximum-cardinality matching and prescribed-degree
  factors in sparse general graphs.
central_instrument: A permutation network replaces dense unmatched-vertex connections in cardinality-to-perfect-matching
  reduction; odd-length incidence paths reduce degree to three with a local witness decoder.
novelty_assessment: Permutation networks and degree-reduction matching gadgets are classical. The extraction
  records size and witness preservation, not the source fast matching engine.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build was performed.
statement_faithfulness: Original vertex records, including isolates, are retained. The threshold reduction
  asks for exact size k, equivalent to at least k by deleting matching edges. Degree reduction handles
  isolates before constructing odd paths.
dependencies: Rearrangeable permutation networks, alternating cycle coloring, perfect matching incidence
  counts and odd-path parity.
antecedents: Classical permutation networks; the source explicitly credits the path degree reduction to
  Dahlhaus-Karpinski 1992.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Sparse matching reductions with explicit witness decoding

## Source manuscript and claim

[Almost-Linear-Time Maximum-Cardinality Matching in General Graphs](../papers/P-000212.md), by OpenAI, September 24, 2026.

The source claims almost-linear-time exact maximum-cardinality matching and prescribed-degree factors in sparse general graphs.

## Extracted instruments

- [MI-000386: Reduce a matching cardinality threshold using a sparse permutation network](../instruments/MI-000386.md)
- [MI-000387: Reduce perfect matching to maximum degree three with odd incidence paths](../instruments/MI-000387.md)

## Dependencies and antecedents

Rearrangeable permutation networks, alternating cycle coloring, perfect matching incidence counts and odd-path parity.

Classical permutation networks; the source explicitly credits the path degree reduction to Dahlhaus-Karpinski 1992. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete permutation-network, cardinality reduction and degree reduction proofs. The matching state, projection algorithm, dynamic backend and almost-linear complexity were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build was performed.

Original vertex records, including isolates, are retained. The threshold reduction asks for exact size k, equivalent to at least k by deleting matching edges. Degree reduction handles isolates before constructing odd paths.

[Batch record](../../batches/B035/README.md)
