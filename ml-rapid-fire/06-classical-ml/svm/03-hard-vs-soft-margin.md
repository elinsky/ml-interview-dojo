# Hard Margin vs Soft Margin

**Q:** What is the difference between hard margin and soft margin SVM?

**A:**

- **Hard margin**: No points allowed inside margin; requires linearly separable data
- **Soft margin**: Allows some misclassifications via **slack variables** (ξ)
- Objective: minimize **½||w||² + C·Σξᵢ** (margin + penalty for violations)
- Soft margin is more practical — real data rarely perfectly separable
- **C parameter** controls tradeoff: high C = less tolerance for errors
- Most SVM implementations use soft margin by default

---
