---
id: openai-math-225
record_type: family
title: Energy bootstraps and finite-energy tests for six-vertex height limits
source_family: '225'
source_collection: openai/math
batch_id: B006
subject: Probability and statistical mechanics
source_paper_ids:
- P-000096
instrument_ids:
- MI-000148
- MI-000149
headline: The source claims a Gaussian free field limit for the iterated balanced-torus plane state throughout
  a=b=1 and 0<c<=2, with variance multiplier 1/arcsin(c/2). This extraction selects two auxiliary convergence
  mechanisms.
central_instrument: A double-commutator estimate upgrades low-energy compression to ordinary moment bounds;
  logarithmic variogram domination extends smooth-test limits to ordinary finite-energy signed measures.
novelty_assessment: Spectral energy methods, logarithmic potential theory and approximation of Gaussian
  fields are established. The extracted arguments are candidate useful packages in this source; the full-range
  theorem and historical priority are not certified.
formalization_summary: No family-specific formalization scope document is listed in the pinned release
  inventory. No Comparator comparison or Lean proof build is claimed.
statement_faithfulness: The source uses a specific zero-slope state obtained by taking one torus length
  to infinity before the other. It makes no uniqueness claim for all Gibbs states or uniform claim as
  c tends to zero. Ordinary signed-measure energy excludes cancellation between divergent positive and
  negative terms.
dependencies: The source’s positive endpoint Hamiltonian and low-band estimates; bounded local commutators;
  stationary increment variograms; absolute logarithmic energy; mollification and an L2 approximation
  argument.
antecedents: Duminil-Copin, Kozlowski, Lammers and Manolescu prove the six-vertex GFF theorem on sqrt(3)<=c<=2
  and provide several broader-range inputs. Earlier dimer GFF results and Bethe-ansatz formulas are established
  background, not new extractions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Energy bootstraps and finite-energy tests for six-vertex height limits

## Source manuscript and claim

[The Gaussian free field limit of the balanced six-vertex model with variance multiplier 1/arcsin(c/2)](../papers/P-000096.md), by OpenAI, September 23, 2026.

The source claims a Gaussian free field limit for the iterated balanced-torus plane state throughout a=b=1 and 0<c<=2, with variance multiplier 1/arcsin(c/2). This extraction selects two auxiliary convergence mechanisms.

## Extracted instruments

- [MI-000148: A double commutator upgrades low-energy compression to a moment bootstrap](../instruments/MI-000148.md)
- [MI-000149: Logarithmic variogram domination extends smooth limits to finite-energy signed measures](../instruments/MI-000149.md)

## Dependencies and antecedents

The source’s positive endpoint Hamiltonian and low-band estimates; bounded local commutators; stationary increment variograms; absolute logarithmic energy; mollification and an L2 approximation argument.

Duminil-Copin, Kozlowski, Lammers and Manolescu prove the six-vertex GFF theorem on sqrt(3)<=c<=2 and provide several broader-range inputs. Earlier dimer GFF results and Bethe-ansatz formulas are established background, not new extractions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the ordinary-moment proof, the endpoint-generator statement and its local domain justification, and the complete finite-energy extension argument. The thermodynamic Bethe-ansatz bounds, chiral collision argument and full-range normalization were not fully audited.

No family-specific formalization scope document is listed in the pinned release inventory. No Comparator comparison or Lean proof build is claimed.

The source uses a specific zero-slope state obtained by taking one torus length to infinity before the other. It makes no uniqueness claim for all Gibbs states or uniform claim as c tends to zero. Ordinary signed-measure energy excludes cancellation between divergent positive and negative terms.

[Batch record](../../batches/B006/README.md)
