1. Fonction binomiale

On défini la fonction binomiale de deux entiers $n$ et $p$ par la formule suivante:

![equation](https://latex.codecogs.com/gif.latex?%5Cbinom%7Bn%7D%7Bp%7D%20%3D%20%5Cfrac%7Bn%21%7D%7Bp%21%28n-p%29%21%7D)

```python
import math

def binom(n, p):
    return math.factorial(n)/(math.factorial(p)*math.factorial(n-p))
```

2. Fonction de bernstein

On définit la fonction de bernstein de deux entiers $n$ et $p$ par la formule suivante:

![equation](https://latex.codecogs.com/gif.latex?B_%7Bn%2Cp%7D%28t%29%20%3D%20%5Cbinom%7Bn%7D%7Bp%7Dt%5Ep%281-t%29%5E%7Bn-p%7D)

```python
import math

def bernstein(n, i, t):
    return binom(n, i)*(t**i)*((1-t)**(n-i))
```

3. Fonction de bezier

On définit la fonction de bezier qui retourne une liste de N points de la courbe de Bezier désirée

![equation](https://latex.codecogs.com/gif.latex?B_%7Bn%2Cp%7D%28t%29%20%3D%20%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%5Cbinom%7Bn%7D%7Bi%7D%5Ccdot%20t%5Ei%5Ccdot%281-t%29%5E%7Bn-i%7D)

```python
import math

def bezier(points):
    n = len(points)
    x = []
    y = []
    for t in numpy.linspace(0, 1, 100):
        x.append(0)
        y.append(0)
        for i in range(n):
            x[-1] += bernstein(n-1, i, t)*points[i][0]
            y[-1] += bernstein(n-1, i, t)*points[i][1]
    return (x, y)
```

4. Affichage de la courbe de Bezier

```python
import matplotlib.pyplot as plt

def show(points):
    x, y = bezier(points)
    pyplot.plot(x, y)
    for i in range(len(points)):
        pyplot.plot([points[i][0]], [points[i][1]], 'ro')
    pyplot.show()

show((-0.5, 0), (2, 2.5), (-2, 2.5), (0.5, 0))
```

![courbe de bezier](./images/curve.png)

Ajout des lignes brisées

```python
import matplotlib.pyplot as plt

def show(points):
    x, y = bezier(points)
    pyplot.plot(x, y)
    for i in range(len(points)):
        pyplot.plot([points[i][0]], [points[i][1]], 'ro')
        if i > 0:
            pyplot.plot([points[i-1][0], points[i][0]],
                        [points[i-1][1], points[i][1]], 'b-')
    pyplot.show()

show((-0.5, 0), (2, 2.5), (-2, 2.5), (0.5, 0))
```

![courbe de bezier](./images/curve2.png)

voilà.