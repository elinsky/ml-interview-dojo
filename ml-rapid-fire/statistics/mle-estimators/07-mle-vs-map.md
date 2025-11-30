# MLE vs MAP

**Q:** What's the difference between MLE and MAP estimation?
- MLE formula
- MAP formula
- When they differ
- Connection to regularization

**A:**

- **MLE**: θ̂ = argmax P(data | θ) — maximize likelihood only
- **MAP**: θ̂ = argmax P(θ | data) = argmax P(data | θ) · P(θ) — includes prior
- **When they differ**: when prior P(θ) is informative (not uniform)
- **MAP = MLE when**: prior is uniform (flat)
- **Regularization connection**:
  - Gaussian prior → L2 regularization (ridge)
  - Laplace prior → L1 regularization (lasso)
- **Bayesian view**: MAP is point estimate; full Bayesian computes entire posterior

---
