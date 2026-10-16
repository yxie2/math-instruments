---
id: openai-math-182
record_type: family
title: Compatible polynomial coordinates and finite square constraints
source_family: '182'
source_collection: openai/math
batch_id: B076
subject: Combinatorics
source_paper_ids:
- P-000481
- P-000482
instrument_ids:
- MI-000714
- MI-000715
headline: The family claims power savings for sets avoiding polynomial differences, including prime arguments
  and degree-dependent exponents.
central_instrument: Normalize the first nonzero coefficient at chosen local roots, preserve progression
  inheritance, and separate finite square constraints by a kernel norm.
novelty_assessment: Established mechanisms are credited explicitly. Selected source-specific formulations
  are extracted without an exhaustive priority claim.
formalization_summary: The scope and SquareDifference Comparator target a fixed power saving for square-difference-free
  subsets of every interval [1,N], not the broader polynomial or prime-argument results. The complete
  scope and Comparator were read. The inspected target contains sorry; no separate solution or Lean build
  was checked.
statement_faithfulness: Local root choices are compatible across powers; multiplicities may vary with
  the prime. Graph counting permits only one directed edge per unordered pair.
dependencies: p-adic valuations, Chinese remaindering, Gauss sums, telescoping products and fourth Schatten
  moments.
antecedents: Lucier auxiliary polynomials, classical quadratic Gauss sums and four-cycle operator estimates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Compatible polynomial coordinates and finite square constraints

## Source manuscripts and claim

- [A power saving for intersective polynomial differences with an exponent depending only on the degree](../papers/P-000481.md): selected passages extracted.
- [A power saving for square-difference-free sets](../papers/P-000482.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [A Power Saving for Polynomial Differences at Prime Arguments](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026)

The family claims power savings for sets avoiding polynomial differences, including prime arguments and degree-dependent exponents.

## Extracted instruments

- [MI-000714: Normalize local root coefficients while retaining progression inheritance](../instruments/MI-000714.md)
- [MI-000715: Count square constraints before lifting to a two-list operator bound](../instruments/MI-000715.md)

## Dependencies and antecedents

p-adic valuations, Chinese remaindering, Gauss sums, telescoping products and fourth Schatten moments.

Lucier auxiliary polynomials, classical quadratic Gauss sums and four-cycle operator estimates.

## Review and formalization scope

Read the full normalization and auxiliary-family proofs in the intersective manuscript and both graph-counting/list-mixing proofs in the square-difference manuscript. The prime-argument companion is inventory-only. The power-saving induction and tuple-law constructions are not certified.

The scope and SquareDifference Comparator target a fixed power saving for square-difference-free subsets of every interval [1,N], not the broader polynomial or prime-argument results. The complete scope and Comparator were read. The inspected target contains sorry; no separate solution or Lean build was checked.

Local root choices are compatible across powers; multiplicities may vary with the prime. Graph counting permits only one directed edge per unordered pair.

[Batch record](../../batches/B076/README.md)
