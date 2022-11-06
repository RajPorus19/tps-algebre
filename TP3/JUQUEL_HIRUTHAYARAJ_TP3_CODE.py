#!/usr/bin/env python3
import numpy
import matplotlib.pyplot as pyplot
from copy import deepcopy


# Entrée

a = 0
b = 2 * numpy.pi
n = 4
def f(x): return numpy.sin(x)
# def f(x): return [1/(1 + 10 * i ** 2) for i in x] if type(x) == list else 1/(1 + 10 * x ** 2)

X = numpy.linspace(a, b, n)
Y = f(X)

# Interpolation polynomiale : Base de Newton

def divis():
    coeff = deepcopy(Y)
    for j in range(len(X)):
        for i in range(len(X) - 1, j, -1):
            coeff[i] = (coeff[i] - coeff[i - 1]) / (X[i] - X[i - j - 1])
    return coeff

def Newton(coeff, x):
    N = 1
    s = coeff[0]
    for i in range(1, len(X)):
        N *= x - X[i - 1]
        s += coeff[i] * N
    return s

def Ajout_un_point(xaj,yaj):
    global X , Y
    X = numpy.append(X, xaj)
    Y = numpy.append(Y,yaj)
    coeff = divis()
    return coeff


# Affichage
Xaff = numpy.linspace(a, b, 1000)

Yexact = f(Xaff)
pyplot.plot(Xaff, Yexact, label='f(x)', color='red')

Yestime = Newton(divis(), Xaff)
pyplot.plot(Xaff, Yestime, label='Interpolation polynomiale', color='blue')

Ynew = Newton(Ajout_un_point(1, f(1)), Xaff)
pyplot.plot(Xaff, Ynew, label='Interpolation polynomiale avec un point ajouté', color='green')

pyplot.ylim(-3, 3)
pyplot.legend()
pyplot.show()