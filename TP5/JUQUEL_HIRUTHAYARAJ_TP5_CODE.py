
# calculer les polynômes d'Hermite

import sys
sys.setrecursionlimit(10000)

import numpy as np
import matplotlib.pyplot as plt

# Fonction qui calcule les polynômes d'Hermite

def phi1(x):
    return 1

def phi2(x):
    return 2*x

def phi3(x):
    return 4*x**2 - 2

def phi4(x):
    return 8*x**3 - 12*x
    

X = [1, 5]
Y = [6, 2]
V = [3/2, -3]

# Fonction qui calcule le polynôme d'interpolation d'Hermite

def Hermite(X, Y, V, x):
    n = len(X)
    h = X[1] - X[0]
    S = 0
    for i in range(n):
        S += Y[i]*phi1((x-X[i])/h) + V[i]*phi2((x-X[i])/h) + (1/(6*h**2))*(phi3((x-X[i])/h)*(Y[i+1]-Y[i]) + phi4((x-X[i])/h)*(V[i+1]-V[i]))
    return S

# Affichage du graphique

x = np.linspace(1, 5, 100)
y = Hermite(X, Y, V, x)
plt.plot(x, y)
plt.show()