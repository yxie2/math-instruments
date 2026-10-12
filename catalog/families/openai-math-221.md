---
id: openai-math-221
record_type: family
title: Mézard–Parisi formula for diluted spin glasses
source_family: '221'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Operator algebras, topology and symplectic geometry
source_paper_ids:
- P-000061
instrument_ids:
- MI-000092
- MI-000093
- MI-000094
headline: Mézard–Parisi formula for diluted spin glasses
central_instrument: '“Depth shift”: couple to a finite auxiliary hierarchy by marked Poisson perturbations and shift every target branching depth by one level so divisions by small coefficients stay bounded, proving the factorization Panchenko left open.'
novelty_assessment: new
formalization_summary: files, not in catalogue
statement_faithfulness: yes, faithful statement
dependencies: 'no'
antecedents: Mourrat–Panchenko; Barbier–Panchenko
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 405 files, not in catalogue new
map_formalization_summary: yes (not in catalogue)
---

# Mézard–Parisi formula for diluted spin glasses

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000061](../papers/P-000061.md)

## Family description

Source status as recorded in the direction paper: Lean, 405 files, not in catalogue new

For Poisson-diluted even-arity models whose interaction law satisfies the Panchenko–Talagrand factorization and positivity hypotheses (model-class conditions, verified for Viana–Bray and soft K-SAT, not assumptions on the Gibbs measure), the free energy equals the infimum over finite-depth hierarchical trial laws, with only first-moment integrability. The lower bound is stated for every bounded interaction whose law is permutation invariant, without the even-arity or factorization restrictions needed for the matching upper bound. Under the stated model-class hypotheses, no additional Gibbs-measure factorization assumption is imposed; establishing that factorization is the step Panchenko’s conditional results left open.

## Extracted instruments.

- [MI-000092: Marked-depth Poisson perturbations with prescribed-tree identities](../instruments/MI-000092.md)

- [MI-000093: Depth shift with charging fresh splits](../instruments/MI-000093.md)

- [MI-000094: Recursive law encoding of a single site](../instruments/MI-000094.md)

## Reused.

Guerra, Franz–Leone and Panchenko–Talagrand interpolation (upper bound, reproved); Aizenman–Sims–Starr cavity; Panchenko’s spin-distribution viewpoint; Ruelle probability cascades; Efron–Stein.

## Caveats.

The architecture and selected estimates in §8 were inspected, without checking every inequality. The repository supplies a Lean development with review status “unchecked”; it was not compiled here. A textual search for admitted proofs would not establish kernel verification.

## Recorded assessment

- Novelty: new
- Formalization: files, not in catalogue
- Statement coverage: yes, faithful statement
- Dependencies: no
- Antecedents: Mourrat–Panchenko; Barbier–Panchenko
