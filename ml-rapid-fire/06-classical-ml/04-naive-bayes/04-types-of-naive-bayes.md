# Types of Naive Bayes

**Q:** What are the different types of Naive Bayes classifiers?

**A:**

- **Gaussian NB**: continuous features, assumes normal distribution per class
- **Multinomial NB**: discrete counts (e.g., word frequencies in text)
- **Bernoulli NB**: binary features (e.g., word present/absent)
- **Complement NB**: variant of Multinomial, better for imbalanced data
- Choice depends on feature type:
  - Continuous data → Gaussian (or exponential, kernel if better fit)
  - Word counts/TF-IDF → Multinomial
  - Binary features → Bernoulli
- **Don't constrain** to standard distributions — use what fits your data

---
