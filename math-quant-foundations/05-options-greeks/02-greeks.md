# Question

Define the main Greeks and explain their practical significance for trading.

# Answer

**The Greeks measure option price sensitivity:**

| Greek | Definition | Interpretation |
|-------|------------|----------------|
| **Delta** $\Delta$ | $\frac{\partial V}{\partial S}$ | Shares to hedge; probability proxy |
| **Gamma** $\Gamma$ | $\frac{\partial^2 V}{\partial S^2}$ | Delta sensitivity; convexity |
| **Theta** $\Theta$ | $\frac{\partial V}{\partial t}$ | Time decay (usually negative) |
| **Vega** $\nu$ | $\frac{\partial V}{\partial \sigma}$ | Volatility sensitivity |
| **Rho** $\rho$ | $\frac{\partial V}{\partial r}$ | Interest rate sensitivity |

**For a call under Black-Scholes:**
- $\Delta_C = N(d_1)$ (between 0 and 1)
- $\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{T}}$ (always positive)
- $\Theta_C = -\frac{S N'(d_1) \sigma}{2\sqrt{T}} - rKe^{-rT}N(d_2)$
- Vega $= S\sqrt{T} N'(d_1)$ (always positive)

**Key relationships:**

**Black-Scholes PDE in Greek form:**
$\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$

**Trading implications:**

1. **Delta-neutral:** Hedge directional risk, keep gamma/vega exposure
2. **Gamma scalping:** Long gamma profits from realized vol > implied vol
3. **Theta decay:** Short options collect premium but face tail risk
4. **Vega trading:** Express view on future volatility

**Gamma-Theta tradeoff:** Long gamma = long convexity = pay theta. You're paying for optionality.
