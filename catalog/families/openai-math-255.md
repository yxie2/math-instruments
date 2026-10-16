---
id: openai-math-255
record_type: family
title: Shape-independent Haar comparison and recurrence with intermediate constraints
source_family: '255'
source_collection: openai/math
batch_id: B031
subject: Group theory
source_paper_ids:
- P-000195
instrument_ids:
- MI-000352
- MI-000353
headline: The source claims quasi-isometric recognition of virtually polycyclic groups, with a finite-index
  uniform-lattice realization in a possibly different solvable Lie group.
central_instrument: Averaging translated sets compares Radon and Haar mass without absolute continuity.
  A positive convolution operator supplies nested sets whose successive random transitions remain in a
  prescribed measurable set.
novelty_assessment: Both selected arguments use classical Tonelli, doubling and Cauchy-Schwarz tools.
  The extraction records uniformity in set shape and all intermediate-state constraints, without certifying
  global quasi-isometric recognition.
formalization_summary: 'Read PolycyclicRecognition.lean: recognition, finite-index lattice realization
  and a uniform bounded-height theorem are stated as sorry targets. No Lean build was performed.'
statement_faithfulness: The Haar comparison constant is independent of set diameter but the averaging
  radius may depend on it. The recurrence increments have law sigma times inverse-sigma, and the number
  of stages is fixed for the subexponential conclusion.
dependencies: Unimodularity, large-scale volume doubling, Tonelli, Cauchy-Schwarz and independent conditional
  transitions.
antecedents: Classical invariant-measure averaging and positive convolution recurrence; no exhaustive
  priority claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Shape-independent Haar comparison and recurrence with intermediate constraints

## Source manuscript and claim

[Quasi-isometric recognition of virtually polycyclic groups](../papers/P-000195.md), by OpenAI, September 24, 2026.

The source claims quasi-isometric recognition of virtually polycyclic groups, with a finite-index uniform-lattice realization in a possibly different solvable Lie group.

## Extracted instruments

- [MI-000352: Compare Radon masses to Haar volumes uniformly over translated set shapes](../instruments/MI-000352.md)
- [MI-000353: Choose nested recurrence sets before sampling a sequence of transitions](../instruments/MI-000353.md)

## Dependencies and antecedents

Unimodularity, large-scale volume doubling, Tonelli, Cauchy-Schwarz and independent conditional transitions.

Classical invariant-measure averaging and positive convolution recurrence; no exhaustive priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full Haar-averaging and backward-recurrence proofs. The polynomial-image, stationary-profile, neighboring-label and recognition arguments were not audited.

Read PolycyclicRecognition.lean: recognition, finite-index lattice realization and a uniform bounded-height theorem are stated as sorry targets. No Lean build was performed.

The Haar comparison constant is independent of set diameter but the averaging radius may depend on it. The recurrence increments have law sigma times inverse-sigma, and the number of stages is fixed for the subexponential conclusion.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/255.md) · [Batch record](../../batches/B031/README.md)
