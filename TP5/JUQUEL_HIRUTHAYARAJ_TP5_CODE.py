
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

# Allure des courbes


# x = numpy.linspace(0, 1, 500)
# pyplot.plot(x, [phi1(i) for i in x], label='phi1')
# pyplot.legend()
# pyplot.show()
# pyplot.plot(x, [phi2(i) for i in x], label='phi2')
# pyplot.legend()
# pyplot.show()
# pyplot.plot(x, [phi3(i) for i in x], label='phi3')
# pyplot.legend()
# pyplot.show()
# pyplot.plot(x, [phi4(i) for i in x], label='phi4')
# pyplot.legend()
# pyplot.show()

X = [1, 5, 7, 8, 10]
Y = [6, 2, -1, 1, 2]
V = [3/2, -3, 0, 4, 1]

# Fonction qui calcule le polynôme d'Hermite P(x)


def foncHermite(X, Y, V, x):
    n = len(X)
    P = 0
    for k in range(n-1):
        d = X[k+1]-X[k]
        t = (x-X[k])/d
        P += Y[k] * phi1(t) + Y[k+1]*phi2(t) + d*(V[k]*phi3(t)+V[k+1]*phi4(t))
    return P

# Allure du polynôme d'Hermite


x = numpy.linspace(0, 10, 500)
pyplot.plot(x, [foncHermite(X, Y, V, i) for i in x])
for k in range(len(X)):
    pyplot.plot((X[k]-1, X[k]+1), (Y[k]-V[k], Y[k]+V[k]), 'r')
pyplot.show()
