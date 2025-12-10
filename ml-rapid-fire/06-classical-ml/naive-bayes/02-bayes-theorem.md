# Bayes' Theorem

**Q:** What is Bayes' theorem and how is it used in Naive Bayes?

**A:**

- **Bayes' theorem**: P(h|d) = P(d|h) · P(h) / P(d)
- For classification: P(class|features) = P(features|class) · P(class) / P(features)
- **P(class)** = prior probability (base rate)
- **P(features|class)** = likelihood
- **P(features)** = evidence (constant, can drop for comparison)
- **P(class|features)** = posterior probability
- **MAP**: argmax P(class) · P(features|class) — select highest posterior
- **Base rate fallacy**: ignoring prior when estimating posterior

[[202101072002]] [[202101081940]] [[202012301740]]

---
