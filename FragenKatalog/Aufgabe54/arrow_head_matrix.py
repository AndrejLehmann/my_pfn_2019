#!/usr/bin/env python3

import numpy as np

def arrow_head_matrix(n):
    mat1 = np.zeros((n, n), dtype = int)
    mat2 = np.zeros((n, n), dtype = int)
    mat1[0,1:] = 1                  #|
    mat2[1:,0] = 1                  #| !!!
    mat3 = np.diag(np.ones((n)))    #|
    #mat3[0,0] = 0
    #for c in range(n):
    #    mat1[c][0] = 1
    #    mat1[c][c] = 1
    return mat1 + mat2 + mat3

print(arrow_head_matrix(5))
