# MCVRP - Calculate the Approximation Ratio

We use $\epsilon$ to denote a small positive constant.

Given $\epsilon$, the function `f(epsilon)` in the `1 Calculating the previous approximation ratios.py` file refers to the function $f$ in [9]. Specifically, we have

$$
f(\epsilon)=\min_{\substack{0<\theta\leq1-\tau, \\ 0<\tau,\rho\leq 1/6}} \\{\frac{1+\zeta}{\theta}+\frac{1-\tau-\theta}{\theta\cdot(1-\tau)}+\frac{3\epsilon}{1-\theta}+\frac{3\rho}{(1-\rho)\cdot(1-\tau)}\\}-1,
$$

where $\theta$ was let to $1-\tau$ in [1] but it is slightly better to set it as
\[
\theta=\min\lrC{\frac{1}{\sqrt{\frac{3\varepsilon}{2+\zeta}}+1}, 1-\tau}.
\] 

and

$$
\zeta=\frac{3\rho+\tau-4\tau\cdot\rho}{1-\rho}+\frac{\epsilon}{\tau\cdot\rho}\cdot(1-\tau\cdot\rho-\frac{3\rho+\tau-4\tau\cdot\rho}{1-\rho}).
$$

Since $f$ is an optimization function, we compute the optimal value using a grid-based brute-force search, which may introduce a small error.

The `1 Calculating the previous approximation ratios.py` file consists of two cases: `splittable` and `unsplittable`.

In the first case, we need to find the proper value of $\epsilon^*$ such that

$$
\epsilon^* = \arg\min_{\epsilon > 0} \max\\{ \alpha+1 - 2\epsilon, 2 + f(\epsilon) \\}.
$$

The `1 Calculating the previous approximation ratios.py` file defaults to setting $\epsilon = 1.005/3000-0.000000005$, and the output is `epsilon should be smaller`, meaning that $\epsilon^* < 1.005/3000-0.000000005$.

However, we note that $\epsilon^\*$ is very close to $1.005/3000$, as even setting $\epsilon = 1.005/3000-0.000000006$ causes the output to be `epsilon can be bigger`, meaning that $\epsilon^\* > 1.005/3000-0.000000006$.

The other case follow a similar pattern.



[1] J. Blauth, V. Traub, J. Vygen, "Improving the approximation ratio for capacitated vehicle routing," *Mathematical Programming*, 197(2) (2023) 451–497.
