---
id: openai-math-015
record_type: family
title: Entropy on restricted components and local quadratic Fourier duality
source_family: '015'
source_collection: openai/math
batch_id: B066
subject: Number theory
source_paper_ids:
- P-000405
- P-000406
instrument_ids:
- MI-000636
- MI-000637
headline: The sources concern equidistribution of prime-degree, quartic and sextic torus packets.
central_instrument: An entropy bound inherited by every dominated invariant probability excludes zero-entropy
  component mass. Quadratic Fourier duality converts a lattice integral into one for the inverse polar
  operator.
novelty_assessment: Classical ingredients and earlier closely related mechanisms are identified. No exhaustive
  novelty assessment or certification of the source headline is claimed.
formalization_summary: DukePrimeDegree targets volume-weighted complete packets of totally real prime
  degree at least five, with multiplier discriminant tending to infinity, arbitrary local homothety type,
  weak Haar convergence and tightness. It has no quartic or sextic target. The scope document and complete
  linked Comparator were read. The target theorem bodies contain sorry; no separate solution or Lean build
  was checked.
statement_faithfulness: The entropy argument assumes an invariant probability limit, ball estimates and
  an entropy criterion. The quadratic transform uses a self-dual lattice, correct polar operator and normalized
  Haar measure, including at p=2.
dependencies: Ergodic decomposition, entropy integration, compact tube coverings, p-adic Fourier transform
  and completing the square.
antecedents: Classical entropy decomposition and Weil quadratic Fourier transformation; the source cites
  ELMV for the ordinary-ball route.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Entropy on restricted components and local quadratic Fourier duality

## Source manuscripts and claim

- [Equidistribution of Prime-Degree Torus Packets with Arbitrary Local Type](../papers/P-000405.md): selected passages extracted.
- [Equidistribution of primitive quartic torus packets for arbitrary orders](../papers/P-000406.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Equidistribution of Primitive Sextic Torus Packets](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026)

The sources concern equidistribution of prime-degree, quartic and sextic torus packets.

## Extracted instruments

- [MI-000636: Force positive entropy in almost every invariant component by domination](../instruments/MI-000636.md)
- [MI-000637: Invert the polar operator in a self-dual lattice Gaussian integral](../instruments/MI-000637.md)

## Dependencies and antecedents

Ergodic decomposition, entropy integration, compact tube coverings, p-adic Fourier transform and completing the square.

Classical entropy decomposition and Weil quadratic Fourier transformation; the source cites ELMV for the ordinary-ball route.

## Review and formalization scope

Read the complete ball-to-entropy and restricted-component proofs, and the complete quadratic Fourier-transformation proof with its scalar-shift context. Two of three manuscripts receive extractions; the sextic companion is inventory-only. Packet counting, tightness and homogeneous classification are not independently established.

DukePrimeDegree targets volume-weighted complete packets of totally real prime degree at least five, with multiplier discriminant tending to infinity, arbitrary local homothety type, weak Haar convergence and tightness. It has no quartic or sextic target. The scope document and complete linked Comparator were read. The target theorem bodies contain sorry; no separate solution or Lean build was checked.

The entropy argument assumes an invariant probability limit, ball estimates and an entropy criterion. The quadratic transform uses a self-dual lattice, correct polar operator and normalized Haar measure, including at p=2.

[Batch record](../../batches/B066/README.md)
