---
id: openai-math-195
record_type: family
title: Slope balancing and a divisor-layer variance obstruction
source_family: '195'
source_collection: openai/math
batch_id: B052
subject: Algebra
source_paper_ids:
- P-000287
instrument_ids:
- MI-000512
- MI-000513
headline: The source claims a three-dimensional complete local complex domain with no nonzero finitely
  generated maximal Cohen-Macaulay module.
central_instrument: Elementary modification raises the average restriction slope while bounding its maximum.
  A Cartier-divisor layer filtration produces a nonnegative Chern-character variance, which can be compared
  with semistable-factor upper bounds.
novelty_assessment: Slope modification has an explicit Chen-Sun antecedent. The layer calculation and
  its numerical interface are source arguments built from standard restriction and Chern-character identities;
  no exhaustive priority claim.
formalization_summary: The target asserts only existence of a three-dimensional complete Noetherian integrally
  closed local C-algebra with residue field C. It does not assert absence of a small Cohen-Macaulay module
  or the essentially finite-type counterexample. The scope document and linked Comparator were read in
  full. The target proof contains sorry; no solution or Lean project was built.
statement_faithfulness: The divisor is smooth and its conormal is ample. Balancing yields slope width
  at most one, not semistability. The layer variance need not be nonnegative for an arbitrary sheaf without
  the extension and punctured-triviality hypotheses.
dependencies: Harder-Narasimhan filtrations, Cartier Tor sequence, coherent lattice filtrations, Chern
  characters, surface Riemann-Roch, Bogomolov and Hodge index inequalities.
antecedents: Chen-Sun optimal extensions and Hecke transforms; standard surface and coherent-sheaf identities.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Slope balancing and a divisor-layer variance obstruction

## Source manuscripts and claim

- [A Complete Local Domain without a Small Cohen–Macaulay Module](../papers/P-000287.md): selected passages extracted.

The source claims a three-dimensional complete local complex domain with no nonzero finitely generated maximal Cohen-Macaulay module.

## Extracted instruments

- [MI-000512: Balance restriction slopes with a bounded monotone average](../instruments/MI-000512.md)
- [MI-000513: Extract a nonnegative variance from a Cartier-divisor lattice filtration](../instruments/MI-000513.md)

## Dependencies and antecedents

Harder-Narasimhan filtrations, Cartier Tor sequence, coherent lattice filtrations, Chern characters, surface Riemann-Roch, Bogomolov and Hodge index inequalities.

Chen-Sun optimal extensions and Hecke transforms; standard surface and coherent-sheaf identities.

## Review and formalization scope

Read the complete balancing, divisor-lattice and semistable-factor proofs and the final variance mixture calculation. The completed-cone extension and explicit surface construction remain unverified here.

The target asserts only existence of a three-dimensional complete Noetherian integrally closed local C-algebra with residue field C. It does not assert absence of a small Cohen-Macaulay module or the essentially finite-type counterexample. The scope document and linked Comparator were read in full. The target proof contains sorry; no solution or Lean project was built.

The divisor is smooth and its conormal is ample. Balancing yields slope width at most one, not semistability. The layer variance need not be nonnegative for an arbitrary sheaf without the extension and punctured-triviality hypotheses.

[Batch record](../../batches/B052/README.md)
