# Question

Define Brownian motion (Wiener process) and its key properties.

# Answer

**Brownian motion** $W_t$ is a continuous-time stochastic process with:

1. $W_0 = 0$
2. **Independent increments:** $W_t - W_s$ independent of $\{W_u : u \leq s\}$
3. **Stationary increments:** $W_t - W_s \sim N(0, t-s)$
4. **Continuous paths:** $t \mapsto W_t$ is continuous (a.s.)

**Key properties:**

- $E[W_t] = 0$
- $\text{Var}(W_t) = t$
- $\text{Cov}(W_s, W_t) = \min(s, t)$
- **Not differentiable:** Paths are continuous but nowhere differentiable
- **Quadratic variation:** $[W, W]_t = t$ (crucial for Ito calculus)
- **Martingale:** $E[W_t | \mathcal{F}_s] = W_s$ for $s < t$

**Scaling property:** $\frac{1}{\sqrt{c}} W_{ct} \stackrel{d}{=} W_t$

**Reflection principle:** Used for barrier option pricing

**Why it matters in finance:**

- Foundation of continuous-time finance
- Drives randomness in asset price models
- Black-Scholes assumes stock prices driven by BM
- $dS_t = \mu S_t dt + \sigma S_t dW_t$ (GBM)

**Simulation:** $W_{t+\Delta t} = W_t + \sqrt{\Delta t} \cdot Z$ where $Z \sim N(0,1)$
