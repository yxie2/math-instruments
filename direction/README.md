# Research direction

The project treats OpenAI’s mathematical manuscript release as a treasure mine of ideas. It begins by extracting candidate new lemmas, constructions, inequalities, objects, structures and proof mechanisms. Their validity, novelty and possible reuse are then investigated.

## First direction paper: mathematical instruments

Ying Xie. *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*. Preprint, 2026.

[Zenodo record](https://zenodo.org/records/23319145) · [Import edition](../editions/zenodo-23319145/README.md) · [References](references.md)

The paper establishes the project’s motivation and extraction method, describes 38 selected families, and presents eleven recurring patterns. It also introduces a subsequent application of the signed restriction lemma from family 112.

## Second direction paper: reusable reasoning

Ying Xie. *From Mathematical Instruments to Reusable Reasoning: A Second Phase of Extraction from AI-Generated Mathematics*. Preprint, 2026.

[Zenodo record](https://zenodo.org/records/23523260) · [Phase II overview](phase-ii-reusable-reasoning.md)

The second paper reconstructs the arguments behind reusable instruments as source-linked reasoning graphs. Claims and joint-premise inferences retain their scope conditions, evidence and review history. A six-paper study and multiscale visualization illustrate how researchers can inspect dependencies and identify the additional work required for transfer. Collection-guided hypothesis suggestions with explicit proof obligations are proposed as a further research direction.

## Relationship to the catalog

The papers establish successive stages of the research direction: extracting instruments, then reconstructing and comparing the reasoning that supports their reuse. This repository is the living collection: later batches can add instruments, revise comparisons, record corrections and document case studies without changing what either published paper originally reported. The Phase II paper describes implementation and data prepared locally for a separate release; adding the paper here does not publish that software or those records.

## Author and assistance

Ying Xie, Kennesaw State University, yxie2@kennesaw.edu.

The following acknowledgment concerns the first direction paper. The second paper records its assistance and author responsibilities in its own acknowledgment.

Claude Fable 5.1 was used for the initial extraction of mathematical instruments, literature comparisons and preliminary novelty assessments. The author thanks OpenAI’s GPT-6 for assistance with mathematical review and draft revision. The author takes responsibility for the establishment of this research direction, design of the methodology, the curation and interpretation of the extracted material, the development of the use case studies, and the presentation of the final manuscript.
