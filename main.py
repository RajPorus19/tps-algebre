#!/usr/bin/env python3

import numpy

def vander(n:int):
    liste = list(range(n+1))
    res = numpy.vander(liste,increasing=True)
    return res

def mat_colonne(liste:list):
    return numpy.array(liste)

def main(n:int):
    mat_vander = vander(n)
    #print('La matrice vander associé  à ',n,mat_vander)
    A=np.linalg.solve(mat_vander, Y)


main()
