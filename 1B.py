# Exercise 1B - Bisection Method

def f(x):
    return x**3 + x - 3


def bisection(a, b, tolerance):
    iterations = 0

    while (b - a) / 2 > tolerance:
        p = (a + b) / 2
        iterations += 1

        # Keep the interval containing the root
        if f(a) * f(p) < 0:
            b = p
        else:
            a = p

    # Final root approximation
    p = (a + b) / 2

    return p, iterations


# Initial interval
a = 1
b = 1.5

# Tolerance 10^-3
root, iterations = bisection(a, b, 10**-3)
print("Tolerance = 10^-3")
print("Root approximation:", root)
print("Number of iterations:", iterations)

# Tolerance 10^-5
root, iterations = bisection(a, b, 10**-5)
print("\nTolerance = 10^-5")
print("Root approximation:", root)
print("Number of iterations:", iterations)