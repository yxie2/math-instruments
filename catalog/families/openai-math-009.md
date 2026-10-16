---
id: openai-math-009
record_type: family
title: Ramification support bounds and exponent recovery by Euler derivations
source_family: 009
source_collection: openai/math
batch_id: B066
subject: Number theory
source_paper_ids:
- P-000399
- P-000400
instrument_ids:
- MI-000630
- MI-000631
headline: The family concerns function-field reconstruction from Milnor K-theory and Galois data.
central_instrument: Several fibers with few orders visible modulo a prime bound a separable map degree.
  Intersections of degree-p subfield cosets synchronize a unique power correction.
novelty_assessment: Classical ingredients and earlier closely related mechanisms are identified. No exhaustive
  novelty assessment or certification of the source headline is claimed.
formalization_summary: The Comparator targets injectivity of the perfect-closure reconstruction correspondence
  modulo Frobenius and ell-adic unit scaling in transcendence degree at least two. It does not target
  existence of reconstruction and belongs to the inventory-only Bogomolov-Pop companion. The scope document
  and complete linked Comparator were read. The target theorem bodies contain sorry; no separate solution
  or Lean build was checked.
statement_faithfulness: The degree bound assumes a separable curve map and genus control. Exponent recovery
  requires p-independent variables and excludes projective monomials.
dependencies: Riemann-Hurwitz with different, p-bases, Euler derivations and differential kernels.
antecedents: Stacks Project Tag 0C1F; Cadoret-Pirutka, section 3.4, on line recovery up to powers.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Ramification support bounds and exponent recovery by Euler derivations

## Source manuscripts and claim

- [Reconstruction of Function Fields from Mod-ℓ Milnor K-Theory](../papers/P-000399.md): selected passages extracted.
- [Reconstruction from Milnor K-theory modulo the characteristic](../papers/P-000400.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [The Bogomolov-Pop reconstruction theorem](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026)

The family concerns function-field reconstruction from Milnor K-theory and Galois data.

## Extracted instruments

- [MI-000630: Bound a curve-map degree using five fibers visible modulo a prime](../instruments/MI-000630.md)
- [MI-000631: Recover a common power correction from two subfield cosets](../instruments/MI-000631.md)

## Dependencies and antecedents

Riemann-Hurwitz with different, p-bases, Euler derivations and differential kernels.

Stacks Project Tag 0C1F; Cadoret-Pirutka, section 3.4, on line recovery up to powers.

## Review and formalization scope

Read the complete uniform-support proof and the complete characteristic-p intersection proof. The first card extracts only its final curve-map inequality; finite curve tests and valuation reconstruction remain inputs. Two of three manuscripts receive extractions; the Bogomolov-Pop companion is inventory-only.

The Comparator targets injectivity of the perfect-closure reconstruction correspondence modulo Frobenius and ell-adic unit scaling in transcendence degree at least two. It does not target existence of reconstruction and belongs to the inventory-only Bogomolov-Pop companion. The scope document and complete linked Comparator were read. The target theorem bodies contain sorry; no separate solution or Lean build was checked.

The degree bound assumes a separable curve map and genus control. Exponent recovery requires p-independent variables and excludes projective monomials.

[Batch record](../../batches/B066/README.md)
