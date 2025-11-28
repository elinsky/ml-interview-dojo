# Question

Explain mean reversion and the Ornstein-Uhlenbeck process.

# Answer

**Mean reversion:** Tendency to return to a long-run average.

**Ornstein-Uhlenbeck (OU) process:**

$dX_t = \theta(\mu - X_t) \, dt + \sigma \, dW_t$

**Parameters:**
- $\mu$: Long-run mean
- $\theta$: Speed of mean reversion (larger = faster)
- $\sigma$: Volatility

**Solution:**

$X_t = \mu + (X_0 - \mu)e^{-\theta t} + \sigma \int_0^t e^{-\theta(t-s)} dW_s$

**Properties:**
- $E[X_t] = \mu + (X_0 - \mu)e^{-\theta t} \to \mu$ as $t \to \infty$
- $\text{Var}(X_t) = \frac{\sigma^2}{2\theta}(1 - e^{-2\theta t}) \to \frac{\sigma^2}{2\theta}$
- Stationary distribution: $N(\mu, \frac{\sigma^2}{2\theta})$

**Half-life:** Time for expected deviation to halve: $t_{1/2} = \frac{\ln 2}{\theta}$

**Finance applications:**

1. **Interest rates:** Vasicek model (OU for short rate)
2. **Pairs trading:** Spread between cointegrated assets
3. **Volatility:** Vol tends to mean-revert
4. **Commodities:** Convenience yield models

**Estimation:**
Discrete approximation: $X_{t+\Delta t} - X_t = \theta(\mu - X_t)\Delta t + \sigma\sqrt{\Delta t} \, Z$

Regress $\Delta X$ on $X$ to estimate $\theta$ and $\mu$.

**Trading signal:** When $X_t$ deviates from $\mu$, bet on reversion.
