---
id: openai-math-153
record_type: family
title: First-bit overlap and many nearby opposite prefixes
source_family: '153'
source_collection: openai/math
batch_id: B014
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000130
instrument_ids:
- MI-000219
- MI-000220
headline: The source claims an arithmetic singularity classification for Bernoulli convolutions and singular
  examples beyond reciprocal Pisot parameters, including a quartic Salem family and an explicit higher-degree
  example.
central_instrument: Entropy capacity prevents the first bit from being measurable from the full sum in
  the overlapping regime. Under singularity, compact concentration turns the resulting common measure
  into many nearby prefixes with opposite first bits.
novelty_assessment: Entropy obstructions and concentration arguments are classical. The selected decoding
  and bin-mass interfaces may be reusable, but neither the arithmetic classification nor historical priority
  is certified here.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory for this
  family. No Lean statement or proof was certified for these extracted lemmas.
statement_faithfulness: First-bit overlap holds for every lambda in (1/2,1), without assuming singularity.
  The many-neighbor result additionally assumes singularity and counts distinct words, not necessarily
  distinct prefix values.
dependencies: Compact approximation of mutually singular measures, binary Fano inequality, entropy chain
  rule, compact concentration, common submeasure mass and bounded bin incidence.
antecedents: Garsia, Entropy and singularity of infinite convolutions (1963), is a primary antecedent
  for entropy methods in these measures. The exact extracted statements are not attributed to that paper.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# First-bit overlap and many nearby opposite prefixes

## Source manuscript and claim

[Arithmetic classification and non-Pisot singularity for Bernoulli convolutions](../papers/P-000130.md), by OpenAI, October 3, 2026.

The source claims an arithmetic singularity classification for Bernoulli convolutions and singular examples beyond reciprocal Pisot parameters, including a quartic Salem family and an explicit higher-degree example.

## Extracted instruments

- [MI-000219: A decoding-capacity contradiction forces measure overlap between the two first-bit branches](../instruments/MI-000219.md)
- [MI-000220: Singular concentration and common branch mass produce many nearby opposite prefixes](../instruments/MI-000220.md)

## Dependencies and antecedents

Compact approximation of mutually singular measures, binary Fano inequality, entropy chain rule, compact concentration, common submeasure mass and bounded bin incidence.

Garsia, Entropy and singularity of infinite convolutions (1963), is a primary antecedent for entropy methods in these measures. The exact extracted statements are not attributed to that paper. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the first-bit overlap and cross-pair proofs and their compact-concentration input. The irreducible polynomial approximation, arithmetic classification, Salem arguments and explicit certificates were not audited.

No family-specific Lean scope document was listed in the pinned inventory for this family. No Lean statement or proof was certified for these extracted lemmas.

First-bit overlap holds for every lambda in (1/2,1), without assuming singularity. The many-neighbor result additionally assumes singularity and counts distinct words, not necessarily distinct prefix values.

[Batch record](../../batches/B014/README.md)
