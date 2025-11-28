# Question

What is Geometric Brownian Motion and why is it used for stock prices?

# Answer

**Geometric Brownian Motion (GBM):**

$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$

**Solution (using Ito's lemma):**

$S_T = S_0 \exp\left[(\mu - \frac{\sigma^2}{2})T + \sigma W_T\right]$

**Key properties:**

- $S_t > 0$ always (prices can't go negative)
- $\log(S_T/S_0) \sim N\left((\mu - \frac{\sigma^2}{2})T, \sigma^2 T\right)$
- Returns are log-normally distributed
- **Memoryless:** Future depends only on current price, not path

**Parameters:**
- $\mu$: Drift (expected return)
- $\sigma$: Volatility

**Expected value:** $E[S_T] = S_0 e^{\mu T}$

Note: The $-\frac{\sigma^2}{2}$ term is the **Ito correction** - converts from log-return expectation to price expectation.

**Why GBM for stocks:**

1. Prices stay positive
2. Percentage returns more natural than absolute
3. Mathematical tractability (Black-Scholes)
4. Reasonable first approximation

**Limitations:**
- Constant volatility (real vol is stochastic)
- No jumps (real markets have discontinuities)
- Thin tails (real returns are fat-tailed)
- No mean reversion (may matter for some assets)
