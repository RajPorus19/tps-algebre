#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as pyplot

# Entrée

a = 0
b = 2 * numpy.pi
n = 5
N = 500
# def f(x): return numpy.sin(x)
def f(x): return [1/(1 + 10 * i ** 2) for i in x] if type(x) == list else 1/(1 + 10 * x ** 2)


# Subdivision de [a,b] en n+1 points équidistants
X = numpy.linspace(a, b, n)
Xaff = numpy.linspace(a, b, N)

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

def error():
    tab = []
    for i in range(N):
        tab.append(numpy.abs(P(Xaff[i]) - f(Xaff[i])))
    return numpy.max(tab)

# Affichage
print(error())

pyplot.plot(Xaff, f(Xaff), label="f")
pyplot.plot(Xaff, [P(x) for x in Xaff], label="P")

pyplot.show()

