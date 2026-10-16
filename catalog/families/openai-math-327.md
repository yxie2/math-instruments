---
id: openai-math-327
record_type: family
title: Reversible lifts for edge labels and ordered charts
source_family: '327'
source_collection: openai/math
batch_id: B008
subject: Functional analysis
source_paper_ids:
- P-000105
instrument_ids:
- MI-000165
- MI-000166
headline: The source claims that a real Banach space has nontrivial Markov type exactly when it admits
  an equivalent uniformly convex norm. The extracted tools convert edge increments and ordered partial
  motions into finite reversible chains.
central_instrument: A reflecting lattice lift turns odd edge labels into a potential increment; finite
  Ramsey averaging and transposed couplings realize partial order maps while preserving stationary marginals
  and independent letters.
novelty_assessment: Markov type, finite representability, Ramsey theory and maximal coupling are established.
  The selected constructions are candidate source-specific combinations supporting its walk argument.
  The superreflexivity characterization and priority are not certified.
formalization_summary: MarkovType.lean states equivalence between a uniform Markov-type inequality for
  some exponent p>1 and existence of an equivalent uniformly convex norm, including the zero space. The
  scope document and Comparator declarations were compared. No Lean solution was built or kernel-checked,
  and the auxiliary instruments are not separate Comparator targets.
statement_faithfulness: Ordinary Markov type is distinct from Markov convexity and Rademacher type. Chains
  are finite, stationary and reversible; their size can depend on the tested time, while the Markov-type
  constant is uniform. Marked self-transitions may carry nonzero labels if their reverse mark is different.
dependencies: Edgewise detailed balance; odd vector labels; finite lattice boxes with rejected boundary
  moves; finite representability; finite Ramsey and separation; equal-marginal couplings paired by transpose.
antecedents: Ball introduced Markov type; Naor-Peres-Schramm-Sheffield established smooth-space implications.
  Brunel-Sucheston supplied the ordered-spreading background. The James-Enflo structural reduction and
  the source’s linear-displacement walk are additional inputs beyond the two extracted constructions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Reversible lifts for edge labels and ordered charts

## Source manuscript and claim

[Nontrivial Markov Type Forces Superreflexivity](../papers/P-000105.md), by OpenAI, September 23, 2026.

The source claims that a real Banach space has nontrivial Markov type exactly when it admits an equivalent uniformly convex norm. The extracted tools convert edge increments and ordered partial motions into finite reversible chains.

## Extracted instruments

- [MI-000165: A finite reflecting lattice lift transfers Markov type to odd edge sums](../instruments/MI-000165.md)
- [MI-000166: Ramsey averaging and transposed couplings build reversible chart transport](../instruments/MI-000166.md)

## Dependencies and antecedents

Edgewise detailed balance; odd vector labels; finite lattice boxes with rejected boundary moves; finite representability; finite Ramsey and separation; equal-marginal couplings paired by transpose.

Ball introduced Markov type; Naor-Peres-Schramm-Sheffield established smooth-space implications. Brunel-Sucheston supplied the ordered-spreading background. The James-Enflo structural reduction and the source’s linear-displacement walk are additional inputs beyond the two extracted constructions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the odd-edge-label proof, finite order averaging and reversible chart transport. The reduced-word action, linear-displacement construction and complete spreading-norm argument were not fully audited.

MarkovType.lean states equivalence between a uniform Markov-type inequality for some exponent p>1 and existence of an equivalent uniformly convex norm, including the zero space. The scope document and Comparator declarations were compared. No Lean solution was built or kernel-checked, and the auxiliary instruments are not separate Comparator targets.

Ordinary Markov type is distinct from Markov convexity and Rademacher type. Chains are finite, stationary and reversible; their size can depend on the tested time, while the Markov-type constant is uniform. Marked self-transitions may carry nonzero labels if their reverse mark is different.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/327.md) · [Batch record](../../batches/B008/README.md)
