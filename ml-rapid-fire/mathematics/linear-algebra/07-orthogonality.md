# Orthogonality

**Q:** What does orthogonality mean and why is it useful?
- Orthogonal vectors
- Orthonormal vectors
- Orthogonal matrix
- Why it matters in ML

**A:**

- **Orthogonal vectors**: a · b = 0 (perpendicular, uncorrelated)
- **Orthonormal**: orthogonal AND unit length (‖v‖ = 1)
- **Orthogonal matrix Q**: QᵀQ = QQᵀ = I; columns are orthonormal
  - Preserves lengths: ‖Qx‖ = ‖x‖
  - Preserves angles (rotation/reflection)
  - Q⁻¹ = Qᵀ (inverse is just transpose — cheap!)
- **ML relevance**: PCA produces orthogonal components; orthogonal weight initialization; stable numerical computations

---
