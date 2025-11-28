# Question

Explain cubic splines in detail. Why are they preferred for yield curve construction?

# Answer

**Cubic spline:** Piecewise cubic polynomials $S_i(x)$ on $[x_i, x_{i+1}]$ satisfying:

1. **Interpolation:** $S_i(x_i) = y_i$, $S_i(x_{i+1}) = y_{i+1}$
2. **C¹ continuity:** $S_i'(x_{i+1}) = S_{i+1}'(x_{i+1})$
3. **C² continuity:** $S_i''(x_{i+1}) = S_{i+1}''(x_{i+1})$

Each cubic: $S_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3$

**Construction:** Solve tridiagonal system for second derivatives $M_i = S''(x_i)$, then recover coefficients.

**Why yield curves use splines:**

1. **Smooth forward rates:** $f(t) = -\frac{d}{dt}\log P(t)$
   Forward rates involve derivative of discount curve. Splines are smooth enough.

2. **Local control:** Changing one rate doesn't distort distant maturities

3. **No arbitrage:** Smooth curves prevent spurious arbitrage opportunities

4. **Hedging:** Greeks require differentiable curves

**Tension splines:** Add parameter to control "tightness" - useful when data is noisy

**Monotone splines:** Preserve monotonicity (important for discount factors, which must decrease)

**Common issues:**
- Negative forwards at short end
- Oscillation if data is inconsistent
- Endpoint behavior (natural vs clamped)

**Alternative:** Nelson-Siegel parametric model - fewer degrees of freedom, more stable
