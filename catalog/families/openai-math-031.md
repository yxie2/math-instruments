---
id: openai-math-031
record_type: family
title: Normalizer extension and simultaneous power-residue separation
source_family: '031'
source_collection: openai/math
batch_id: B022
subject: Number theory
source_paper_ids:
- P-000162
instrument_ids:
- MI-000286
- MI-000287
headline: The source claims that every continuous open homomorphism between Galois groups of solvably
  closed Galois extensions of number fields comes from a unique contravariant field embedding, with no
  restriction on its kernel.
central_instrument: Unique implementation of induced automorphisms extends a local homomorphism to the
  normalizer of its kernel. Distinct auxiliary Kummer exponents impose simultaneous, potentially overlapping,
  residue-separation requirements without conflict.
novelty_assessment: The normalizer argument depends on classical Uchida reconstruction, and the separation
  lemma combines classical Kummer theory with Chebotarev. The selected formulations and bookkeeping are
  useful independently; no exhaustive priority or full anabelian proof certification is claimed.
formalization_summary: No family-specific Lean scope document is listed in the pinned release inventory
  for family 031. No formal proof project was built.
statement_faithfulness: Unique realization of each relevant automorphism is an explicit input to the normalizer
  argument; trivial center alone does not guarantee realization. Power-separation sets may overlap and
  contain other distinguished primes, but each excludes its own distinguished prime.
dependencies: Normalizer of a kernel, uniqueness of conjugation implementers, open subgroups of profinite
  groups, valuations in cyclotomic fields, Kummer independence and Chebotarev conjugacy classes.
antecedents: Uchida, Isomorphisms of Galois groups of solvably closed Galois extensions (1979); classical
  Kummer theory and Chebotarev density.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Normalizer extension and simultaneous power-residue separation

## Source manuscript and claim

[Open Homomorphisms of Global Solvably Closed Galois Groups](../papers/P-000162.md), by OpenAI, October 5, 2026.

The source claims that every continuous open homomorphism between Galois groups of solvably closed Galois extensions of number fields comes from a unique contravariant field embedding, with no restriction on its kernel.

## Extracted instruments

- [MI-000286: Extend to a kernel normalizer using unique conjugation implementers](../instruments/MI-000286.md)
- [MI-000287: Distinct Kummer exponents separate overlapping prime lists simultaneously](../instruments/MI-000287.md)

## Dependencies and antecedents

Normalizer of a kernel, uniqueness of conjugation implementers, open subgroups of profinite groups, valuations in cyclotomic fields, Kummer independence and Chebotarev conjugacy classes.

Uchida, Isomorphisms of Galois groups of solvably closed Galois extensions (1979); classical Kummer theory and Chebotarev density. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the entire normalizer-extension proof and simultaneous power-separation proof, together with the source statements of reconstruction and trivial centralizers. The larger matching and generation arguments were not audited.

No family-specific Lean scope document is listed in the pinned release inventory for family 031. No formal proof project was built.

Unique realization of each relevant automorphism is an explicit input to the normalizer argument; trivial center alone does not guarantee realization. Power-separation sets may overlap and contain other distinguished primes, but each excludes its own distinguished prime.

[Batch record](../../batches/B022/README.md)
