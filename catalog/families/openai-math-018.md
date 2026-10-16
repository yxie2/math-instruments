---
id: openai-math-018
record_type: family
title: Sign-action extension obstructions and local denominator clearing
source_family: 018
source_collection: openai/math
batch_id: B065
subject: Number theory
source_paper_ids:
- P-000393
- P-000394
instrument_ids:
- MI-000624
- MI-000625
headline: The sources claim the Margulis-Platonov conjecture over global function fields and number fields.
central_instrument: A central involution acting by minus one reduces splitting of a lattice extension
  to a mod-two cocycle. Local density plus a full lattice yields a rational additive spanning criterion.
novelty_assessment: The extracted arguments use classical ingredients. The particular source interfaces
  are recorded without certifying a new headline theorem or earliest priority.
formalization_summary: No Lean scope document or linked Comparator is supplied for this family in the
  pinned inventory. No formal solution was built.
statement_faithfulness: The cohomological class is attached to an existing extension; no surjectivity
  onto all cohomology classes is claimed. The spanning criterion assumes local density and a full lattice
  and does not prove the source group-theoretic inputs.
dependencies: Group extensions, cocycles, torsion-free lattices, rational denominators and the Chinese
  remainder theorem.
antecedents: Classical extension cocycles and local-to-global lattice arithmetic; the function-field source
  explicitly relates its sign argument to its number-field companion.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Sign-action extension obstructions and local denominator clearing

## Source manuscripts and claim

- [The Margulis–Platonov conjecture over global function fields](../papers/P-000393.md): selected passages extracted.
- [The Margulis–Platonov conjecture over number fields](../papers/P-000394.md): selected passages extracted.

The sources claim the Margulis-Platonov conjecture over global function fields and number fields.

## Extracted instruments

- [MI-000624: Detect splitting of a sign-action lattice extension modulo two](../instruments/MI-000624.md)
- [MI-000625: Clear rational denominators using local density and a full lattice](../instruments/MI-000625.md)

## Dependencies and antecedents

Group extensions, cocycles, torsion-free lattices, rational denominators and the Chinese remainder theorem.

Classical extension cocycles and local-to-global lattice arithmetic; the function-field source explicitly relates its sign argument to its number-field companion.

## Review and formalization scope

Read the complete sign-element lemma, its lift calculations and involution restriction, and the complete additive-span proof. Extract only the final general denominator-clearing implication from the latter. Global norm-torus and normal-subgroup arguments remain unaudited.

No Lean scope document or linked Comparator is supplied for this family in the pinned inventory. No formal solution was built.

The cohomological class is attached to an existing extension; no surjectivity onto all cohomology classes is claimed. The spanning criterion assumes local density and a full lattice and does not prove the source group-theoretic inputs.

[Batch record](../../batches/B065/README.md)
