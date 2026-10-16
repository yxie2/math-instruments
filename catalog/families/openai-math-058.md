---
id: openai-math-058
record_type: family
title: Liouville covers and proper intrinsic distances
source_family: 058
source_collection: openai/math
batch_id: B070
subject: Algebraic and complex geometry
source_paper_ids:
- P-000435
- P-000436
instrument_ids:
- MI-000666
- MI-000667
headline: The family claims a classification of semialgebraic universal covers and symmetry of bounded
  domains with compact quotient.
central_instrument: Minimal positive harmonic rays become deck characters whose logarithmic differential
  has zero energy. Uniform local compactness propagates to all balls of an intrinsic distance.
novelty_assessment: The selected tools use established mechanisms. Exact source-specific rounding and
  lattice interfaces have not received exhaustive priority checks. No headline theorem is certified.
formalization_summary: The scope and all of SymmetricDomains were read. The target assumes a connected
  bounded semialgebraic relatively open subset of an affine algebraic set, a proper holomorphic action
  by a discrete group, and compact orbit quotient. It concludes smoothness and biholomorphism with a bounded
  symmetric domain; freeness is not assumed. This target belongs to the bounded-domain manuscript, not
  the full universal-cover classification. It has a sorry body. No separate solution or Lean build was
  checked.
statement_faithfulness: Liouville uses a regular virtually abelian cover of a compact Kahler base. The
  distance argument starts after smoothness is supplied and uses a bounded embedding and cocompact biholomorphic
  action.
dependencies: Harnack estimates, elliptic compactness, Krein-Milman, divergence integration, Schwarz contraction
  and finite disc chains.
antecedents: Lyons-Sullivan Liouville theorem and classical Kobayashi-distance completeness arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Liouville covers and proper intrinsic distances

## Source manuscripts and claim

- [Semialgebraic universal covers of normal projective varieties](../papers/P-000435.md): selected passages extracted.
- [Symmetry of semialgebraic bounded domains with compact quotient](../papers/P-000436.md): selected passages extracted.

The family claims a classification of semialgebraic universal covers and symmetry of bounded domains with compact quotient.

## Extracted instruments

- [MI-000666: Kill an abelian deck character by integrating the logarithmic energy](../instruments/MI-000666.md)
- [MI-000667: Propagate uniform local compactness to properness of a disc-chain distance](../instruments/MI-000667.md)

## Dependencies and antecedents

Harnack estimates, elliptic compactness, Krein-Milman, divergence integration, Schwarz contraction and finite disc chains.

Lyons-Sullivan Liouville theorem and classical Kobayashi-distance completeness arguments.

## Review and formalization scope

Read the full Liouville proof and full proper-distance and continuity-principle proofs. Both manuscripts receive extractions. Smoothness, scaling, symmetry and the complete cover classification are not certified.

The scope and all of SymmetricDomains were read. The target assumes a connected bounded semialgebraic relatively open subset of an affine algebraic set, a proper holomorphic action by a discrete group, and compact orbit quotient. It concludes smoothness and biholomorphism with a bounded symmetric domain; freeness is not assumed. This target belongs to the bounded-domain manuscript, not the full universal-cover classification. It has a sorry body. No separate solution or Lean build was checked.

Liouville uses a regular virtually abelian cover of a compact Kahler base. The distance argument starts after smoothness is supplied and uses a bounded embedding and cocompact biholomorphic action.

[Batch record](../../batches/B070/README.md)
