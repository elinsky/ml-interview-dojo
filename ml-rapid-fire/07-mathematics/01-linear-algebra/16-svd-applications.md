# SVD Applications

**Q:** What are the key applications of SVD?
- Low-rank approximation
- Pseudoinverse
- Other applications

**A:**

- **Low-rank approximation**: keep top k singular values → best rank-k approximation (Eckart-Young theorem)
  - Image compression
  - Noise reduction
  - Latent factor models (recommender systems)
- **Pseudoinverse**: A⁺ = VΣ⁺Uᵀ (for least squares when A not invertible)
- **Other applications**:
  - PCA (via SVD of centered data matrix)
  - Matrix completion
  - Condition number = σ_max / σ_min (numerical stability)
  - Latent Semantic Analysis (NLP)

---
