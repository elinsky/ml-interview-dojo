# Categorical Cross-Entropy

**Q:** How does categorical cross-entropy differ from binary cross-entropy? Give the formula.

**A:** Used for multi-class (3+ classes) instead of binary. Formula: -Σ y_i·log(p_i) summed over all classes. Only the true class contributes (others have y_i=0). Paired with softmax (not sigmoid) [@chollet2018deep, p. 114]. — 202101120811 Activation Functions

"It's useful to think of a softmax output layer with log-likelihood cost as being quite similar to a sigmoid output layer with cross-entropy cost" [@nielsen2015neural, p. 73]. — 202101171406 Log-Likelihood Cost

---
