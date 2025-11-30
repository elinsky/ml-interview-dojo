# Vector Norms

**Q:** What are the common vector norms and when do you use each?
- L1, L2, L∞ formulas
- Geometric interpretation
- ML applications

**A:**

- **L1 norm**: ‖x‖₁ = Σᵢ|xᵢ| — sum of absolute values (Manhattan distance)
- **L2 norm**: ‖x‖₂ = √(Σᵢxᵢ²) — Euclidean distance (most common)
- **L∞ norm**: ‖x‖∞ = maxᵢ|xᵢ| — maximum absolute value
- **ML applications**:
  - L1: sparse solutions, Lasso regularization, robust to outliers
  - L2: smooth solutions, Ridge regularization, gradient-friendly
  - L∞: worst-case bounds, adversarial robustness

---
