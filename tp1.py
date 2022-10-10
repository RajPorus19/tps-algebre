#!/usr/bin/env python3

import numpy

a = 0
b = 2 * numpy.pi
n = 5
X = numpy.linspace(a, b, n)
Y= numpy.sin(X)
V=numpy.vander(X,increasing=True)

A=numpy.linalg.solve(V, Y)

def pol(x):
    s = 0
    for k in range(n):
        s += A[k] * x**k
    return s

print(pol(6))