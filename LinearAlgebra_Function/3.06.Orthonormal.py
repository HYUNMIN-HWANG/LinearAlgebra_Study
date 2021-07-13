# orthonormal basis vector
# ||Vi|| = 1

import numpy as np
from scipy.linalg import orth

'''scipy.linalg.orth'''
A = np.array([[2, 0, 0], [0, 5, 0]])
print(A)
# [[2 0 0]
#  [0 5 0]]

orth_A = orth(A)
print(orth_A)
# [[0. 1.]
#  [1. 0.]]

print(orth_A.T @ orth_A)
# [[1. 0.]
#  [0. 1.]]


orth_AT = orth(A.T)
print(orth_AT)
# [[0. 1.]
#  [1. 0.]
#  [0. 0.]]

print(orth_AT.T @ orth_AT)
# [[1. 0.]
#  [0. 1.]]
