# Small counterexamples that protect a transfer

The following calculations explain why some hypotheses in the extracted instruments are essential. They are exact counterexamples to specific shortcuts, not counterexamples to the source theorems. The linked cards contain the complete positive statements and their source locations.

## Ordinary order does not compare all powers

For [MI-000451](../catalog/instruments/MI-000451.md), take

$$A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
B=\begin{pmatrix}2&1\\1&1\end{pmatrix}.$$

Both are positive and $B-A$ is positive. But

$$B^2-A^2=\begin{pmatrix}4&3\\3&2\end{pmatrix}$$

has determinant $-1$, hence a negative eigenvalue. Ordinary $A\le B$ cannot replace the card's spectral-tail condition. This matters even in dimension two, before any unbounded-domain issue arises.

## Clipping does not commute with taking a mean

For clipping to $[-1,1]$, the values $(0,3)$ have mean $3/2$, whose clipped value is $1$. Their clipped values $(0,1)$ have mean $1/2$. [MI-000457](../catalog/instruments/MI-000457.md) obtains a residual estimate using nonexpansiveness and an orthogonal projection; it never interchanges these operations.

## A special fiber does not determine an arbitrary deformation

For $S=k[t]$, the surjection $S\to S/(t)$ induces an isomorphism after reduction modulo $t$, but has nonzero kernel. The target is not flat. In [MI-000419](../catalog/instruments/MI-000419.md), flatness is what makes the reduced kernel inject into the reduced source.

The lower grading bound also matters. The nonzero graded module $J=k[t,t^{-1}]$ satisfies $J=tJ$. There is no least nonzero degree, so the minimal-degree argument cannot conclude $J=0$.

## Rational independence does not imply localized saturation

In $K=\mathbb Z_{(2)}$, the single vector $w=2$ is rationally independent, yet

$$\operatorname{span}_{\mathbb Q}(w)\cap K=K
\ne 2K=\operatorname{span}_{\mathbb Z_{(2)}}(w).$$

Its reduction modulo $2$ is zero. [MI-000445](../catalog/instruments/MI-000445.md) assumes independence after reduction, which supplies the missing control of denominators.

## Fixed-order vanishing does not imply completed vanishing

Let $R=\mathbb C[[h]]$ and consider the direct system

$$R\xrightarrow{h}R\xrightarrow{h}R\xrightarrow{h}\cdots.$$

Modulo any fixed $h^n$, every element dies after at most $n$ transitions. But the direct limit of the modules themselves is $\mathbb C((h))$: map stage $i$ into it by $f\mapsto h^{-i}f$. Every transition is injective, and the union contains all Laurent series with finitely many negative powers.

In [MI-000471](../catalog/instruments/MI-000471.md), a common upper weight bound and strictness prevent this behavior. If the stage-$i$ generator instead has weight $2i$, with $h$ lowering weight by two, these nonzero transitions preserve weights while the upper bound grows. The failed uniformity is explicit.

## Positivity of a few moments does not give positivity of every mass

The signed atomic measure $2\delta_0-\delta_1$ has positive total mass. It is not positive: testing against the square of $p(t)=t$ gives $-1$. [MI-000449](../catalog/instruments/MI-000449.md) requires positivity for every polynomial square, together with an exponential moment to pass from polynomials to atom indicators in infinite support.

These examples suggest a practical sequence: identify the exact hypothesis used at each step, try a small model after dropping it, and retain the hypothesis if the conclusion fails. A passing finite model still leaves the general proof to be supplied. See the [research guide](research-guide.md) and [assessment policy](assessment.md) for the different kinds of evidence recorded in the catalogue.
