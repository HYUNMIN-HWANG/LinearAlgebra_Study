# Trace Matirx
# sum along diagonals of the array.

# 행렬의 대각선의 합과, eigenvalue의 합이 동일하다.

import numpy as np
from numpy.linalg import eig

A = np.array([[4, -5],[2, -3]])

# sum along diagonals of the array.
trace = np.matrix.trace(A)
print(trace)

# sum of Egienvalue
eig_val, eig_vec = np.linalg.eig(A)
print(sum(eig_val))
