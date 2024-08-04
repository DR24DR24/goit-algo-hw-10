# goit-algo-hw-10

# Report on Integrating Rapidly Changing Functions

Ordinary integration functions work well for smooth functions. However, if a function changes rapidly, ordinary integration functions yield large errors. In this case, using the Monte Carlo method, it is much easier to achieve the required calculation accuracy.

## Test Function

As a test function for integration, the following function was chosen:

$$
f(x) = \sin\left(\frac{1}{x}\right)
$$

Integration range: from $10^{-5}$ to 2.

## Results of Numerical Experiments

### Standard Integration Function

The standard Python integration function without additional settings gives an error of $10^{-3}$.

### Monte Carlo Method

The Monte Carlo method with $10^7$ points gives an error of $3 \cdot 10^{-4}$. Thus, under these conditions, the Monte Carlo method proved to be more accurate.

Nevertheless, the results of the Monte Carlo method and the standard integration method are consistent with each other, taking into account the error estimates of the integration.
