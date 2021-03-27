#!/usr/bin/env python
# coding: utf-8

import numpy as np
import scipy
from   sklearn import preprocessing 

#Definición de matriz simétrica
import numpy as np
from numpy import linalg as LA


# Definición de matriz simétrica
def its_simetric(matrix, order):
    """
    inputs:
        matrix: a cuadratic matix
        order: the number of raws in the matix

    outputs:


    """
    simetrica = True
    for i in range(orden):
        for j in range(orden):
            if (matriz[i][j] != matriz[j][i]):
                simetric = False
    return simetric


def is_pos_def(x):
    """

    input:
        param x: matrix to check if it  is define positive

        return: True if the matix is define positive and False otherwise



        Checks if a matix is define positive to know the problem is being solve
        is convex and can be treated by the cojugate gradiant method.

    """
    return np.all(np.linalg.eigvals(x) > 0)


def cgm(A,b,x):
    """
    A: matrix
    b: vector
    x: soluction vector
    """
    r = np.dot(A,x)-b
    p = -r
    k = 0
    
    while True: 
        r_s = np.dot(np.transpose(r),r)
        alpha_k = r_s/np.dot(np.transpose(p),np.dot(A,p))
        
        x = x + np.dot(alpha_k,p)
        
        r = r + np.dot(alpha_k, np.dot(A,p))
        
        beta = np.dot(np.transpose(r),r)/r_s
        
        p = -r + beta*p
        
        k = k+1
        if np.linalg.norm(r) < 1e-10:
            break    
    return x
    