# Laplace Smoothing

**Q:** What is Laplace smoothing and why is it needed?

**A:**

- **Problem**: if a feature value never appears with a class, P(feature|class) = 0
- Zero probability → entire product becomes zero → wrong predictions
- **Laplace smoothing** (additive smoothing): add α to all counts
- P(xᵢ|class) = (count(xᵢ, class) + α) / (count(class) + α·n)
- **α = 1**: Laplace smoothing; **α < 1**: Lidstone smoothing
- Prevents zero probabilities, acts as mild regularization
- In sklearn: `alpha` parameter (default=1.0)

---
