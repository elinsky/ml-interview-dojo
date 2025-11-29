# Gaussian Naive Bayes

**Q:** How does Gaussian Naive Bayes work?

**A:**

- Assumes continuous features follow **Gaussian (normal) distribution** per class
- P(xᵢ|class) = (1/√(2πσ²)) · exp(-(xᵢ - μ)² / 2σ²)
- **Training**: estimate mean (μ) and variance (σ²) for each feature per class
- **Prediction**: plug new x into Gaussian PDF for each class
- Works best when features are roughly normally distributed
- **Tip**: remove outliers (>3-4 std from mean) for better Gaussian fit
- Simple, fast, no hyperparameters to tune

---
