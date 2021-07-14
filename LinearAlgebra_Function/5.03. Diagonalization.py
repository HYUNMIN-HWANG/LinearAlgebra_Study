#  Diagonalization Theorem
# M = P * D * inv(P)

import numpy 
from sympy import * 
M = Matrix([[3, -2, 4, -2],
            [5, 3, -3, -2],
            [5, -2, 2, -2],
            [5, -2, -3, 3]])

M = Matrix(([0.5, 0.5],[0.5,0.5]))
print("Matrix : {} ".format(M))

# Use sympy.diagonalize() method
P, D = M.diagonalize()
	
print("Eigenvector of a matrix : {}".format(P))
print("Diagonal of a matrix : {}".format(D))    # Eigenvalue들이 diagonal 형태로 있는 행렬
print(P*D*P**-1)

# Matrix : Matrix([[0.500000000000000, 0.500000000000000], [0.500000000000000, 0.500000000000000]]) 
# Eigenvector of a matrix : Matrix([[-0.707106781186548, -0.707106781186548], [0.707106781186548, -0.707106781186548]])
# Diagonal of a matrix : Matrix([[0, 0], [0, 1.00000000000000]])
# Matrix([[0.500000000000000, 0.500000000000000], [0.500000000000000, 0.500000000000000]])