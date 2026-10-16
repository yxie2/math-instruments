---
id: openai-math-258
record_type: family
title: Capping free words and stabilizing virtually free endomorphisms
source_family: '258'
source_collection: openai/math
batch_id: B061
subject: Group theory
source_paper_ids:
- P-000364
- P-000365
instrument_ids:
- MI-000595
- MI-000596
headline: The sources claim hyperbolicity for Baumslag-Solitar-free one-relator groups and virtual compact
  specialness for hyperbolic one-relator groups.
central_instrument: A one-letter cap turns based words into cyclic words with bounded errors under fixed
  free-group injections. Stable kernels and invariant finite-index free subgroups reduce virtually free
  mapping tori to injective free ones.
novelty_assessment: The arguments use classical free-group quasigeodesics, normal forms and Hopficity.
  Their exact source interfaces are extracted without claiming earliest priority or the global one-relator
  results.
formalization_summary: No Lean scope document or linked Comparator is supplied for this family in the
  pinned inventory. No formal solution was built.
statement_faithfulness: Caps are chosen in the domain before applying injections. All constants may depend
  on the fixed injections and tested word. Kernel stabilization is for finitely generated virtually free
  groups, not arbitrary groups.
dependencies: Reduced and cyclic words, undistortion of finitely generated free subgroups, Morse bounds,
  finite quotients, Hopficity and ascending normal forms.
antecedents: Classical bounded-cancellation and free-group current methods; invariant finite-index cores
  and Hopficity.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Capping free words and stabilizing virtually free endomorphisms

## Source manuscripts and claim

- [Baumslag-Solitar-free one-relator groups are hyperbolic](../papers/P-000364.md): selected passages extracted.
- [Virtual compact specialness of hyperbolic one-relator groups](../papers/P-000365.md): selected passages extracted.

The sources claim hyperbolicity for Baumslag-Solitar-free one-relator groups and virtual compact specialness for hyperbolic one-relator groups.

## Extracted instruments

- [MI-000595: Cap a free word before transferring it to a counting current](../instruments/MI-000595.md)
- [MI-000596: Remove stable kernels before passing from virtually free to free mapping tori](../instruments/MI-000596.md)

## Dependencies and antecedents

Reduced and cyclic words, undistortion of finitely generated free subgroups, Morse bounds, finite quotients, Hopficity and ascending normal forms.

Classical bounded-cancellation and free-group current methods; invariant finite-index cores and Hopficity.

## Review and formalization scope

Read the complete capping lemma and complete virtually-free stabilization proof. The current trajectory, annular flaring, filling and cubulation arguments remain unaudited.

No Lean scope document or linked Comparator is supplied for this family in the pinned inventory. No formal solution was built.

Caps are chosen in the domain before applying injections. All constants may depend on the fixed injections and tested word. Kernel stabilization is for finitely generated virtually free groups, not arbitrary groups.

[Batch record](../../batches/B061/README.md)
