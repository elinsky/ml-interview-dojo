# Question

Explain the term structure of volatility and interest rates.

# Answer

**Volatility term structure:** How implied vol varies with time to expiration

**Common patterns:**
- **Contango (upward):** Longer-dated options have higher IV
  Normal state; uncertainty grows with horizon
- **Backwardation (inverted):** Near-term IV higher
  During stress; immediate uncertainty elevated

**Interest rate term structure (yield curve):**

**Key rates:**
- Spot rate $r(t)$: Rate for borrowing from now to $t$
- Forward rate $f(t_1, t_2)$: Rate locked in now for $[t_1, t_2]$
- Instantaneous forward: $f(t) = -\frac{\partial}{\partial t}\log P(0,t)$

**Curve shapes:**
- **Normal (upward):** Long rates > short rates
- **Inverted:** Short rates > long rates (recession signal)
- **Humped:** Peak at intermediate maturities

**Relationship:** 
$P(0,T) = \exp\left(-\int_0^T f(0,t) \, dt\right)$

**Principal components of yield curve moves:**
1. **Level (PC1):** Parallel shift (~85% of variance)
2. **Slope (PC2):** Steepening/flattening (~10%)
3. **Curvature (PC3):** Butterfly (~3%)

**Models:**
- **Short-rate:** Vasicek, CIR, Hull-White
- **Forward-rate:** HJM framework
- **Market models:** LIBOR Market Model (BGM)

**Trading implications:**
- Curve steepeners/flatteners
- Calendar spreads for vol term structure
- Duration and convexity hedging
