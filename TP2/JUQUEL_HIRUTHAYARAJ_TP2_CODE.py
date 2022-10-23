#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as pyplot


# Entrée

a = -5
b = 5
n = 20
N = 500
# def f(x): return numpy.sin(x)
def f(x): return [1/(1 + 10 * i ** 2) for i in x] if type(x) == list else 1/(1 + 10 * x ** 2)


X = numpy.linspace(a, b, n)
Y = f(X)
x = numpy.linspace(a, b, N)

# Interpolation polynomiale et base de Lagrange

def L(i, x, X):
    l = 1
    for j in range(n):
        if i != j:
            l *= (x - X[j]) / (X[i] - X[j])
    return l

def P(x, X, Y):
    p = 0
    for i in range(n):
        p += Y[i] * L(i, x, X)
    return p

y = P(x, X, Y)

# Affichage

pyplot.plot(x, y, label='Interpolation')
pyplot.plot(x, f(x), label='f')
pyplot.plot(X, Y, 'o', label='Points d\'interpolation')
pyplot.ylim(-3, 3)
pyplot.legend()
pyplot.show()