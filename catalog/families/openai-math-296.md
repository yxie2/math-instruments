---
id: openai-math-296
record_type: family
title: Baire generation criteria and explicit matrix encoding
source_family: '296'
source_collection: openai/math
batch_id: B018
subject: Operator algebras
source_paper_ids:
- P-000145
instrument_ids:
- MI-000251
- MI-000252
headline: The source claims single generation for every type II_1 factor with separable predual and a
  dense G_delta locus of relative generating unitaries for every irreducible inclusion of such factors.
central_instrument: Simultaneous continuity of projection norms turns a persistent perturbative correlation
  into generic generation. A separated-spectrum two-by-two encoding converts four self-adjoint corner
  generators into two.
novelty_assessment: Baire continuity and matrix-unit encoding are classical mechanisms. The conditional
  perturbative interface is useful, but its difficult perturbation input and the global generator theorem
  were not certified.
formalization_summary: 'The scope document, FactorGeneration.lean and RelativeGeneration.lean targets
  were inspected. They use separable predual, arbitrary representing Hilbert spaces and the normalized
  trace two-topology. Comparator statements were inspected, not proof builds: no Lean solution was built
  or kernel-checked. The auxiliary cards are not all separate formalization targets.'
statement_faithfulness: The generation criterion is conditional on a persistent-correlation perturbation
  at every proper subspace. The amplitude is fixed before word length tends to infinity. Matrix encoding
  assumes four self-adjoint generators of the corner.
dependencies: Complete metric spaces, Baire category, semicontinuity, separable L2 spaces, conditional
  expectations, spectral calculus and matrix units.
antecedents: Classical continuity-point results for semicontinuous functions and classical matrix-amplification
  generator encodings; source-specific perturbation estimates are separate.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Baire generation criteria and explicit matrix encoding

## Source manuscript and claim

[Relative generation and the generator problem for finite factors](../papers/P-000145.md), by OpenAI, September 23, 2026.

The source claims single generation for every type II_1 factor with separable predual and a dense G_delta locus of relative generating unitaries for every irreducible inclusion of such factors.

## Extracted instruments

- [MI-000251: Persistent correlations at proper subspaces force a dense G_delta generation locus](../instruments/MI-000251.md)
- [MI-000252: Separated spectra encode four self-adjoint generators into two after amplification](../instruments/MI-000252.md)

## Dependencies and antecedents

Complete metric spaces, Baire category, semicontinuity, separable L2 spaces, conditional expectations, spectral calculus and matrix units.

Classical continuity-point results for semicontinuous functions and classical matrix-amplification generator encodings; source-specific perturbation estimates are separate. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the completeness, projection-continuity and final generation argument, plus the full four-to-two matrix encoding. The independence construction and perturbation proposition were not audited.

The scope document, FactorGeneration.lean and RelativeGeneration.lean targets were inspected. They use separable predual, arbitrary representing Hilbert spaces and the normalized trace two-topology. Comparator statements were inspected, not proof builds: no Lean solution was built or kernel-checked. The auxiliary cards are not all separate formalization targets.

The generation criterion is conditional on a persistent-correlation perturbation at every proper subspace. The amplitude is fixed before word length tends to infinity. Matrix encoding assumes four self-adjoint generators of the corner.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/296.md) · [Batch record](../../batches/B018/README.md)
