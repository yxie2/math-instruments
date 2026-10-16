---
id: openai-math-310
record_type: family
title: Saturated residues and augmented product shuffles
source_family: '310'
source_collection: openai/math
batch_id: B025
subject: Topology
source_paper_ids:
- P-000172
instrument_ids:
- MI-000306
- MI-000307
headline: The source claims that for every finite group G and prime p, a trivial normal p-core forces
  nonzero augmented reduced rational homology of the poset of nonidentity elementary abelian p-subgroups.
central_instrument: Extract a chain residue at a fully saturated initial flag. Combine cycles in commuting
  factors through an explicitly signed staircase shuffle that includes degree minus one.
novelty_assessment: Residues at initial flags and join shuffle maps are elementary established chain constructions.
  The source records the saturation and augmentation conventions needed for propagation; the global group-theoretic
  theorem is not certified.
formalization_summary: No family-specific scope document or Comparator target is listed for this family.
  No Lean artifact was built or kernel-checked.
statement_faithfulness: The empty poset has reduced homology Q in degree -1. Residues require ranks 1
  through r with no gaps, and product coordinates require commuting factors with trivial intersection.
dependencies: Augmented simplicial boundaries, saturated rank flags, commuting subgroup products and staircase
  triangulation of products of cones.
antecedents: Classical simplicial chain residues, join boundaries and signed Eilenberg-Zilber-type shuffles.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Saturated residues and augmented product shuffles

## Source manuscript and claim

[Rational homology and Quillen's conjecture](../papers/P-000172.md), by OpenAI, September 24, 2026.

The source claims that for every finite group G and prime p, a trivial normal p-core forces nonzero augmented reduced rational homology of the poset of nonidentity elementary abelian p-subgroups.

## Extracted instruments

- [MI-000306: A saturated initial flag defines a signed chain residue](../instruments/MI-000306.md)
- [MI-000307: Shuffle augmented flags into a product without losing the join sign](../instruments/MI-000307.md)

## Dependencies and antecedents

Augmented simplicial boundaries, saturated rank flags, commuting subgroup products and staircase triangulation of products of cones.

Classical simplicial chain residues, join boundaries and signed Eilenberg-Zilber-type shuffles. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete saturated-residue and product-shuffle proofs, including empty flags and the join realization. The faithful-component propagation, frame coefficient estimates and classification-dependent reductions were not audited.

No family-specific scope document or Comparator target is listed for this family. No Lean artifact was built or kernel-checked.

The empty poset has reduced homology Q in degree -1. Residues require ranks 1 through r with no gaps, and product coordinates require commuting factors with trivial intersection.

[Batch record](../../batches/B025/README.md)
