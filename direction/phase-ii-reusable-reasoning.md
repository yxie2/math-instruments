# Second direction paper: reusable reasoning

**Ying Xie. From Mathematical Instruments to Reusable Reasoning: A Second Phase of Extraction from AI-Generated Mathematics.** Preprint, 2026.

[Read the paper on Zenodo](https://zenodo.org/records/23523260) · [Research direction](README.md) · [Math Instruments](../README.md)

## From instruments to reasoning graphs

Large collections of AI-generated mathematics create a research problem: how can their arguments become a cumulative resource for further mathematics? The [first direction paper](https://zenodo.org/records/23319145) identifies mathematical instruments and recurring proof mechanisms. This second paper reconstructs their dependencies as source-linked reasoning graphs.

The graphs represent claims and joint-premise inferences as directed hypergraphs. They retain the hypotheses, scope conditions, source passages and evidence status needed to assess a proposed route. Transfer records identify the mechanism being reused, application-specific adaptations and remaining proof obligations.

## Studies and visualization

The paper distinguishes three stages: a selected-argument query pilot, an earlier four-paper statement/proof inventory (RB001), and a six-paper semantic study (G001). The pilot's twenty query scenarios are separate from the six-paper study.

G001 contains four OpenAI papers and two retrospective application papers by Ying Xie. Its records cover 105 proof environments, 158 arguments, 454 inferences and 1,760 nonblank source blocks, at the level of mathematical argument steps. A multiscale viewer connects the collection, a paper's argument map, individual inferences and exact source passages. The paper includes visualization screenshots and complete reasoning graphs for selected arguments.

The retrospective applications concern [signed restrictions and fixed-depth circuit lower bounds](../case-studies/CS-001-signed-restriction/README.md) and [quantum decoding and subset bounds](../case-studies/CS-003-quantum-subset/README.md). They show how signed restrictions, cubic-moment optimization and polynomial certificates require additional mathematical work in a new setting.

## Research direction and evidence

The proposed research cycle connects a question or candidate hypothesis to relevant mechanisms, a proposed reasoning graph, explicit transfer obligations, mathematical investigation and verification, and the return of reviewed outcomes to the collection. Automatically suggesting hypotheses from curated graphs, with candidate routes and explicit proof obligations, is a proposed extension.

Author review led to corrections of premises, scope and source anchors; the paper reports its coverage and remaining limits. Source accounting, mathematical validity, novelty and discovery performance remain distinct. The study is an exploratory preprint, and independent peer review, blinded annotation evaluation and prospective discovery studies remain future work.

## Paper and companion materials

The public paper is linked through its [Zenodo record](https://zenodo.org/records/23523260), following the first direction paper's publication convention. Appendix B describes the implementation, source snapshots and audit records prepared locally for a separate data and software release. The manuscript source package contains the text, figures and tables needed to compile the paper; it does not include the study implementation and data.

Author: **Ying Xie**, Kennesaw State University, yxie2@kennesaw.edu. The paper's acknowledgment records AI and software assistance and the author's responsibilities.

For the reusable reasoning methodology, cite this second direction paper. For instrument extraction, cite the first direction paper. Cite source manuscripts for their mathematical contributions and identify the repository release or commit when using catalog records. Both direction papers are identified in [CITATION.cff](../CITATION.cff).
