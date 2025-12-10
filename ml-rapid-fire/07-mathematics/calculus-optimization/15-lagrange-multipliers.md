# Lagrange Multipliers

**Q:** What are Lagrange multipliers and when do you use them?
- Problem setup
- Method
- Intuition

**A:**

- **Problem**: minimize f(x) subject to g(x) = 0
- **Method**: solve ∇f = λ∇g and g(x) = 0
  - Form Lagrangian: L(x, λ) = f(x) - λg(x)
  - Find stationary points: ∇ₓL = 0, ∇λL = 0
- **Intuition**: at optimum, gradient of objective is parallel to gradient of constraint (can't improve without violating constraint)
- **λ interpretation**: sensitivity of optimal value to constraint relaxation
- **ML applications**: SVM (maximize margin subject to constraints), constrained optimization

---
