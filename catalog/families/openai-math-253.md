---
id: openai-math-253
record_type: family
title: Dimension-free density perturbations and finite Folner extraction
source_family: '253'
source_collection: openai/math
batch_id: B030
subject: Group theory
source_paper_ids:
- P-000194
instrument_ids:
- MI-000350
- MI-000351
headline: The source claims an infinite finitely presented simple amenable group.
central_instrument: Orthogonality of centered product-density scores makes square-root density speed independent
  of dimension. Equivariant coset projection and layer cake turn almost-invariant probabilities into finite
  Folner sets.
novelty_assessment: Square-root density geometry, product orthogonality, Reiter conditions and layer-cake
  Folner extraction are established methods. The selected formulas expose the constants and whole-field
  versus marginal distinction; the source simple amenable group claim remains unaudited.
formalization_summary: Read SimpleAmenable.lean. Its target asks for one infinite finitely presented simple
  group with finite nonempty Folner sets for every finite set of translations and positive error. The
  inspected Comparator contains a sorry target; no Lean build or kernel verification was performed.
statement_faithfulness: The density has a nonnegative even smooth compactly supported square root. Whole-field
  total variation follows from an exactly common independent outside factor, not from convergence of finitely
  many marginals. Subgroup projection uses right cosets for a left group action.
dependencies: Differentiation of densities, integration by parts, independence and parity, resolvent identity,
  total variation contraction, finite truncation and layer cake.
antecedents: Classical Hellinger/Fisher-information calculations and Reiter-to-Folner arguments; no first-priority
  claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Dimension-free density perturbations and finite Folner extraction

## Source manuscript and claim

[An infinite finitely presented simple amenable group](../papers/P-000194.md), by OpenAI, September 23, 2026.

The source claims an infinite finitely presented simple amenable group.

## Extracted instruments

- [MI-000350: Bound affine product-density perturbations independently of dimension](../instruments/MI-000350.md)
- [MI-000351: Push approximate invariance to a subgroup and extract a finite Folner set](../instruments/MI-000351.md)

## Dependencies and antecedents

Differentiation of densities, integration by parts, independence and parity, resolvent identity, total variation contraction, finite truncation and layer cake.

Classical Hellinger/Fisher-information calculations and Reiter-to-Folner arguments; no first-priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full density-speed lemma, entire-field covariance proof, shape-matching conclusion and Reiter-to-Folner proof. The averaging-matrix estimates, partition coupling, finite presentation and simplicity constructions were not audited.

Read SimpleAmenable.lean. Its target asks for one infinite finitely presented simple group with finite nonempty Folner sets for every finite set of translations and positive error. The inspected Comparator contains a sorry target; no Lean build or kernel verification was performed.

The density has a nonnegative even smooth compactly supported square root. Whole-field total variation follows from an exactly common independent outside factor, not from convergence of finitely many marginals. Subgroup projection uses right cosets for a left group action.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/253.md) · [Batch record](../../batches/B030/README.md)
