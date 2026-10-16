---
id: openai-math-043
record_type: family
title: Common lowering operators and tensor Lefschetz detection
source_family: '043'
source_collection: openai/math
batch_id: B039
subject: Algebraic and complex geometry
source_paper_ids:
- P-000227
instrument_ids:
- MI-000416
- MI-000417
headline: The source claims P=W in composite rank with fixed determinant.
central_instrument: A common lowering operator and one double-commutator identity determine a Lefschetz
  filtration. Lefschetz symmetry of a nonzero tensor product detects symmetry of both factors.
novelty_assessment: The eigenspace-filtration mechanism has an explicit antecedent in Hausel-Mellit-Minets-Schiffmann.
  The selected linear algebra is curated as an interface, without an independent priority claim.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: Both filtrations must have the same center and be compatible with the same raising
  and lowering operators. A common raising operator alone does not suffice. Both tensor factors must be
  nonzero.
dependencies: Finite filtrations, primitive Lefschetz strings and finite-dimensional sl2 representation
  theory in characteristic zero.
antecedents: Hausel-Mellit-Minets-Schiffmann, P=W via H_2, especially the operator/filtration comparison
  in Section 8.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Common lowering operators and tensor Lefschetz detection

## Source manuscript and claim

[P=W in composite rank for fixed determinant](../papers/P-000227.md), by OpenAI, September 24, 2026.

The source claims P=W in composite rank with fixed determinant.

## Extracted instruments

- [MI-000416: Recover a Lefschetz filtration from a common lowering operator](../instruments/MI-000416.md)
- [MI-000417: Detect hard Lefschetz in nonzero tensor factors](../instruments/MI-000417.md)

## Dependencies and antecedents

Finite filtrations, primitive Lefschetz strings and finite-dimensional sl2 representation theory in characteristic zero.

Hausel-Mellit-Minets-Schiffmann, P=W via H_2, especially the operator/filtration comparison in Section 8. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete selected comparison and tensor-product proofs. The geometric construction of the common lowering operator was not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

Both filtrations must have the same center and be compatible with the same raising and lowering operators. A common raising operator alone does not suffice. Both tensor factors must be nonzero.

[Batch record](../../batches/B039/README.md)
