# QR decomposition
# A = Q*R
#   Q : Gram Schmidt로 구한 Q
#   R : Upper triangular matrix


import numpy as np

A = np.array([[0, 1], [1, 1], [1, 1], [2, 1]])
# A = np.array([[1,1,2], [0,0,1], [1,0,0]])
print("A : \n", A)
# [[0 1]
#  [1 1]
#  [1 1]
#  [2 1]]

q, r = np.linalg.qr(A)
print("Q : \n", q)
# [[ 0.          0.8660254 ]
#  [-0.40824829  0.28867513]
#  [-0.40824829  0.28867513]
#  [-0.81649658 -0.28867513]]

print("R : \n", r)
# [[-2.44948974 -1.63299316]
#  [ 0.          1.15470054]]

print("A = QR : \n", q@r)
# [[0. 1.]
#  [1. 1.]
#  [1. 1.]
#  [2. 1.]]

''''
A : 
 [[0 1]
 [1 1]
 [1 1]
 [2 1]]
Q :
 [[ 0.          0.8660254 ]
 [-0.40824829  0.28867513]
 [-0.40824829  0.28867513]
 [-0.81649658 -0.28867513]]
R :
 [[-2.44948974 -1.63299316]
 [ 0.          1.15470054]]
A = QR :
 [[0. 1.]
 [1. 1.]
 [1. 1.]
 [2. 1.]]


A : 
 [[1 1 2]
 [0 0 1]
 [1 0 0]]
Q :
 [[-0.70710678 -0.70710678  0.        ]
 [-0.          0.          1.        ]
 [-0.70710678  0.70710678  0.        ]]
R :
 [[-1.41421356 -0.70710678 -1.41421356]
 [ 0.         -0.70710678 -1.41421356]
 [ 0.          0.          1.        ]]
A = QR :
 [[ 1.00000000e+00  1.00000000e+00  2.00000000e+00]
 [ 0.00000000e+00  0.00000000e+00  1.00000000e+00]
 [ 1.00000000e+00 -1.33393446e-16 -2.66786891e-16]]
 '''