---
id: openai-math-059
record_type: family
title: Henselian square lifting and integral lattice residues
source_family: 059
source_collection: openai/math
batch_id: B070
subject: Algebraic and complex geometry
source_paper_ids:
- P-000437
- P-000438
instrument_ids:
- MI-000668
- MI-000669
headline: The sources claim ambiently homeomorphic isolated hypersurfaces with different multiplicities.
central_instrument: Newton iteration lifts residue-field square representations in a finite operator algebra.
  A transfer congruence specifies an integral lattice inside a rational splitting.
novelty_assessment: The selected tools use established mechanisms. Exact source-specific rounding and
  lattice interfaces have not received exhaustive priority checks. No headline theorem is certified.
formalization_summary: No Lean scope document is supplied for this family in the pinned inventory. No
  formal solution was built.
statement_faithfulness: Square lifting requires an odd residue characteristic and units. The lattice card
  is conditional on the supplied exact sequence and signed transfer congruence; it does not verify their
  geometric construction.
dependencies: Finite complete algebras, Jacobson radicals, Newton iteration, finite-field counting, torsion-free
  lattices and projection-transfer identities.
antecedents: Classical Hensel lifting and integral gluing by residue congruences.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Henselian square lifting and integral lattice residues

## Source manuscripts and claim

- [Ambiently homeomorphic isolated hypersurfaces of multiplicities two and three](../papers/P-000437.md): selected passages extracted.
- [Ambiently homeomorphic isolated hypersurface germs in ℂ⁴ with multiplicities four and five](../papers/P-000438.md): selected passages extracted.

The sources claim ambiently homeomorphic isolated hypersurfaces with different multiplicities.

## Extracted instruments

- [MI-000668: Lift squares and two-square representations in a finite odd-adic algebra](../instruments/MI-000668.md)
- [MI-000669: Recover an integral lattice from projection-transfer residues](../instruments/MI-000669.md)

## Dependencies and antecedents

Finite complete algebras, Jacobson radicals, Newton iteration, finite-field counting, torsion-free lattices and projection-transfer identities.

Classical Hensel lifting and integral gluing by residue congruences.

## Review and formalization scope

Read the complete operator-algebra lifting proof and integral-extension proof, plus the lattice definitions and rational-coordinate setup. Both manuscripts receive extractions. The preceding Bockstein/Mayer-Vietoris statements are retained as inputs, not certified; seed certificates, global isometries and ambient homeomorphisms are outside the audit.

No Lean scope document is supplied for this family in the pinned inventory. No formal solution was built.

Square lifting requires an odd residue characteristic and units. The lattice card is conditional on the supplied exact sequence and signed transfer congruence; it does not verify their geometric construction.

[Batch record](../../batches/B070/README.md)
