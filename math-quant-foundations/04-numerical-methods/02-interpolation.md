# Question

Compare linear, polynomial, and spline interpolation. When would you use each?

# Answer

**Linear interpolation:**

$f(x) = y_i + \frac{y_{i+1} - y_i}{x_{i+1} - x_i}(x - x_i)$

- Simple, fast, stable
- Not smooth (corners at data points)
- Use for: Quick estimates, when smoothness doesn't matter

**Polynomial interpolation (Lagrange):**

Unique polynomial of degree $n-1$ through $n$ points

$P(x) = \sum_{i=1}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}$

- Smooth everywhere
- **Runge's phenomenon:** Wild oscillations with many points
- Use for: Few points, or with Chebyshev nodes

**Cubic spline interpolation:**

Piecewise cubics, matching at knots with continuity of $f$, $f'$, $f''$

- Smooth (continuous second derivative)
- Local: changing one point affects neighbors only
- No oscillation problems
- Use for: Yield curves, volatility surfaces

**Finance applications:**

1. **Yield curve:** Bootstrap + cubic spline for smooth forward rates
2. **Vol surface:** Interpolate between strikes and maturities
3. **Greeks by finite difference:** Need smooth interpolation first

**Boundary conditions for splines:**
- Natural: $f''= 0$ at endpoints
- Clamped: Specify $f'$ at endpoints
- Not-a-knot: Third derivative continuous at 2nd and (n-1)th points
