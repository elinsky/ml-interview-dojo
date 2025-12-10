# Common Kernel Functions

**Q:** What are the common kernel functions for SVM?

**A:**

- **Linear**: K(x, x') = ⟨x, x'⟩ — no transformation, fast, use LinearSVC for scale
- **Polynomial**: K(x, x') = (γ⟨x, x'⟩ + r)^d — degree d, coef0 r control complexity
- **RBF (Gaussian)**: K(x, x') = exp(-γ||x - x'||²) — most popular, infinite dimensions
- **Sigmoid**: K(x, x') = tanh(γ⟨x, x'⟩ + r) — similar to neural network
- Start with RBF; try linear if dataset is large or n_features >> n_samples
- Custom kernels supported via precomputed Gram matrix

---
