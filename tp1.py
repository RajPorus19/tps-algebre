#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as pyplot

# Entrée

a = 0
b = 5 * numpy.pi
n = 12
N = 500
# def f(x): return numpy.sin(x)


def f(x): return [1/(1 + 10 * i ** 2) for i in x] if type(x) == list else 1/(1 + 10 * x ** 2)


# Subdivision de [a,b] en n+1 points équidistants
X = numpy.linspace(a, b, n)
Xaff = numpy.linspace(a, b, N)

# Matrice de Vandermonde
V = numpy.vander(X, increasing=True)

# Matrice verticale Yi = f(Xi)
Y = f(X)

# Résolution du système V A = Y
A = numpy.linalg.solve(V, Y)

# Évaluation de la fonction


def Polynome(x):
    s = 0
    for k in range(n):
        s += A[k] * x**k
    return s


def Erreur():
    tab = [numpy.abs(Polynome(Xaff[i]) - f(Xaff[i])) for i in range(N)]
    return numpy.max(tab)


# Affichage
print(Erreur())

pyplot.plot(Xaff, f(Xaff), label="f")
pyplot.plot(Xaff, [Polynome(x) for x in Xaff], label="P")

pyplot.show()
