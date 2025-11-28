# Question

What is a martingale and why is it central to derivative pricing?

# Answer

**Martingale definition:** A stochastic process $M_t$ is a martingale if:

$E[M_T | \mathcal{F}_t] = M_t$ for all $T > t$

**Intuition:** The best forecast of future value is the current value. No predictable drift.

**Examples:**
- Brownian motion $W_t$
- $W_t^2 - t$ (compensated squared BM)
- Fair game cumulative winnings

**Key properties:**
- $E[M_T] = E[M_0]$ (constant expectation)
- Submartingale: $E[M_T | \mathcal{F}_t] \geq M_t$ (upward drift)
- Supermartingale: $E[M_T | \mathcal{F}_t] \leq M_t$ (downward drift)

**Why martingales matter in finance:**

1. **Risk-neutral pricing:** Under $\mathbb{Q}$, discounted asset prices are martingales:
   $E^{\mathbb{Q}}[e^{-r(T-t)} S_T | \mathcal{F}_t] = S_t$

2. **No-arbitrage:** Equivalent to existence of martingale measure

3. **Option pricing formula:**
   $V_t = e^{-r(T-t)} E^{\mathbb{Q}}[\text{payoff}_T | \mathcal{F}_t]$

4. **Replication:** Self-financing portfolio value is a martingale

**Girsanov theorem:** Changing probability measure can turn a process with drift into a martingale. This is how we switch from physical measure $\mathbb{P}$ to risk-neutral measure $\mathbb{Q}$.
