
# calculer les polynômes d'Hermite

import numpy as np
import matplotlib.pyplot as plt

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


x = np.linspace(-1, 2, 100)
plt.plot(x, [phi1(i) for i in x], label='phi1')
plt.plot(x, [phi2(i) for i in x], label='phi2')
plt.plot(x, [phi3(i) for i in x], label='phi3')
plt.plot(x, [phi4(i) for i in x], label='phi4')
plt.legend()
plt.show()

X = [1, 5]
Y = [6, 2]
V = [3/2, -3]

# Fonction qui calcule le polynôme d'Hermite P(x)


def foncHermite(X, Y, V, x):
    n = len(X)
    P = Y[0] * phi1((x-X[0])/(X[1]-X[0]))
    + Y[1] * phi2((x-X[0])/(X[1]-X[0]))
    + (X[1] - X[0]) * (V[0] * phi3((x-X[0])/(X[1]-X[0])) +
                       V[1] * phi4((x-X[0])/(X[1]-X[0])))
    return P


# Allure du polynôme d'Hermite


x = np.linspace(0, 6, 100)
plt.plot(x, [foncHermite(X, Y, V, i) for i in x])
plt.show()
