# Hessian

**Q:** What is the Hessian and why does it matter for optimization?
- Definition
- What it tells you
- Role in optimization

**A:**

- **Definition**: matrix of second-order partial derivatives: H[i,j] = ∂²f/∂xᵢ∂xⱼ
- **Properties**: symmetric if f has continuous second derivatives
- **What it tells you**: local curvature of function
  - Positive definite → local minimum
  - Negative definite → local maximum
  - Indefinite (mixed signs) → saddle point
- **Optimization**:
  - Newton's method: θ ← θ - H⁻¹∇f (uses curvature for faster convergence)
  - Eigenvalues of H determine condition number → affects gradient descent speed
  - Large eigenvalue ratio → elongated contours → slow convergence

---
