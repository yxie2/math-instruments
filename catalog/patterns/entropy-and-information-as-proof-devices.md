---
id: PAT-003
record_type: pattern
title: Entropy and information as proof devices
batch_id: B001
source_section: '7.3'
updated: '2026-10-12'
---

# Entropy and information as proof devices

[Pattern index](README.md)

Mutual information, relative-entropy projections, and entropy inequalities organize estimates in several proofs. The information quantities measure how much dependence or conditioning is available, and incompatible upper and lower bounds produce a contradiction.

The Kakeya proof uses a mutual-information bound to apply a projection theorem to dependent events. The Hadwiger construction combines Kleitman–Winston recording with a Csiszár I-projection as its progress measure and a Ford–Fulkerson cut as its stopping certificate. The matrix-multiplication argument for $`\omega`$ uses an entropy inequality for a shared tensor leg, while the zero-divisor construction bounds repeated traversals of a random graph by entropy. In the second group, conditioning in the ionization argument costs $`\log^5(e/p)`$ times the inverse squared noise scale in energy. The area-law proof expresses conditional mutual information through a log-norm derivative, and the Haldane-gap proof uses a Rényi-2 purity bootstrap.
