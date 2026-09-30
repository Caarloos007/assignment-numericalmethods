# Exercise 2C - Newton-Raphson Method
# Compare the number of iterations for different initial approximations

import matplotlib.pyplot as plt


def f(x):
    return x**3 - 2*x - 2


def df(x):
    return 3*x**2 - 2


def newton_raphson(p0, tolerance):
    p = p0
    iterations = 0

    while True:
        # Apply the Newton-Raphson formula
        p_new = p - f(p) / df(p)
        iterations += 1

        # Check the stopping condition
        if abs(p_new - p) < tolerance:
            return p_new, iterations

        p = p_new


# Initial approximations and tolerances
initial_values = [1.5, 2.5]
tolerances = [10**-3, 10**-5]

# Store the iteration counts
results = {}

for p0 in initial_values:
    print("\nInitial approximation:", p0)

    results[p0] = []

    for tolerance in tolerances:
        root, iterations = newton_raphson(p0, tolerance)
        results[p0].append(iterations)

        print("Tolerance:", tolerance)
        print("Root approximation:", root)
        print("Number of iterations:", iterations)


# Create the comparison chart
x = range(len(tolerances))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    results[1.5],
    width,
    label="Initial approximation = 1.5"
)

plt.bar(
    [i + width / 2 for i in x],
    results[2.5],
    width,
    label="Initial approximation = 2.5"
)

plt.xticks(x, ["Tolerance = 10^-3", "Tolerance = 10^-5"])
plt.xlabel("Tolerance")
plt.ylabel("Number of iterations")
plt.title("Newton-Raphson: Iteration Comparison")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()


# Discuss the influence of the initial approximation
print("\nDiscussion:")
print(
    f"For tolerance 10^-3, the initial approximation 1.5 "
    f"requires {results[1.5][0]} iterations, while 2.5 "
    f"requires {results[2.5][0]} iterations."
)

print(
    f"For tolerance 10^-5, the initial approximation 1.5 "
    f"requires {results[1.5][1]} iterations, while 2.5 "
    f"requires {results[2.5][1]} iterations."
)

print(
    "Both initial approximations converge to the same root. "
    "The initial approximation can affect the number of iterations "
    "required. A closer initial guess to the root may lead to faster "
    "convergence, although this is not guaranteed in every case."
)