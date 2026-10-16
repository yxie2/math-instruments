---
id: openai-math-237
record_type: family
title: Joint renewal laws and transfer of finite bridge estimates
source_family: '237'
source_collection: openai/math
batch_id: B080
subject: Probability and statistical mechanics
source_paper_ids:
- P-000500
instrument_ids:
- MI-000746
- MI-000747
headline: The family claims honeycomb walk and polygon exponents, bridge laws and changes of measure.
central_instrument: Cut at a marked irreducible piece to expose two renewal factors; use discounted bad-piece
  counts and truncated rewards to transfer finite-mass estimates.
novelty_assessment: Classical ingredients are credited; exact novelty of the source-specific assembly
  is not established.
formalization_summary: HoneycombFreeEnergy targets existence of a fixed-length forced free-energy limit,
  for all initial vertices, directions and real forces. It does not state the small-force exponent or
  the 3/4 spatial law. Full scope and named Comparator read. Other linked targets were not inspected.
  The inspected target includes sorry; no separate solution or Lean build was checked.
statement_faithfulness: Irreducible height is positive. Length, height, displacement and diameter of the
  same piece remain jointly distributed. The finite bridge exponent estimates are assumptions of this
  extraction.
dependencies: Unique bridge factorization, nonnegative generating functions, marked-piece bijections and
  elementary tail/Laplace bounds.
antecedents: Classical renewal-reward identities, geometric series and dyadic Borel-Cantelli estimates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Joint renewal laws and transfer of finite bridge estimates

## Source manuscripts and claim

- [Renewal and changes of law for critical honeycomb walks](../papers/P-000500.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Radial transfer estimates and polygon length laws for honeycomb walks](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Radial-transfer-estimates-and-polygon-length-laws-for-honeycomb-walks-September-26-2026)
- [Critical honeycomb chords with prescribed boundary endpoints](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026)
- [Cylinder loop weights and planar nesting](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026)
- [Mass and covering exponents for fixed-length honeycomb walks](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026)
- [Signed cylinder propagation and marked polygons on the honeycomb lattice](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Signed-cylinder-propagation-and-marked-polygons-on-the-honeycomb-lattice-September-26-2026)
- [Cylinder amplitudes and logarithmic bridge-length windows on the honeycomb lattice](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Cylinder-amplitudes-and-logarithmic-bridge-length-windows-on-the-honeycomb-lattice-September-26-2026)
- [Marked polygon correlations and one-arc bounds](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Marked-polygon-correlations-and-one-arc-bounds-September-26-2026)
- [Disk transfer representations and confined bridge mass](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Disk-transfer-representations-and-confined-bridge-mass-September-26-2026)
- [Polynomial vacuum representations and bridge mass for honeycomb walks](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026)
- [Critical strip-crossing mass on the honeycomb lattice](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-strip-crossing-mass-on-the-honeycomb-lattice-September-26-2026)
- [Uniform marked-polygon estimates and sharp finite bridge moments](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-marked-polygon-estimates-and-sharp-finite-bridge-moments-September-26-2026)
- [Cap-selected amplitudes and triangle chords for honeycomb walks](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Cap-selected-amplitudes-and-triangle-chords-for-honeycomb-walks-September-26-2026)

The family claims honeycomb walk and polygon exponents, bridge laws and changes of measure.

## Extracted instruments

- [MI-000746: Mark one renewal piece to obtain a two-sided reward convolution](../instruments/MI-000746.md)
- [MI-000747: Use discounted bad-piece mass and truncated rewards to control a joint renewal law](../instruments/MI-000747.md)

## Dependencies and antecedents

Unique bridge factorization, nonnegative generating functions, marked-piece bijections and elementary tail/Laplace bounds.

Classical renewal-reward identities, geometric series and dyadic Borel-Cantelli estimates.

## Review and formalization scope

Read the full factorization, additive-reward, joint-increment and sum-growth proofs in the renewal companion. Twelve other manuscripts are inventory-only, including the family lead paper. Their finite bridge estimates are not certified.

HoneycombFreeEnergy targets existence of a fixed-length forced free-energy limit, for all initial vertices, directions and real forces. It does not state the small-force exponent or the 3/4 spatial law. Full scope and named Comparator read. Other linked targets were not inspected. The inspected target includes sorry; no separate solution or Lean build was checked.

Irreducible height is positive. Length, height, displacement and diameter of the same piece remain jointly distributed. The finite bridge exponent estimates are assumptions of this extraction.

[Batch record](../../batches/B080/README.md)
