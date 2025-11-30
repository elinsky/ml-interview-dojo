# Poisson Distribution

**Q:** What is the Poisson distribution and when do you use it?
- What it models
- Parameter and notation
- Mean and variance
- Relationship to binomial
- Example use case

**A:**

- **Models**: count of events in fixed interval (time/space) when events occur independently at constant rate
- **Parameter**: Poisson(λ) — λ = average rate (events per interval)
- **Mean = Variance**: E[X] = Var(X) = λ
- **Binomial limit**: Binomial(n,p) → Poisson(np) as n→∞, p→0, np=λ constant
- **Example**: number of trades arriving per minute, number of defaults in a portfolio

---
