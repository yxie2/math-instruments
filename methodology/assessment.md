# Assessment and evidence

- **Reading is not verification.** The initial extraction and subsequent mathematical review included checks of selected statements, hypotheses and identities; those checks do not independently certify every underlying proof. No Lean formalization was built or kernel-checked during either stage. Absence of a check in this survey says nothing about whether other people have checked a manuscript.

- **Novelty assessments depend on the search scope.** “No precedent found” means that the literature comparison described in the card found no matching instrument; a device in a 1980s Russian paper or an unpublished talk could be missed. The verdicts are provisional judgments relative to the literature searched; the subsequent mathematical review did not independently validate them, and mixed labels are not counted as disjoint classes.

- **Initial choice of thirty-eight.** B001 selected 38 of the release's 372 families for the prominence of the problems, favoring major conjectures and particularly strong claims. Later batches broaden the selection across subjects, including improvements to existing bounds. Current counts and pending families appear in the [coverage table](../tables/coverage.md). A family is marked catalogued when selected instruments have records, not when every associated manuscript has been fully audited.

- **Search coverage.** Some entries in the second group used directly retrieved primary sources without a fresh literature search. Their novelty assessments have correspondingly narrower support.

- **Priority and AI lineage.** At least four results have close human or AI-assisted neighbours predating the release (Naimark: Tanaka; Crouzeix: Jin, Lorist–Schwenninger, Luo; Borsuk: a 63-dimensional GitHub note; Serre positivity: a December 2025 AI note). This survey records these; it does not adjudicate priority.

- **Scope of the extracted novelty.** The extraction identified devices within proofs. It did not identify a new foundational theory, a new category of object comparable to motives or perfectoid spaces, or a new conjecture. This describes what the extraction found in the selected families; it is not an exhaustive claim about their contents or the full release.

## Independent dimensions

- **Novelty:** preserve the actual comparison and mixed verdicts; a family-level verdict is not automatically an instrument-level verdict.
- **Mathematical review:** state exactly which statement, identity, argument or dependency was checked and where the evidence is recorded.
- **Formalization:** distinguish supplied files, inspected declarations, compilation and kernel checking.
- **Reuse:** record proposed, attempted and demonstrated applications separately from extraction.

B001 imports the direction paper’s descriptions and assessments. The repository import adds no independent proof verification. Source titles and headline statements describe the source manuscripts’ claims. No Lean project was built for B001.

B002–B044 add exact source labels and hashes, selected argument readings, targeted antecedent comparisons and finite verification programs. Their [aggregate audit](../batches/B045/README.md) checks reproducibility and provenance. A program that verifies a finite identity or sampled example does not establish an asymptotic theorem, an infinite-dimensional limit or the truth of every dependency. Comparator files containing `sorry` are theorem targets, not evidence of a completed proof. Curation patterns connect methods and proposed uses without increasing the extraction or demonstrated-application counts.
