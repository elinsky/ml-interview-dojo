# Chain Rule

**Q:** What is the chain rule and why is it essential for ML?
- Formula
- Intuition
- Role in backpropagation

**A:**

- **Formula**: d/dx[f(g(x))] = f'(g(x)) · g'(x) — "outer derivative × inner derivative"
- **Multivariate**: ∂L/∂x = (∂L/∂y)(∂y/∂x) — derivative flows backwards through composition
- **Intuition**: if y changes by dy and L changes by dL/dy per unit y, then effect of x on L is the product
- **Backpropagation**: chain rule applied repeatedly through network layers
  - Forward: compute activations
  - Backward: multiply local gradients along path from loss to parameter
- **Example**: L(σ(wx)) → ∂L/∂w = (∂L/∂σ)(∂σ/∂z)(∂z/∂w) where z = wx

---
