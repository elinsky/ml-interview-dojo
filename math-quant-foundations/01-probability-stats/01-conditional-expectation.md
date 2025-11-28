# Question

What is conditional expectation and why is it central to quantitative finance?

# Answer

**Conditional expectation** $E[X|Y]$ is the expected value of $X$ given knowledge of $Y$. It's a random variable (function of $Y$), not a number.

**Key properties:**

1. **Tower property (Law of Iterated Expectations):**
   $E[E[X|Y]] = E[X]$
   
   You can "average out" the conditioning. Critical for pricing derivatives.

2. **Linearity:** $E[aX + bZ | Y] = aE[X|Y] + bE[Z|Y]$

3. **Taking out what's known:** If $g(Y)$ is a function of $Y$:
   $E[g(Y) \cdot X | Y] = g(Y) \cdot E[X|Y]$

**Why it matters in finance:**

- **Derivative pricing:** Price = $E^Q[\text{discounted payoff} | \mathcal{F}_t]$ under risk-neutral measure
- **Filtering:** Estimating hidden state from noisy observations
- **Martingales:** $M_t$ is a martingale iff $E[M_T | \mathcal{F}_t] = M_t$

**Example:** If stock follows GBM, $E[S_T | S_t] = S_t e^{\mu(T-t)}$ (under physical measure)
