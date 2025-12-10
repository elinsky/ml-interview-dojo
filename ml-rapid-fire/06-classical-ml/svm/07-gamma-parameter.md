# The Gamma Parameter

**Q:** What does gamma (γ) control in the RBF kernel?

**A:**

- Controls **influence radius** of each training example
- **High γ**: small radius, each point only affects nearby points → complex boundary, overfitting (high variance)
- **Low γ**: large radius, points influence farther → smoother boundary, underfitting (high bias)
- γ = 1/(2σ²) where σ is Gaussian width
- Typical range: 0 < γ < 1 (start with 0.1)
- Must tune together with C for best results (grid search)

---
