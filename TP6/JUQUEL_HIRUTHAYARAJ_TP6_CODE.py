
# calculer les polynômes d'Hermite

import numpy
import matplotlib.pyplot as pyplot

# Fonction qui calcule les polynômes d'Hermite


def phi1(x):
    return 0 if x < 0 or x > 1 else (x-1)**2*(1+2*x)


def phi2(x):
    return 0 if x < 0 or x > 1 else x**2*(3-2*x)


def phi3(x):
    return 0 if x < 0 or x > 1 else x*(x-1)**2


def phi4(x):
    return 0 if x < 0 or x > 1 else (x-1)*x**2


# Fonction qui calcule le polynôme d'Hermite P(x)


def foncHermite(X, Y, V, x):
    n = len(X)
    P = 0
    for k in range(n-1):
        d = X[k+1]-X[k]
        t = (x-X[k])/d
        P += Y[k] * phi1(t) + Y[k+1]*phi2(t) + d*(V[k]*phi3(t)+V[k+1]*phi4(t))
    return P


def vecteurB(Y):
    Z = numpy.zeros(len(Y), dtype=int)
    for k in range(1, len(Y)-1):
        Z[k] = 3*(Y[k+1]-Y[k-1])
    Z[0] = 3*(Y[1]-Y[0])
    Z[-1] = 3*(Y[-1]-Y[-2])
    return Z


def matriceS(n):
    diag = numpy.zeros(n, dtype=int)
    diag.fill(4)
    diag[0] = 2
    diag[-1] = 2
    sur_sous_diag = numpy.zeros(n-1, dtype=int)
    sur_sous_diag.fill(1)
    S = numpy.diag(diag) + numpy.diag(sur_sous_diag, k=1) + \
        numpy.diag(sur_sous_diag, k=-1)
    return S


X = [7, 0, -8, -8, 0, 7]
Y = [0, 4, -3, 3, -4, 0]
T = [0, 1, 2, 3, 4, 5]

Bx = vecteurB(X)
By = vecteurB(Y)

S = matriceS(len(X))

Xp = numpy.linalg.solve(S, Bx)
Yp = numpy.linalg.solve(S, By)

x = numpy.linspace(T[0], T[-1], 500)
Xaff = [foncHermite(T, X, Xp, t) for t in x]
Yaff = [foncHermite(T, Y, Yp, t) for t in x]

pyplot.plot(Xaff, Yaff)
# pyplot.legend()
pyplot.show()
