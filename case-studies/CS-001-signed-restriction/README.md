# Signed restriction and fixed-depth circuit lower bounds

Status: public preprint with proofs.

**Ying Xie — [From Signed Restrictions to Lower Bounds at Every Fixed Depth](https://zenodo.org/records/23429046)**. Preprint, October 17, 2026. [DOI: 10.5281/zenodo.23429046](https://doi.org/10.5281/zenodo.23429046).

Can a lemma extracted from a depth-three circuit argument remain useful after several rounds of classical depth reduction? This study follows the signed restriction lemma from family [112](../../catalog/families/openai-math-112.md) into that question. It extends the source's stated depth-three lower bound to every fixed depth for the same polynomial-time language. The application illustrates the research approach of the [direction paper](https://zenodo.org/records/23319145): isolate a reusable mechanism, identify the extra conditions needed in a new setting, and develop the argument around it.

## Extracted input

- [MI-000083: Restriction bound independent of clause count](../../catalog/instruments/MI-000083.md), extracted from Section 3, Lemma 3.1 of [Beyond the Square-Root Exponent for Depth-Three Boolean Circuits](../../catalog/papers/P-000026.md).

The source is pinned to OpenAI repository revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Its signed expansion expresses a restricted width-$`k`$ CNF in terms of width-$`b`$ CNFs. The resulting correlation bound has a nonnegative multiplier with bounded expected value, independent of the number of clauses. The source also supplies the evaluator language used in the application.

## Target and adaptation

Classical switching reduces a fixed-depth circuit to an OR of CNFs whose clauses depend on earlier random restrictions. A direct reuse of the extracted lemma must therefore handle these adaptive choices and the fact that the coefficient-mass bound holds in expectation.

Section 2 supplies an adaptive averaging lemma. Conditional on the preceding restriction history, it applies the signed restriction bound to a freshly restricted CNF. It then separates the event where narrow-CNF correlations are small from its complement. This permits the earlier choices to depend on their history while retaining the fresh randomness required by the argument.

Section 3 develops the hard-slice correlation estimate for the required retention probabilities. Section 4 combines it with successive depth reduction, error accounting and normalization of circuits with shared gates. Appendix A makes the width dependence of classical disjoint sparsification explicit, allowing the testing width to grow as $`\log n/\log\log n`$.

## Results and evidence

**Theorem 1.1** states that one language $`L\in\mathsf P`$, namely the evaluator language of family 112, has membership functions $`f_n`$ satisfying

```math
S_D(f_n)\ge 2^{\Omega_D\left((n\log n/\log\log n)^{1/(D-1)}\right)}
\qquad\text{for every fixed integer }D\ge3
```

at all sufficiently large input lengths $`n`$. Here $`S_D`$ counts AND/OR gates in exact circuits of depth at most $`D`$, allowing arbitrary finite fan-in and fan-out, shared gates, input negations and constants. The language is independent of $`D`$; the implicit constants and the sufficient input length may depend on $`D`$.

In particular, for each fixed depth, the ratio $`\log S_D(f_n)/n^{1/(D-1)}`$ tends to infinity. **Theorem 1.2 and Appendix B** give an explicit sufficient length threshold and a quantitative gate-count bound. Section 5 describes the remaining question of whether the method can yield a fixed positive power improvement in the exponent; the stated theorem gives a logarithmic improvement.

The linked preprint supplies the proofs and attributes the signed restriction lemma and evaluator language to the OpenAI source. Classical switching and sparsification are cited separately. The catalogue's source-review and novelty assessments remain separate from this application record; see the [assessment policy](../../methodology/assessment.md).

## What this use case demonstrates

The useful feature of the extracted instrument is its independence from clause count. Depth reduction can create CNFs with many clauses, while the signed restriction estimate still controls their correlation. Reuse requires an additional averaging argument and quantitative control of the testing width. Together these steps carry a source mechanism into a theorem for every fixed circuit depth.

## Publication and references

- [Application paper and publication metadata on Zenodo](https://zenodo.org/records/23429046).
- [Download the application PDF](https://zenodo.org/api/records/23429046/files/paper.pdf/content).
- [Direction paper: What the Machine Invented](https://zenodo.org/records/23319145).
- [Original source manuscript and pinned version](../../catalog/papers/P-000026.md).

The Zenodo paper is authored by Ying Xie and released under CC BY 4.0. Its acknowledgment records the author's guidance and responsibility and GPT-6 assistance with exploration, proof development, code checks and drafting.
