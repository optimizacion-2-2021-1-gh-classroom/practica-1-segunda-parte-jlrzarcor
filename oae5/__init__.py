#!/usr/bin/env python
# coding: utf-8

import numpy as np
import scipy
from   sklearn import preprocessing


def cgm(A,b,x):
    """
    input:
            A: Coeficient matrix
            b: solution vector
            x: vector to be optimize
        output:
            x: optimiza vector
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
        if k > 10:
            break    
    return x


# Definición de matriz simétrica
def its_simetric_o(matrix, order):
    """
    inputs:
        matrix: a cuadratic matix
        order: the number of raws in the matix
    outputs:
        True ir our matrix is simetric, false otherwise
    """
    simetrica = True
    for i in range(orden):
        for j in range(orden):
            if (matriz[i][j] != matriz[j][i]):
                simetric = False
    return simetric


def its_simetric(matrix):
    """
    inputs:
        matrix: a cuadratic matix
    outputs:
        True ir our matrix is simetric, false otherwise
    """
    matrix_t = np.transpose(matrix)
    return matrix.all() == matrix_t.all()


def symmetrize(n):
    """
    input:
        n: size of the symmetric matrix required 
    optput:
        symetric matix
    """
    
    a = np.random.randint(10, size=(n,n))

    return a + a.T - np.diag(a.diagonal())

def symmetrize_posdef(n):
    """
    input:
        n: size of the symmetric matrix required
    optput:
        symetric define positive matix
    """
    while True:

        a = np.random.randint(10, size=(n,n))
        if np.all(np.linalg.eigvals(a) > 0):
            break
        else:
            a = np.random.randint(10, size=(n,n))
            
    return a

def is_pos_def(x):
    """
    input:
        param x: matrix to check if it  is define positive
        return: True if the matix is define positive and False otherwise
        Checks if a matix is define positive to know the problem is being solve
        is convex and can be treated by the cojugate gradiant method.
    """
    return np.all(np.linalg.eigvals(x) > 0)

