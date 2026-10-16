---
id: openai-math-202
record_type: family
title: Modular orbit cancellation and central radical annihilators
source_family: '202'
source_collection: openai/math
batch_id: B052
subject: Algebra
source_paper_ids:
- P-000288
instrument_ids:
- MI-000514
- MI-000515
headline: The source claims the blockwise Alperin weight conjecture for every finite group and prime.
central_instrument: Conjugation orbits of p-power size disappear in characteristic p, producing Brauer
  and quotient-compatible projections. Dual-basis averaging gives central elements annihilating the radical.
novelty_assessment: 'Both mechanisms are classical modular representation theory: Brauer projection and
  the Higman trace. The source uses their explicit forms in its counting reduction.'
formalization_summary: No family scope document or linked Comparator target is listed in the pinned release
  inventory. No formal verification is claimed.
statement_faithfulness: Brauer multiplicativity requires p-subgroup invariance in characteristic p. The
  dual-basis trace uses a nondegenerate symmetric associative form; conclusions for ordinary defect-zero
  characters need additional block theory.
dependencies: Finite p-group orbits, normalizer and centralizer inclusions, simple modules, symmetric
  algebra pairings and nilpotent radicals.
antecedents: Brauer morphisms, as in Webb; Higman trace and its radical-annihilation property, as in Lorenz-Tokoly.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Modular orbit cancellation and central radical annihilators

## Source manuscripts and claim

- [The Blockwise Alperin Weight Conjecture](../papers/P-000288.md): selected passages extracted.

The source claims the blockwise Alperin weight conjecture for every finite group and prime.

## Extracted instruments

- [MI-000514: Cancel p-orbits to compare coefficient restriction with Brauer projection](../instruments/MI-000514.md)
- [MI-000515: Use dual-basis averaging to construct a central radical annihilator](../instruments/MI-000515.md)

## Dependencies and antecedents

Finite p-group orbits, normalizer and centralizer inclusions, simple modules, symmetric algebra pairings and nilpotent radicals.

Brauer morphisms, as in Webb; Higman trace and its radical-annihilation property, as in Lorenz-Tokoly.

## Review and formalization scope

Read the full normalizer-projection and averaging/defect-zero proofs, plus the zero-or-one-residue lemma for context. The geometric tuple-divisibility and full weight-count proof were not certified.

No family scope document or linked Comparator target is listed in the pinned release inventory. No formal verification is claimed.

Brauer multiplicativity requires p-subgroup invariance in characteristic p. The dual-basis trace uses a nondegenerate symmetric associative form; conclusions for ordinary defect-zero characters need additional block theory.

[Batch record](../../batches/B052/README.md)
