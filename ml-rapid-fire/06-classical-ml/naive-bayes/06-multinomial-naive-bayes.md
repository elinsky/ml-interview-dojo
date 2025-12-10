# Multinomial Naive Bayes

**Q:** How does Multinomial Naive Bayes work?

**A:**

- For **discrete count** data (e.g., word frequencies)
- P(xᵢ|class) estimated from frequency counts in training data
- **Training**: count feature occurrences per class, normalize to probabilities
- Most popular for **text classification** (spam, sentiment, topic modeling)
- Works with raw counts or TF-IDF features
- Assumes features represent counts from multinomial distribution

---
