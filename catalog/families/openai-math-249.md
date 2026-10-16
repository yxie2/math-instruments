---
id: openai-math-249
record_type: family
title: Local degree and quadratic cancellation for word equations
source_family: '249'
source_collection: openai/math
batch_id: B030
subject: Group theory
source_paper_ids:
- P-000192
instrument_ids:
- MI-000346
- MI-000347
headline: The source claims a finitely generated residually finite group of integral cohomological dimension
  two and geometric dimension three.
central_instrument: Cyclic conjugation localizes word-map degree to an invariant isolating set. Exact
  translated relator counts suppress first-order errors in products of conjugated small quaternion defects.
novelty_assessment: Global word-map degree is classical Gerstenhaber-Rothaus theory. The selected invariant-fiber
  localization is more specific than that global formula; a targeted comparison does not establish first
  priority. The cancellation mechanism combines exact chain counts with elementary quaternion estimates.
formalization_summary: Read EilenbergGanea.lean. Its explicit height-kernel group is required to be finitely
  generated and residually finite, have integral cohomological dimension two, admit a three-dimensional
  classifying CW space and admit no two-dimensional one. The inspected Comparator contains a sorry target;
  no Lean build or kernel verification was performed.
statement_faithfulness: The localized degree lemma requires coefficient-free words, a nonsingular exponent-sum
  matrix, simultaneous-conjugation invariance, identity containment and an isolating boundary. The quadratic
  bound requires exact translated multiplicities, not merely approximate abelian cancellation.
dependencies: Mapping degree, finite cyclic conjugation, ordinary finite-dimensional Sard perturbations,
  an aligned cellular boundary basis and unit-quaternion product estimates.
antecedents: Gerstenhaber-Rothaus degree formula as stated in Frøyshov 2013, Proposition 2.1; standard
  degree theory and commutator estimates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Local degree and quadratic cancellation for word equations

## Source manuscript and claim

[A finitely generated counterexample to the Eilenberg–Ganea conjecture](../papers/P-000192.md), by OpenAI, September 23, 2026.

The source claims a finitely generated residually finite group of integral cohomological dimension two and geometric dimension three.

## Extracted instruments

- [MI-000346: Localize SU(2) word-map degree by cyclic conjugation](../instruments/MI-000346.md)
- [MI-000347: Convert exact translated relator counts into a uniform quadratic error](../instruments/MI-000347.md)

## Dependencies and antecedents

Mapping degree, finite cyclic conjugation, ordinary finite-dimensional Sard perturbations, an aligned cellular boundary basis and unit-quaternion product estimates.

Gerstenhaber-Rothaus degree formula as stated in Frøyshov 2013, Proposition 2.1; standard degree theory and commutator estimates. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete localized degree proof, exact translated-count proof and uniform quadratic estimate. The geometric seed, acyclic level model, arbitrary-presentation comparison and transport obstruction were not audited.

Read EilenbergGanea.lean. Its explicit height-kernel group is required to be finitely generated and residually finite, have integral cohomological dimension two, admit a three-dimensional classifying CW space and admit no two-dimensional one. The inspected Comparator contains a sorry target; no Lean build or kernel verification was performed.

The localized degree lemma requires coefficient-free words, a nonsingular exponent-sum matrix, simultaneous-conjugation invariance, identity containment and an isolating boundary. The quadratic bound requires exact translated multiplicities, not merely approximate abelian cancellation.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/249.md) · [Batch record](../../batches/B030/README.md)
