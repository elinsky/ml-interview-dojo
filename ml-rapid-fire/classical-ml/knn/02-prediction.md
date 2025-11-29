# KNN Prediction

**Q:** How does KNN make predictions?

**A:**

- **Classification**: majority vote among K nearest neighbors
- **Regression**: mean (or median) of K nearest neighbors' values
- **Class probabilities**: p(class) = count(class) / K — normalized frequency
- Ties in classification: expand K by 1, use distance-weighted voting, or random
- Must choose distance metric to define "nearest"
- No training phase — all computation at prediction time ("just-in-time")

---
