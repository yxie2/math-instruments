---
id: openai-math-017
record_type: family
title: Irrationality exponent of π is 2
source_family: '017'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Number theory and arithmetic geometry
source_paper_ids:
- P-000067
instrument_ids:
- MI-000007
- MI-000008
- MI-000009
headline: Irrationality exponent of $`\pi`$ equals 2
central_instrument: '“Separated-weight interpolation”: jets at translates on the exponential curve with anisotropic weights chosen independently of the centers, while the sufficiently large degree threshold may depend on them, proved by a Dyson-type curve inequality pushed through nef/ample and Serre vanishing on a weighted blow-up.'
novelty_assessment: combination bordering new
formalization_summary: files, not in catalogue
statement_faithfulness: yes (eventual bound and sSup form)
dependencies: 'no'
antecedents: Masser 1981; Fischler–Nakamaye 2014
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 867 files, not in catalogue combination bordering new logarithm extension requires a separate argument
map_formalization_summary: 'yes'
---

# Irrationality exponent of π is 2

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000067](../papers/P-000067.md)

## Family description

Source status as recorded in the direction paper: Lean, 867 files, not in catalogue combination bordering new logarithm extension requires a separate argument

For every $`\nu>2`$ and all large q, $`|\pi-p/q|\ge q^{-\nu}`$; hence the Flint–Hills series converges. The previous bound cited by the initial extraction is 7.103 (Zeilberger–Zudilin 2020). The threshold is ineffective.

## Extracted instruments.

- [MI-000007: Separated-weight interpolation](../instruments/MI-000007.md)

- [MI-000008: Weighted transverse multiplicity](../instruments/MI-000008.md)

- [MI-000009: Two ways to make the determinant small](../instruments/MI-000009.md)

## Reused.

Laurent’s interpolation determinants; Roth’s separated denominators; Philippon zero estimates; Demailly’s jets; Mondal’s weighted Bézout; Stacks Project.

## Caveats.

An analogue with centers $`(r^j,jp_i/q_i)`$ for $`r\in\mathbb Q_{>0}\setminus\{1\}`$ is a proposed extension. The claim $`\mu(\log r)=2`$ needs a separate proof, including the interpolation hypotheses, rational-height costs and determinant estimates. It is not established by the source comparison in this survey. The initial extraction also flags the interpolation argument’s nearest prior art as requiring closer comparison.

## Recorded assessment

- Novelty: combination bordering new
- Formalization: files, not in catalogue
- Statement coverage: yes (eventual bound and sSup form)
- Dependencies: no
- Antecedents: Masser 1981; Fischler–Nakamaye 2014
