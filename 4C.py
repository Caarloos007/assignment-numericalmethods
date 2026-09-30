# Exercise 4C - Graphical representation
# Trapezoidal Rule and Simpson's 1/3 Rule

import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-x**2)


# Integration limits and number of subintervals
a = 0
b = 2
n = 4

# Integration nodes
x_nodes = np.linspace(a, b, n + 1)
y_nodes = f(x_nodes)

# 1. Composite Trapezoidal Rule

# Fine points for plotting the function
x = np.linspace(a, b, 500)
y = f(x)

plt.figure(figsize=(10, 6))

# Plot the original function
plt.plot(x, y, label=r"$f(x)=e^{-x^2}$", linewidth=2)

# Plot and shade each trapezoid
for i in range(n):
    x_trap = np.linspace(x_nodes[i], x_nodes[i + 1], 100)

    # Linear approximation between two consecutive nodes
    y_trap = (
        y_nodes[i]
        + (y_nodes[i + 1] - y_nodes[i])
        * (x_trap - x_nodes[i])
        / (x_nodes[i + 1] - x_nodes[i])
    )

    # Plot the straight-line approximation
    plt.plot(
        x_trap,
        y_trap,
        linestyle="--",
        linewidth=1.5
    )

    # Shade the trapezoidal region
    plt.fill_between(
        x_trap,
        0,
        y_trap,
        alpha=0.25
    )

# Mark the integration nodes
plt.scatter(
    x_nodes,
    y_nodes,
    s=50,
    zorder=5,
    label="Integration nodes"
)

plt.title("Composite Trapezoidal Rule")
plt.xlabel("x")
plt.ylabel(r"$f(x)$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(a, b)
plt.ylim(0, 1.1)

plt.tight_layout()
plt.show()


# 2. Simpson's 1/3 Rule

plt.figure(figsize=(10, 6))

# Plot the original function
plt.plot(x, y, label=r"$f(x)=e^{-x^2}$", linewidth=2)

# Simpson uses a quadratic polynomial for every pair
# of consecutive subintervals.
for i in range(0, n, 2):

    # Three Simpson nodes
    x0 = x_nodes[i]
    x1 = x_nodes[i + 1]
    x2 = x_nodes[i + 2]

    y0 = y_nodes[i]
    y1 = y_nodes[i + 1]
    y2 = y_nodes[i + 2]

    # Fine points for the parabola
    x_simpson = np.linspace(x0, x2, 200)

    # Quadratic Lagrange interpolation
    y_simpson = (
        y0 * (x_simpson - x1) * (x_simpson - x2)
        / ((x0 - x1) * (x0 - x2))
        +
        y1 * (x_simpson - x0) * (x_simpson - x2)
        / ((x1 - x0) * (x1 - x2))
        +
        y2 * (x_simpson - x0) * (x_simpson - x1)
        / ((x2 - x0) * (x2 - x1))
    )

    # Plot the parabolic approximation
    plt.plot(
        x_simpson,
        y_simpson,
        linestyle="--",
        linewidth=1.5
    )

    # Shade the Simpson region
    plt.fill_between(
        x_simpson,
        0,
        y_simpson,
        alpha=0.25
    )

# Mark the integration nodes
plt.scatter(
    x_nodes,
    y_nodes,
    s=50,
    zorder=5,
    label="Integration nodes"
)

plt.title("Simpson's 1/3 Rule")
plt.xlabel("x")
plt.ylabel(r"$f(x)$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(a, b)
plt.ylim(0, 1.1)

plt.tight_layout()
plt.show()



# Brief explanation

print("\nExercise 4C - Explanation")
print(
    "The first graph shows the Composite Trapezoidal Rule. "
    "The function is approximated by straight lines between "
    "consecutive integration nodes, creating trapezoidal regions."
)

print(
    "The second graph shows Simpson's 1/3 Rule. "
    "The function is approximated by quadratic parabolas over "
    "each pair of subintervals."
)

print(
    "The integration nodes are marked on both graphs, and the "
    "shaded regions represent the areas used in each numerical approximation."
)