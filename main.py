#!/usr/bin/env python3

import numpy

def vander(n):
    liste = list(range(n+1))
    res = numpy.vander(liste,increasing=True)
    return res

def main():
    print(vander(5))


main()
