# Third direction paper: recursive reasoning exploration

**Ying Xie. Recursive Reasoning Exploration: Mathematical Research through Evolving Reasoning Graphs.**

**Case study: An Exact Certificate-Degree Theorem for Two-Term Tensor Decompositions.** Phase III of the Math Instruments Program. Preprint, published November 1, 2026.

[Read the paper on Zenodo](https://zenodo.org/records/23849757) · [DOI: 10.5281/zenodo.23849757](https://doi.org/10.5281/zenodo.23849757) · [Research direction](README.md) · [Math Instruments](../README.md)

## From extraction to exploration

The Math Instruments Program develops through three phases:

| Phase | Research focus | Paper |
| --- | --- | --- |
| I | Extract reusable mathematical instruments from research papers. | [What the Machine Invented](https://zenodo.org/records/23319145) |
| II | Reconstruct source-linked reasoning graphs with claims, jointly required premises, scope conditions and evidence. | [From Mathematical Instruments to Reusable Reasoning](phase-ii-reusable-reasoning.md) |
| III | Use and extend those graphs through mathematical exploration, retaining the path from a research target to its outcomes. | [Recursive Reasoning Exploration](https://zenodo.org/records/23849757) |

Recursive Reasoning Exploration (RRE) makes the evolving graph part of the research process. Researchers and AI agents select targets from existing knowledge, develop arguments, check results, record failed approaches and revise the graph. Newly established results and unresolved obligations can then generate further targets. The retained history supports replay, comparison of approaches and learning from mathematical research paths.

The framework accommodates human-directed, collaborative and goal-directed autonomous exploration, and proposes open-ended exploration as a further mode. The reported case study is an agent-led run with a human-specified objective.

## Case study: an exact certificate-degree theorem

The paper studies the polynomial equations for expressing a tensor as a sum of two rank-one tensors. When no such decomposition exists, a polynomial identity can certify that these equations have no common solution. Certificate degree is measured in the original decomposition variables, as the largest total degree of a product of an equation with its certificate multiplier.

The main theorem states that, for every complex tensor of order **n >= 2** and rank greater than two, the minimum certificate degree for the two-term decomposition equations is **exactly 3n**. The proof combines a matching lower bound, explicit certificates and a transfer argument with classical rank-two tensor geometry. It includes the W tensors of order at least three, whose matrix flattenings all have rank at most two.

A parallel investigation gives the bounds **3m + 3 <= delta_m(I_m, N) <= 3m + 6** for every **m >= 2** and every nonzero nilpotent complex m-by-m matrix N, where delta_m is the minimum certificate degree for the m-term decomposition equations of the tensor with slices I_m and N.

## How the graph develops

Six recorded graph revisions grow from **8 nodes and no inferences** to **68 nodes and 34 inferences**, alongside **44 exploration events**. They connect the initial objective, intermediate targets, mathematical arguments, exact arithmetic checks and subsequent extensions. The paper presents proofs of the general statements and identifies the finite computations used to check explicit certificates.

The visualizations show how each stage changes the graph. This connects a mathematical result to the research decisions and supporting arguments that produced it, while leaving reusable components available for subsequent exploration.

## Publication and associated materials

The Zenodo record provides the published manuscript PDF. The paper also describes companion reasoning graphs, checking programs and replay materials. This repository entry links the published paper; the associated software and data require a separate release.

For citation metadata, see [CITATION.cff](../CITATION.cff). The paper records assistance and author responsibilities in its own acknowledgment.
