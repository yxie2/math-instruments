---
id: openai-math-306
record_type: family
title: Nilpotent lifting and finite congruence recurrence
source_family: '306'
source_collection: openai/math
batch_id: B025
subject: Topology
source_paper_ids:
- P-000171
instrument_ids:
- MI-000304
- MI-000305
headline: The source claims that two orientation-preservingly homeomorphic Dehn fillings of a smooth nontrivial
  knot in S3 have the same unoriented slope, including the meridional slope.
central_instrument: A nilpotent labelled deformation preserves a rational quasi-isomorphism and hence
  a nonzero positive-power pairing. Mod-two quasi-isomorphisms act invertibly on the integral free homology
  lattice modulo every power of two.
novelty_assessment: Finite filtrations, Cayley-Hamilton, Nakayama and finite linear groups are classical.
  Their source application separates rational nonvanishing, torsion and congruence recurrence. The geometric
  cosmetic-surgery claim is not certified.
formalization_summary: No family-specific scope document or Comparator target is listed for this family.
  No Lean artifact was built or kernel-checked.
statement_faithfulness: A filling homeomorphism need not preserve the surgery core or exterior. The algebra
  does not require labelled homology to be free over the coefficient ring or integral homology to be torsion-free.
  Repeated operations must genuinely be powers of one map.
dependencies: Finite nilpotent filtrations of mapping cones, Cayley-Hamilton, universal coefficients,
  localization, Nakayama and the exponent of a finite general linear group.
antecedents: Classical filtered-complex lifting, finite-dimensional recurrence and local algebra; no historical
  novelty is claimed for these algebraic lemmas.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Nilpotent lifting and finite congruence recurrence

## Source manuscript and claim

[Purely cosmetic surgery on knots in the three-sphere](../papers/P-000171.md), by OpenAI, None.

The source claims that two orientation-preservingly homeomorphic Dehn fillings of a smooth nontrivial knot in S3 have the same unoriented slope, including the meridional slope.

## Extracted instruments

- [MI-000304: Lift a quasi-isomorphism through nilpotent labels and recover a positive power](../instruments/MI-000304.md)
- [MI-000305: Preserve an integral pairing by repeating a mod-two unit](../instruments/MI-000305.md)

## Dependencies and antecedents

Finite nilpotent filtrations of mapping cones, Cayley-Hamilton, universal coefficients, localization, Nakayama and the exponent of a finite general linear group.

Classical filtered-complex lifting, finite-dimensional recurrence and local algebra; no historical novelty is claimed for these algebraic lemmas. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the labelled-construction statement and proof, complete positive-power lemma, complete finite-lattice lemma and the recurrence portion of its application. The Floer counts, compactification, nonvanishing and geometric gluing inputs were not audited.

No family-specific scope document or Comparator target is listed for this family. No Lean artifact was built or kernel-checked.

A filling homeomorphism need not preserve the surgery core or exterior. The algebra does not require labelled homology to be free over the coefficient ring or integral homology to be torsion-free. Repeated operations must genuinely be powers of one map.

[Batch record](../../batches/B025/README.md)
