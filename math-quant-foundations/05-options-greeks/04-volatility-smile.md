# Question

What is the volatility smile/skew? What causes it?

# Answer

**Volatility smile:** Implied volatility varies with strike price.

- **Smile:** IV higher for OTM puts AND calls (U-shaped)
- **Skew:** IV higher for OTM puts than calls (monotonic)

**Equity markets typically show skew:**
- OTM puts: Higher IV (crash protection premium)
- ATM: Lower IV
- OTM calls: Slightly lower or flat

**FX markets often show smile:** Symmetric around ATM

**Why Black-Scholes predicts flat IV:**
BS assumes constant vol → all strikes should give same IV
Reality: Different strikes have different IVs

**Causes of the smile:**

1. **Fat tails:** Real returns have more extreme moves than lognormal
2. **Jumps:** Discontinuous price moves (crashes)
3. **Stochastic volatility:** Vol itself is random
4. **Leverage effect:** Vol increases when prices fall
5. **Supply/demand:** Hedging demand for OTM puts

**Models that generate smiles:**

| Model | Mechanism |
|-------|-----------|
| Local volatility | $\sigma(S,t)$ deterministic function |
| Stochastic vol (Heston) | Vol follows mean-reverting process |
| Jump-diffusion (Merton) | Poisson jumps added to GBM |
| SABR | Stochastic vol with correlation |

**Trading the smile:**
- Risk reversals: Long OTM call, short OTM put
- Butterflies: Bet on smile shape
- Variance swaps: Trade realized vs implied variance
