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