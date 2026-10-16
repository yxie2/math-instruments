---
id: openai-math-342
record_type: family
title: Closed anti-invariant lifts and affine current separators
source_family: '342'
source_collection: openai/math
batch_id: B038
subject: Differential geometry
source_paper_ids:
- P-000225
instrument_ids:
- MI-000412
- MI-000413
headline: The source claims that a symplectically tamed almost-complex structure on a closed four-manifold
  admits a compatible symplectic form, with additional cone descriptions.
central_instrument: An elliptic generalized inverse lifts anti-invariant forms to closed forms. Dual correction
  converts positive separators into closed currents, with different annihilation conditions for existence
  and for a prescribed class.
novelty_assessment: The lift and cohomology splitting have established four-dimensional antecedents, and
  current separation is classical Hahn-Banach duality. These ingredients do not themselves prove compatibility.
formalization_summary: Read TamingCompatibility.lean, whose fixed-J existence target contains sorry. The
  scope page links a September-23 manuscript path, whereas this extraction binds the October-6 manuscript
  in the inventory; the version mismatch is retained as a limitation. No Lean build.
statement_faithfulness: Closedness of a current means annihilation of exact test forms. An existence separator
  annihilates all closed invariant forms; a prescribed-class separator need only annihilate exact invariant
  forms. No fixed-class conclusion follows from the Comparator existence target.
dependencies: Self-dual symbol algebra, elliptic generalized inverses, harmonic projections, measure-valued
  positivity and affine separation.
antecedents: Draghici-Zhang exact-form correction, Draghici-Li-Zhang cohomology decomposition, and Sullivan/Harvey-Lawson
  positive-current separation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Closed anti-invariant lifts and affine current separators

## Source manuscript and claim

[Taming implies compatibility on four-manifolds](../papers/P-000225.md), by OpenAI, October 6, 2026.

The source claims that a symplectically tamed almost-complex structure on a closed four-manifold admits a compatible symplectic form, with additional cone descriptions.

## Extracted instruments

- [MI-000412: Lift anti-invariant two-forms to closed forms by an elliptic inverse](../instruments/MI-000412.md)
- [MI-000413: Correct positive separators while distinguishing existence from a fixed class](../instruments/MI-000413.md)

## Dependencies and antecedents

Self-dual symbol algebra, elliptic generalized inverses, harmonic projections, measure-valued positivity and affine separation.

Draghici-Zhang exact-form correction, Draghici-Li-Zhang cohomology decomposition, and Sullivan/Harvey-Lawson positive-current separation. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete closed-lift and existence-separation proofs, invariant-cohomology decomposition and prescribed-class separation. Mass, angular-energy, tangent-density and residual-current arguments were not audited.

Read TamingCompatibility.lean, whose fixed-J existence target contains sorry. The scope page links a September-23 manuscript path, whereas this extraction binds the October-6 manuscript in the inventory; the version mismatch is retained as a limitation. No Lean build.

Closedness of a current means annihilation of exact test forms. An existence separator annihilates all closed invariant forms; a prescribed-class separator need only annihilate exact invariant forms. No fixed-class conclusion follows from the Comparator existence target.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/342.md) · [Batch record](../../batches/B038/README.md)
