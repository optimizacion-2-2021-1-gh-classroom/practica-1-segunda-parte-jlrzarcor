#!/usr/bin/env python
# coding: utf-8

import numpy as np
import scipy
from   sklearn import preprocessing 

#Definición de matriz simétrica
def es_simetrica(matriz,orden):
    simetrica=True
    for i in range (orden):
        for j in range (orden):
            if (matriz[i][j]!=matriz[j][i]):
                simetrica=False
    return simetrica
   
   
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
    