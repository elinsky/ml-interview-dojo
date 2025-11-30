# Convex Functions

**Q:** What is a convex function and why does convexity matter?
- Definition
- Geometric interpretation
- Why it matters for optimization

**A:**

- **Definition**: f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y) for all x, y and λ ∈ [0,1]
- **Geometric**: line segment between any two points lies above the curve ("bowl shape")
- **Second-order test**: f is convex iff Hessian is positive semi-definite everywhere
- **Why it matters**:
  - Any local minimum is a global minimum
  - Gradient descent guaranteed to find optimum
  - No saddle points or local minima to get stuck in
- **Examples**: MSE, cross-entropy (in predictions), L2 norm, linear functions

---
