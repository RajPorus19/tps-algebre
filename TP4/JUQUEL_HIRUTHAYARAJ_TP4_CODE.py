#!/usr/bin/env python3
import numpy
import matplotlib.pyplot as pyplot
import math


def binom(n, p):
    return math.factorial(n)/(math.factorial(p)*math.factorial(n-p))


def bernstein(n, i, t):
    return binom(n, i)*(t**i)*((1-t)**(n-i))

# return a list of points N points on the bezier curve


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

# show the bezier curve and all line segments


def show(points):
    x, y = bezier(points)
    pyplot.plot(x, y)
    for i in range(len(points)):
        pyplot.plot([points[i][0]], [points[i][1]], 'ro')
        if i > 0:
            pyplot.plot([points[i-1][0], points[i][0]],
                        [points[i-1][1], points[i][1]], 'b-')
    pyplot.show()

# main function


def main():
    points = [(-0.5, 0), (2, 2.5), (-2, 2.5), (0.5, 0)]
    show(points)


if __name__ == '__main__':
    main()
