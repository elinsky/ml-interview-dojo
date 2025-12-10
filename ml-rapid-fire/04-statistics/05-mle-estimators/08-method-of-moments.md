# Method of Moments

**Q:** What is the Method of Moments and how does it compare to MLE?
- Core idea
- Steps
- Comparison to MLE

**A:**

- **Core idea**: equate sample moments to population moments, solve for parameters
- **Steps**:
  1. Express population moments in terms of parameters: E[X] = f(θ), E[X²] = g(θ), ...
  2. Set sample moments equal: x̄ = f(θ̂), (1/n)Σxᵢ² = g(θ̂), ...
  3. Solve system of equations for θ̂
- **vs MLE**:
  - MoM: simpler, always has closed form, but less efficient
  - MLE: asymptotically optimal (lowest variance), but may require numerical optimization
- **When to use MoM**: quick initial estimate, or when MLE is intractable

---
