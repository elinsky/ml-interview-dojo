# Question

State the Central Limit Theorem and explain why it's fundamental to quantitative finance.

# Answer

**Central Limit Theorem (CLT):**

For i.i.d. random variables $X_1, ..., X_n$ with mean $\mu$ and variance $\sigma^2$:

$\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)$ as $n \to \infty$

Or equivalently: $\bar{X}_n \approx N(\mu, \sigma^2/n)$ for large $n$

**Key implications:**

1. **Averages are approximately normal** regardless of underlying distribution
2. **Standard error scales as $1/\sqrt{n}$** - need 4x data for 2x precision
3. **Confidence intervals:** $\bar{x} \pm z_{\alpha/2} \cdot \sigma/\sqrt{n}$

**Finance applications:**

1. **Portfolio returns:** Sum of many small bets → approximately normal
2. **Monte Carlo:** Average of simulations converges to true expectation
3. **Risk measures:** Justifies normal approximations (with caution)
4. **Statistical arbitrage:** Mean reversion of spreads

**When CLT fails or is slow:**

- **Heavy tails:** Fat-tailed distributions (like asset returns) converge slowly
- **Dependence:** Requires independence or weak dependence
- **Infinite variance:** Distributions without finite variance (e.g., Cauchy) never converge

**Berry-Esseen bound:** Convergence rate is $O(1/\sqrt{n})$ - tells you how good the approximation is.

**Warning for quants:** Don't assume normality blindly. Tails of return distributions are fatter than Gaussian.
