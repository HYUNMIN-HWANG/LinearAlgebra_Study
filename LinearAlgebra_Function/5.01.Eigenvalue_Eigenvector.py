# Eigenvalue & Eigenvector
# A*x = ㅅ*x
# x : Eigenvector
# ㅅ: Eigenvalue

# det (A - ㅅI) = 0

import numpy as np
from numpy.linalg import eig

testmatirx = np.array([[4, -5],[2, -3]])
eig_val, eig_vec = eig(testmatirx)

print("Eigenvalue : \n", eig_val)
print("Eigenvector : \n", eig_vec)


# Eigenvalue :
#  [ 2. -1.]
# Eigenvector :
#  [[0.92847669 0.70710678]
#  [0.37139068 0.70710678]]
