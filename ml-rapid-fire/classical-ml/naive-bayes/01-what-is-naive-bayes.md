# What is Naive Bayes?

**Q:** What is Naive Bayes?

**A:**

- **Probabilistic classifier** based on Bayes' theorem
- Also called: **idiot Bayes** (due to naive assumption)
- **"Naive"** = assumes features are conditionally independent given the class
- Predicts class with highest posterior: **MAP** (Maximum A Posteriori) hypothesis
- Despite naive assumption, works surprisingly well in practice
- Very fast training — no optimization, just counting frequencies
- Popular for text classification (spam filtering, sentiment analysis)
- Approximates **Bayes Optimal Classifier** (theoretical minimum error)

---
