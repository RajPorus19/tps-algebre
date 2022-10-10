#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as pyplot

# Entrée

a = 0
b = 2 * numpy.pi
n = 250
# def f(x): return numpy.sin(x)
def f(x): return [i**2 for i in x]


# Subdivision de [a,b] en n+1 points équidistants
X = numpy.linspace(a, b, n)

# V.A = Y
V = numpy.vander(X, increasing=True)

# Matrice verticale Yi = f(Xi)
Y = f(X)

# Résolution du système
A = numpy.linalg.solve(V, Y)

# Évaluation de la fonction


def P(x):
    s = 0
    for k in range(n):
        s += A[k] * x**k
    return s


# Affichage
pyplot.plot(X, Y)
pyplot.plot(X, [P(x) for x in X])

pyplot.show()
