# Compte rendu TP5 - Interpolation polynomiale : Base d'Hermite

## I. Base d'Hermite

|   | ![phi1](https://latex.codecogs.com/gif.latex?%5Cphi_1) | ![phi2](https://latex.codecogs.com/gif.latex?%5Cphi_2) | ![phi3](https://latex.codecogs.com/gif.latex?%5Cphi_3) | ![phi4](https://latex.codecogs.com/gif.latex?%5Cphi_4) |
|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cphi%280%29) | 1 | 0 | 0 | 0 |
| ![](https://latex.codecogs.com/gif.latex?%5Cphi%281%29) | 0 | 1 | 0 | 0 |
| ![](https://latex.codecogs.com/gif.latex?%5Cphi%5E1%280%29) | 0 | 0 | 1 | 0 |
| ![](https://latex.codecogs.com/gif.latex?%5Cphi%5E1%281%29) | 0 | 0 | 0 | 1 |

On obtient:

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_1%28x%29%20%3D%20%28x-1%29%5E2%281&plus;2x%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_2%28x%29%20%3D%20x%5E2%283-2x%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_3%28x%29%20%3D%20x%28x-1%29%5E2)

![equation](https://latex.codecogs.com/gif.latex?%5Cphi_4%28x%29%20%3D%20%28x-1%29x%5E2)

Allure des courbes de la base d'Hermite:

![courbes](./images/hermite.png)
![courbes](./images/hermite2.png)

![courbes](./images/hermite3.png)
![courbes](./images/hermite4.png)

1. On cherche un polynome P de degré 3 tel que :

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%280%29%20%3D%20Y_0%20%5C%5C%20P%281%29%20%3D%20Y_1%20%5C%5C%20P%27%280%29%20%3D%20V_0%20%5C%5C%20P%27%281%29%20%3D%20V_1%20%5Cend%7Bcases%7D)

![equation](https://latex.codecogs.com/gif.latex?P%28x%29%20%3D%20Y_0%20%5Cphi_1%28x%29%20&plus;%20Y_1%20%5Cphi_2%28x%29%20&plus;%20V_0%20%5Cphi_3%28x%29%20&plus;%20V_1%20%5Cphi_4%28x%29)

car

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%280%29%20%3D%20Y_0%20%5Ctimes1%20&plus;%20Y_1%20%5Ctimes0%20&plus;%20V_0%20%5Ctimes0%20&plus;%20V_1%20%5Ctimes0%20%3D%20Y_0%20%5C%5C%20P%281%29%20%3D%20Y_0%20%5Ctimes0%20&plus;%20Y_1%20%5Ctimes1%20&plus;%20V_0%20%5Ctimes0%20&plus;%20V_1%20%5Ctimes0%20%3D%20Y_1%20%5C%5C%20P%27%280%29%20%3D%20Y_0%20%5Ctimes0%20&plus;%20Y_1%20%5Ctimes0%20&plus;%20V_0%20%5Ctimes1%20&plus;%20V_1%20%5Ctimes0%20%3D%20V_0%20%5C%5C%20P%27%281%29%20%3D%20Y_0%20%5Ctimes0%20&plus;%20Y_1%20%5Ctimes0%20&plus;%20V_0%20%5Ctimes0%20&plus;%20V_1%20%5Ctimes1%20%3D%20V_1%20%5Cend%7Bcases%7D)

1. On cherche un polynome P de degré 3 qui passe par deux points A et B et dont on connaît les dérivées VA et VB en XA et XB.

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%28X_A%29%20%3D%20Y_A%20%5C%5C%20P%28X_B%29%20%3D%20Y_B%20%5C%5C%20P%27%28X_A%29%20%3D%20V_A%20%5C%5C%20P%27%28X_B%29%20%3D%20V_B%20%5Cend%7Bcases%7D)

On pose 

![equation](https://latex.codecogs.com/gif.latex?t%20%3D%20%5Cfrac%7Bx-X_A%7D%7BX_B-X_A%7D)

![equation](https://latex.codecogs.com/gif.latex?P%28x%29%20%3D%20Y_A%20%5Cphi_1%28t%29%20&plus;%20Y_B%20%5Cphi_2%28t%29%20&plus;%20V_A%20%5Cphi_3%28t%29%20&plus;%20V_B%20%5Cphi_4%28t%29)

car

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%28X_A%29%20%3D%20Y_A%20%5Ctimes1%20&plus;%20Y_B%20%5Ctimes0%20&plus;%20V_A%20%5Ctimes0%20&plus;%20V_B%20%5Ctimes0%20%3D%20Y_A%20%5C%5C%20P%28X_B%29%20%3D%20Y_A%20%5Ctimes0%20&plus;%20Y_B%20%5Ctimes1%20&plus;%20V_A%20%5Ctimes0%20&plus;%20V_B%20%5Ctimes0%20%3D%20Y_B%20%5C%5C%20P%27%28X_A%29%20%3D%20Y_A%20%5Ctimes0%20&plus;%20Y_B%20%5Ctimes0%20&plus;%20V_A%20%5Ctimes1%20&plus;%20V_B%20%5Ctimes0%20%3D%20V_A%20%5C%5C%20P%27%28X_B%29%20%3D%20Y_A%20%5Ctimes0%20&plus;%20Y_B%20%5Ctimes0%20&plus;%20V_A%20%5Ctimes0%20&plus;%20V_B%20%5Ctimes1%20%3D%20V_B%20%5Cend%7Bcases%7D)

Exemple:

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%281%29%20%3D%206%20%5C%5C%20P%285%29%20%3D%202%20%5C%5C%20P%27%281%29%20%3D%20%5Cfrac%7B3%7D%7B2%7D%20%5C%5C%20P%27%285%29%20%3D%20-3%20%5Cend%7Bcases%7D)

![equation](https://latex.codecogs.com/gif.latex?P%28x%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-1%7D%7B4%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-5%7D%7B-4%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-1%7D%7B4%7D%20%5Cright%29%5E2%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-5%7D%7B-4%7D%20%5Cright%29%5E2)

3. Faire la même chose

Soit

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%285%29%20%3D%202%20%5C%5C%20P%287%29%20%3D%20-1%20%5C%5C%20P%27%285%29%20%3D%20-3%20%5C%5C%20P%27%287%29%20%3D%200%20%5Cend%7Bcases%7D)

alors

![equation](https://latex.codecogs.com/gif.latex?P%28x%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-5%7D%7B2%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-7%7D%7B-2%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-5%7D%7B2%7D%20%5Cright%29%5E2%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-7%7D%7B-2%7D%20%5Cright%29%5E2)

Soit

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%287%29%20%3D%20-1%20%5C%5C%20P%288%29%20%3D%201%20%5C%5C%20P%27%287%29%20%3D%200%20%5C%5C%20P%27%288%29%20%3D%204%20%5Cend%7Bcases%7D)

alors

![equation](https://latex.codecogs.com/gif.latex?P%28x%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-7%7D%7B1%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-8%7D%7B-1%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-7%7D%7B1%7D%20%5Cright%29%5E2%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-8%7D%7B-1%7D%20%5Cright%29%5E2)

Soit

![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20P%288%29%20%3D%201%20%5C%5C%20P%2810%29%20%3D%202%20%5C%5C%20P%27%288%29%20%3D%204%20%5C%5C%20P%27%2810%29%20%3D%201%20%5Cend%7Bcases%7D)

alors

![equation](https://latex.codecogs.com/gif.latex?P%28x%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-8%7D%7B2%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%28%20%5Cfrac%7Bx-10%7D%7B-2%7D%20%5Cright%29%5E3%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-8%7D%7B2%7D%20%5Cright%29%5E2%20&plus;%20%5Cfrac%7B3%7D%7B4%7D%20%5Cleft%28%20%5Cfrac%7Bx-10%7D%7B-2%7D%20%5Cright%29%5E2)

## II. Interpolation polynomiale

1. On écrit les fonction phi1, phi2, phi3, phi4 nulles en dehor de l'intervalle [0,1]:

```python
def phi1(x):
    return 0 if x < 0 or x > 1 else (x-1)**2*(1+2*x)


def phi2(x):
    return 0 if x < 0 or x > 1 else x**2*(3-2*x)


def phi3(x):
    return 0 if x < 0 or x > 1 else x*(x-1)**2


def phi4(x):
    return 0 if x < 0 or x > 1 else (x-1)*x**2
```

2. Stockage des tableaux X,Y et V:

```python
X = [-5, -2, 0, 3, 6]
Y = [-4, -1, 1, 1, -1]
V = [3, 0, 3, -2, 0]
```

3. Ecriture de foncHermite qui renvoie le polynome de Hermite:

```python
def foncHermite(X, Y, V, x):
    n = len(X)
    P = 0
    for k in range(n-1):
        d = X[k+1]-X[k]
        t = (x-X[k])/d
        P += Y[k] * phi1(t) + Y[k+1]*phi2(t) + d*(V[k]*phi3(t)+V[k+1]*phi4(t))
    return P
```

4. Affichage de la courbe représentative de P:

```python
import numpy
import matplotlib.pyplot as pyplot

x = numpy.linspace(X[0], X[-1], 500)
pyplot.plot(x, [foncHermite(X, Y, V, i) for i in x])
pyplot.show()
```

![alt text](./images/curve.png)

5. Ajout des tangentes:

```python
import numpy
import matplotlib.pyplot as pyplot

x = numpy.linspace(0, 10, 500)
pyplot.plot(x, [foncHermite(X, Y, V, i) for i in x])
for k in range(len(X)):
    pyplot.plot((X[k]-1, X[k]+1), (Y[k]-V[k], Y[k]+V[k]))
pyplot.show()
```

![alt text](./images/curve2.png)

voila.