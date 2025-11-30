# Exponential Distribution

**Q:** What is the exponential distribution and what makes it special?
- What it models
- Parameter
- Memoryless property (what it means)
- Relationship to Poisson

**A:**

- **Models**: time between events in a Poisson process (waiting time)
- **Parameter**: Exp(λ) — λ = rate; Mean = 1/λ
- **Memoryless**: P(X > s+t | X > s) = P(X > t) — "past doesn't matter"; only continuous distribution with this property
- **Poisson connection**: if events arrive as Poisson(λ), inter-arrival times are Exp(λ)
- **Example**: time until next trade, time until component failure

---
