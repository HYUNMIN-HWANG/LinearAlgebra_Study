# LU decomposition

import numpy as np
import scipy
import scipy.linalg # Linear Algebra Library

A = scipy.array([ [7,3,-1,2],[3,8,1,-4],[-1,1,4,-1],[2,-1,-1,6]])
P, L, U = scipy.linalg.lu(A)    # P : Permutation , L : Lower, U : Upper

# PA = LU

print("A : ")
print(A)

print("P : ")
print(P)

print("L : ")
print(L)

print("U : ")
print(U)

"""
A : 
[[ 7  3 -1  2]
 [ 3  8  1 -4]
 [-1  1  4 -1]
 [ 2 -1 -1  6]]
P :
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
L :
[[ 1.          0.          0.          0.        ]
 [ 0.42857143  1.          0.          0.        ]
 [-0.14285714  0.21276596  1.          0.        ]
 [ 0.28571429 -0.27659574 -0.08982036  1.        ]]
U :
[[ 7.          3.         -1.          2.        ]
 [ 0.          6.71428571  1.42857143 -4.85714286]
 [ 0.          0.          3.55319149  0.31914894]
 [ 0.          0.          0.          4.11377246]]
"""