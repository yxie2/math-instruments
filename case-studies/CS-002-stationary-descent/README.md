# Stationary descent and its information cost

Status: public preprint with proofs. Historical priority of the exact finite-state formula remains unresolved.

**Ying Xie — [From Extracted Instruments to Mathematical Insight: A Case Study in Stationary Descent](https://zenodo.org/records/23408425)**. Preprint, 2026. [DOI: 10.5281/zenodo.23408425](https://doi.org/10.5281/zenodo.23408425).

A stationary trajectory can usually move downward if occasional upward jumps restore its distribution. How much dependence between successive observations does this require? This study follows two catalogue entries from different subjects into that question. It is a worked example of the research approach in the direction paper: extract a useful mechanism, change the question, develop the mathematics, and compare the result with existing work.

## Extracted inputs

| Instrument | Part used in the exploration |
| --- | --- |
| [MI-000098: Backward intertwiner over an ergodic base](../../catalog/instruments/MI-000098.md) | The final obstruction to an almost-sure strict descent under a probability-preserving transformation. |
| [MI-000014: Two-frame entropy transfer of projection theorems](../../catalog/instruments/MI-000014.md) | Comparison of an event under a joint law and under the product of its marginals, followed by a mutual-information bound. |

The direction paper describes these mechanisms in family 293, Section 9.4.3, and family 074, Section 8.2.1, respectively ([arXiv v1](https://arxiv.org/html/2610.17090v1)). The relevant source records include [Backward intertwiners and a transitive commutant](../../catalog/papers/P-000025.md) and [The Kakeya maximal conjecture in three dimensions](../../catalog/papers/P-000058.md), pinned to OpenAI repository revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

The application re-proves the elementary descent obstruction and develops its probability arguments directly. It does not assume the full operator-theoretic or geometric headline claims as premises.

## Target and adaptation

Let $`X,Y`$ be real random variables with the same distribution, and let $`\varepsilon=\Pr(Y\ge X)`$ be the probability that strict descent fails. A stationary process supplies such a pair through consecutive observations. The target is the least mutual information $`I(X;Y)`$ compatible with the prescribed marginal law and failure probability.

The first instrument suggests replacing impossible uninterrupted descent with descent that fails rarely. The second suggests measuring the necessary dependence. Comparing only the descent event with independent observations gives a bound that approaches one bit as $`\varepsilon\to0`$ in the atomless case. That calculation loses the constraints imposed by the full marginal law.

Keeping those constraints leads to uniform ranks $`U,V`$ and the circular difference $`D=(U-V)\bmod1`$. For finite-information couplings, equal marginals give $`\mathbb E D=\varepsilon`$. An exponential density on the circle then solves the atomless problem. The finite-state problem leads instead to explicit row and column scaling of an order kernel, followed by a relative-entropy identity proving optimality.

## Results and evidence

The preprint states and proves the following results; logarithms are natural unless bits are specified.

- **Sharp atomless optimum (Theorem 1).** For any prescribed common atomless real marginal and $`0<\varepsilon<1/2`$, the minimum is

  ```math
  J(\varepsilon)=\log\frac{\lambda}{1-e^{-\lambda}}-\lambda\varepsilon,
  \qquad
  \varepsilon=\frac1\lambda-\frac1{e^\lambda-1},\quad\lambda>0.
  ```

  The paper constructs the unique optimizer. At $`\varepsilon=1/2`$, independence is the unique minimizer and the information is zero.

- **A bound for arbitrary marginals (Corollary 2).** For identically distributed real variables, including laws with atoms, and $`0<\varepsilon<1/2`$,

  ```math
  I(X;Y)\ge J(\varepsilon)\ge\log(1/\varepsilon)-1.
  ```

  Thus a 99% probability of strict descent gives an information lower bound of approximately 5.2012 bits. The divergence as failures become rare is missed by the binary-event comparison.

- **Exact finite-state optimum (Theorem 3 and Appendix A).** For any positive marginal $`p=(p_1,\ldots,p_n)`$ on ordered states, with $`n\ge2`$, feasible failure probabilities are exactly $`[\max_i p_i,1]`$. An explicit scalar parametrization gives the unique interior optimizer and the paper evaluates both endpoints. The optimal value is invariant under rearranging the masses; the optimal matrices generally change. For 100 equally likely states, maximal 99% descent has exact cost $`\log_2 100\approx6.644`$ bits.

Section 5 gives a stationary stochastic phase model that attains the atomless bound, and explains the obstruction imposed by exchange symmetry. The information cost is not asserted to be a thermodynamic heat cost.

Appendix C describes exact rational checks, comparisons with a separate implementation of scaling the same kernel, permutation checks and endpoint calculations. The scaling comparisons check the formula for the whole matrix; the relative-entropy identity supplies the proof of optimality.

## What this use case demonstrates

An extracted instrument can suggest a useful question even when only one step of its original argument transfers. Here, a descent obstruction and an information comparison lead to a common optimization problem, whose solution connects circular distributions, copulas, entropy projection and matrix scaling.

Section 6 discusses those established connections and the limits of the novelty search. The exact finite formula and invariance of its value are presented as candidates for a specialized contribution, with historical priority unresolved. Section 7 describes how other researchers can follow the same process. The paper also reports two exploratory leads that did not yield new purity or pseudorandomness results.

## Publication and references

- [Application paper and publication metadata on Zenodo](https://zenodo.org/records/23408425).
- [Download the application PDF](https://zenodo.org/api/records/23408425/files/stationary_descent_case_study.pdf/content).
- [Direction paper: What the Machine Invented](https://zenodo.org/records/23319145).
- [Catalogue assessment and evidence policy](../../methodology/assessment.md).

The Zenodo paper is authored by Ying Xie and released under CC BY 4.0. Its acknowledgment records the author's guidance and responsibility and GPT-6 assistance with exploration, proof development, code checks and drafting.
