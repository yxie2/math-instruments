---
id: openai-math-220
record_type: family
title: Unused environment rows and strictly positive repeated trials
source_family: '220'
source_collection: openai/math
batch_id: B078
subject: Probability and statistical mechanics
source_paper_ids:
- P-000491
instrument_ids:
- MI-000728
- MI-000729
headline: The family claims directional zero-one laws and ballisticity statements for random walks in
  random environments.
central_instrument: Factor only at departure rows that have actually been used; exploit repeated positive-probability
  trials without imposing a uniform ellipticity constant.
novelty_assessment: Classical finite mechanisms are separated from the source headline claims. Exhaustive
  priority is not established.
formalization_summary: DirectionalWalk targets an iid strictly elliptic directional zero-one assertion
  in dimensions at least three for arbitrary nonzero real directions. It supplies no proof of that assertion
  in the inspected target file. The full scope document and named Comparator were read. Other linked Comparators
  were not inspected. Target declarations contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: The extracted manuscript assumes iid nearest-neighbor transition rows, each strictly
  positive almost surely. A terminal arrival does not use its row until a departure occurs.
dependencies: Product environment law, the strong Markov property, finite prescribed paths and first-visit
  column bookkeeping.
antecedents: The finite-slab argument already appears in Zerner and Merkl, A zero-one law for planar random
  walks in random environment, Lemma 4.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Unused environment rows and strictly positive repeated trials

## Source manuscripts and claim

- [A directional zero–one law under strict ellipticity](../papers/P-000491.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [A directional zero–one law for finite-range-dependent random environments](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026)
- [Directional transience implies ballisticity](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Directional-transience-implies-ballisticity-September-23-2026)

The family claims directional zero-one laws and ballisticity statements for random walks in random environments.

## Extracted instruments

- [MI-000728: Transfer path events using unused departure rows](../instruments/MI-000728.md)
- [MI-000729: Escape a finite directional slab using strict ellipticity alone](../instruments/MI-000729.md)

## Dependencies and antecedents

Product environment law, the strong Markov property, finite prescribed paths and first-visit column bookkeeping.

The finite-slab argument already appears in Zerner and Merkl, A zero-one law for planar random walks in random environment, Lemma 4.

## Review and formalization scope

Read both complete selected proofs, including repeated departures and the finite/infinite column split. Two companions are inventory-only. No directional zero-one or ballisticity headline is certified.

DirectionalWalk targets an iid strictly elliptic directional zero-one assertion in dimensions at least three for arbitrary nonzero real directions. It supplies no proof of that assertion in the inspected target file. The full scope document and named Comparator were read. Other linked Comparators were not inspected. Target declarations contain sorry; no separate solution or Lean build was checked.

The extracted manuscript assumes iid nearest-neighbor transition rows, each strictly positive almost surely. A terminal arrival does not use its row until a departure occurs.

[Batch record](../../batches/B078/README.md)
