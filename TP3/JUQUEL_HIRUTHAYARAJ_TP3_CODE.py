#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as pyplot


# Entrée

a = -1000
b = 1000
n = 500
N = 5000
# def f(x): return numpy.sin(x)
def f(x): return [1/(1 + 10 * i ** 2) for i in x] if type(x) == list else 1/(1 + 10 * x ** 2)


X = numpy.linspace(a, b, n)
Y = f(X)
x = numpy.linspace(a, b, N)

# Interpolation polynomiale : Base de Newton

def Newton(X, Y, x):
    n = len(X)
    P = numpy.zeros((n, n))
    P[:, 0] = Y
    for j in range(1, n):
        for i in range(n - j):
            P[i, j] = (P[i + 1, j - 1] - P[i, j - 1]) / (X[i + j] - X[i])
    y = numpy.zeros(N)
    for k in range(n):
        temp = P[0, k]
        for j in range(k):
            temp = temp * (x - X[j])
        y = y + temp
    return y

# Affichage

pyplot.plot(x, f(x), label='f(x)')
pyplot.plot(x, Newton(X, Y, x), label='Newton')
pyplot.plot(X, Y, 'o', label='Points d\'interpolation')
# pyplot.ylim(-3, 3)
# pyplot.legend()
# pyplot.show()