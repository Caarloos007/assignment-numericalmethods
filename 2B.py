# Exercise 2B - Newton-Raphson Method

def f(x):
    return x**3 - 2*x - 2


def df(x):
    return 3*x**2 - 2


def newton_raphson(p0, tolerance):
    p = p0
    iterations = 0

    while True:
        # Newton-Raphson formula
        p_new = p - f(p) / df(p)
        iterations += 1

        # Check the stopping condition
        if abs(p_new - p) < tolerance:
            return p_new, iterations

        p = p_new


# Initial approximation
p0 = 1.5

# Tolerance 10^-3
root, iterations = newton_raphson(p0, 10**-3)
print("Tolerance = 10^-3")
print("Root approximation:", root)
print("Number of iterations:", iterations)

# Tolerance 10^-5
root, iterations = newton_raphson(p0, 10**-5)
print("\nTolerance = 10^-5")
print("Root approximation:", root)
print("Number of iterations:", iterations)