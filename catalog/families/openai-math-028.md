---
id: openai-math-028
record_type: family
title: Shared entropy costs and uniform bounds from periodic obstructions
source_family: 028
source_collection: openai/math
batch_id: B022
subject: Number theory
source_paper_ids:
- P-000161
instrument_ids:
- MI-000284
- MI-000285
headline: The source claims that for each fixed step bound every connected component of the Gaussian-prime
  graph has uniformly bounded cardinality, and consequently no infinite injective walk with bounded steps
  exists.
central_instrument: A single shared conditioning variable costs its entropy once before averaging sampled
  coordinates. A periodic avoiding graph with no infinite path has components injecting into one finite
  residue cell, and finitely many exceptional vertices incur an explicit degree budget.
novelty_assessment: The entropy calculation uses classical chain rules and subadditivity. The source credits
  Vardi for the periodicity principle. The finite-obstruction construction linking these mechanisms to
  the Gaussian moat problem was not audited.
formalization_summary: Read GaussianMoat.lean, including Gaussian-prime vertices, the real step bound,
  the uniform finite component-cardinality target and its no-infinite-injective-walk consequence. The
  inspected Comparator files contain target statements with sorry placeholders; no Lean solution was built
  or kernel-checked.
statement_faithfulness: The sampled coordinate set is independent of all other random data; Y and the
  shared conditioning variable may depend on each other. The component bound is conditional on the existence
  of a periodic obstruction with no infinite path, and explicitly restores the finitely many removed Gaussian
  primes.
dependencies: Shannon entropy chain rule and subadditivity, uniform coordinate inclusion probabilities,
  locally finite path trees, lattice translations and a finite attachment-degree count.
antecedents: Classical Shannon entropy inequalities; Vardi, Prime percolation, Section 6, Proposition
  6.2, as explicitly credited by the source.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Shared entropy costs and uniform bounds from periodic obstructions

## Source manuscript and claim

[Bounded-Step Walks on Gaussian Primes](../papers/P-000161.md), by OpenAI, September 26, 2026.

The source claims that for each fixed step bound every connected component of the Gaussian-prime graph has uniformly bounded cardinality, and consequently no infinite injective walk with bounded steps exists.

## Extracted instruments

- [MI-000284: Pay a shared conditioning entropy once before averaging sampled coordinates](../instruments/MI-000284.md)
- [MI-000285: A periodic graph without an infinite path has a finite-cell component bound](../instruments/MI-000285.md)

## Dependencies and antecedents

Shannon entropy chain rule and subadditivity, uniform coordinate inclusion probabilities, locally finite path trees, lattice translations and a finite attachment-degree count.

Classical Shannon entropy inequalities; Vardi, Prime percolation, Section 6, Proposition 6.2, as explicitly credited by the source. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete shared-conditioning lemma and periodic-component proposition. The finite sieve theorem, coverage-transfer schedule and geometric obstruction construction were not audited.

Read GaussianMoat.lean, including Gaussian-prime vertices, the real step bound, the uniform finite component-cardinality target and its no-infinite-injective-walk consequence. The inspected Comparator files contain target statements with sorry placeholders; no Lean solution was built or kernel-checked.

The sampled coordinate set is independent of all other random data; Y and the shared conditioning variable may depend on each other. The component bound is conditional on the existence of a periodic obstruction with no infinite path, and explicitly restores the finitely many removed Gaussian primes.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/028.md) · [Batch record](../../batches/B022/README.md)
