#!/usr/bin/env python3

import numpy

# inputs
a = 0
b = 2 * numpy.pi
n = 5
def f(x): return numpy.sin(x)


# interval
X = numpy.linspace(a, b, n)

# V.A = Y
V = numpy.vander(X, increasing=True)
Y = f(X)
A = numpy.linalg.solve(V, Y)


def pol(x):
    s = 0
    for k in range(n):
        s += A[k] * x**k
    return s


print(pol(6))
