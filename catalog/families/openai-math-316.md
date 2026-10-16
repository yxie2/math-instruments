---
id: openai-math-316
record_type: family
title: Cartier halving with an exponent floor and primitive square roots
source_family: '316'
source_collection: openai/math
batch_id: B025
subject: Topology
source_paper_ids:
- P-000174
instrument_ids:
- MI-000310
- MI-000311
headline: The source claims that the positive stable mod-two Hurewicz image of the sphere is spanned by
  Hopf-invariant-one and existing Kervaire-invariant-one images, with the corresponding sphere case of
  Eccles conjecture.
central_instrument: Track the exact smallest Dickson exponent under Cartier degree halving. Recover a
  primitive, Steenrod-annihilated square root from a decomposable primitive in a connected polynomial
  Hopf algebra.
novelty_assessment: Cartier/Kameko halving, Dickson ideal transformations and primitive-root arguments
  have classical foundations. The cards preserve the source exponent threshold and reducedness assumptions.
  The Curtis classification and its tensor obstruction are not certified.
formalization_summary: No family-specific scope document or Comparator target is listed for this family.
  No Lean artifact was built or kernel-checked.
statement_faithfulness: The headline does not assert existence of Kervaire classes in new degrees. Above-floor
  monomials satisfy a strict exponent inequality and parity constraints. Primitive-root uniqueness uses
  injective Frobenius in both the algebra and its tensor square.
dependencies: Binomial parity, Cartan formula, Dickson Jacobian, Milnor coinvariants, triangular polynomial
  derivations and Frobenius injectivity.
antecedents: Cartier and Kameko squaring; Hung and Giambalvo-Peterson on polynomial and Dickson algebra
  transformations; elementary structure of polynomial Hopf algebras.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Cartier halving with an exponent floor and primitive square roots

## Source manuscript and claim

[The Stable Hurewicz Image of the Sphere at Two](../papers/P-000174.md), by OpenAI, September 25, 2026.

The source claims that the positive stable mod-two Hurewicz image of the sphere is spanned by Hopf-invariant-one and existing Kervaire-invariant-one images, with the corresponding sphere case of Eccles conjecture.

## Extracted instruments

- [MI-000310: Cartier halving carries an explicit Dickson exponent floor](../instruments/MI-000310.md)
- [MI-000311: A decomposable primitive in a polynomial Hopf algebra has a primitive root](../instruments/MI-000311.md)

## Dependencies and antecedents

Binomial parity, Cartan formula, Dickson Jacobian, Milnor coinvariants, triangular polynomial derivations and Frobenius injectivity.

Cartier and Kameko squaring; Hung and Giambalvo-Peterson on polynomial and Dickson algebra transformations; elementary structure of polynomial Hopf algebras. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the Milnor quotient and coinvariant calculations, complete Cartier proof, suspension-kernel discussion and complete primitive-root proof. The Tor injection, full tensor obstruction, fourth-power exclusion and spherical-class classification were not audited.

No family-specific scope document or Comparator target is listed for this family. No Lean artifact was built or kernel-checked.

The headline does not assert existence of Kervaire classes in new degrees. Above-floor monomials satisfy a strict exponent inequality and parity constraints. Primitive-root uniqueness uses injective Frobenius in both the algebra and its tensor square.

[Batch record](../../batches/B025/README.md)
