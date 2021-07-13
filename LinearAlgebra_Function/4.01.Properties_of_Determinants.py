# Properties of the Determinants 
# https://www.codeformech.com/determinant-linear-algebra-using-python/

import numpy as np

# 1)The determinant of a matrix and the transpose of a matrix are equal.
P = np.array([[1,3,5],[2,0,4],[4,2,7]])
print('Matrix P:')
print(P)

print('Transpose of Matrix P:')
print(P.T)

print('Determinant of Matrix P:')
print(np.around(np.linalg.det(P), decimals=4))   # Rounding the value

print('Determinant of the Transpose of Matrix P:')
print(np.around(np.linalg.det(P.T), decimals=4))   # Rounding the value

"""
Matrix P:
[[1 3 5]
 [2 0 4]
 [4 2 7]]
Transpose of Matrix P:
[[1 2 4]
 [3 0 2]
 [5 4 7]]
Determinant of Matrix P:
18.0
Determinant of the Transpose of Matrix P:
18.0
"""

print("="*30)

# 2) Shifting the parallel lines by one place changes the sign of the determinant keeping the absolute value the same.
A = np.array([[3,5,1],[2,4,9],[7,1,6]])
A_dash = np.array([[2,4,9],[3,5,1],[7,1,6]])

print('Matrix A:')
print(A)
print('Determinant of Matrix A:')
print(np.around(np.linalg.det(A), decimals=4))   # Rounding the value
print('------------------------------')

print("Matrix A':")
print(A_dash)
print("Determinant of Matrix A':")
print(np.around(np.linalg.det(A_dash),      decimals=4))   # Rounding the value

"""
Matrix A:
[[3 5 1]
 [2 4 9]
 [7 1 6]]
Determinant of Matrix A:
274.0
------------------------------
Matrix A':
[[2 4 9]
 [3 5 1]
 [7 1 6]]
Determinant of Matrix A':
-274.0
"""

print("="*30)

# 3) If any two lines of a matrix are the same, then the determinant is zero.
B = np.array([[2,3,5],[2,3,5],[7,11,13]])

print("Matrix B:")
print(B)
print("Determinant of Matrix B:")
print(np.around(np.linalg.det(B), decimals=4))   # Rounding the value

"""
Matrix B:
[[ 2  3  5]
 [ 2  3  5]
 [ 7 11 13]]
Determinant of Matrix B:
0.0
"""

print("="*30)

# 4) If a line of a determinant is multiplied by a scalar, 
# the value of the new determinant can be calculated by multiplying the value of the original determinant by the same scalar value.

R = np.array([[2,1,3,0],[1,0,2,3],[3,2,0,1],[2,0,1,3]])
# 3rd row of the determinant is multiplied by 4
R_dash = np.array([[2,1,3,0],[1,0,2,3],[12,8,0,4],[2,0,1,3]])

print('Matrix R:')
print(R)
print('Determinant of Matrix R:')
print(np.around(np.linalg.det(R), decimals=4))   # Rounding the value
print('------------------------------')

print("Matrix R':")
print(R_dash)
print("Determinant of Matrix R':")
print(np.around(np.linalg.det(R_dash), decimals=4))   # Rounding the value

"""
Matrix R:
[[2 1 3 0]
 [1 0 2 3]
 [3 2 0 1]
 [2 0 1 3]]
Determinant of Matrix R:
-24.0
------------------------------
Matrix R':
[[ 2  1  3  0]
 [ 1  0  2  3]
 [12  8  0  4]
 [ 2  0  1  3]]
Determinant of Matrix R':
-96.0
"""

print("="*30)

# 5) If any line of the determinant has each element as a sum of  't' terms, 
# then the determinant can be written as the sum of 't' determinants.
# |L| = |L1| + |L2| + |L3|

L = np.array([[1,5,12],[3,2,11],[4,5,17]])
L1 = np.array([[1,5,5],[3,2,2],[4,5,5]])
L2 = np.array([[1,5,5],[3,2,2],[4,5,5]])
L3 = np.array([[1,5,2],[3,2,7],[4,5,7]])

print('Matrix L:')
print(L)
print('Matrix L1 = L2:')
print(L1)
print('Matrix L3:')
print(L3)
print('------------------------------')

print('Determinant of Matrix L:')
print(np.around(np.linalg.det(L), decimals=4))   # Rounding the value
print('Determinant of Matrix L1 = L2:')
print(np.around(np.linalg.det(L1), decimals=4))   # Rounding the value
print('Determinant of Matrix L3:')
print(np.around(np.linalg.det(L3), decimals=4))   # Rounding the value

"""
Matrix L:
[[ 1  5 12]
 [ 3  2 11]
 [ 4  5 17]]
Matrix L1 = L2:
[[1 5 5]
 [3 2 2]
 [4 5 5]]
Matrix L3:
[[1 5 2]
 [3 2 7]
 [4 5 7]]
------------------------------
Determinant of Matrix L:
28.0
Determinant of Matrix L1 = L2:
0.0
Determinant of Matrix L3:
28.0
"""

print("="*30)


# 6) The value of the determinant remains the same if a line is added by multiples of one or more parallel lines.
# Let’s take one example where 1st column is added with 3 times the 2ns column and 2 times the 3rd column, 
# i.e. . C1 = C1 + 3C2 + 2C3

A = np.array([[1,3,2],[3,2,1],[2,1,3]])
A_dash = np.array([[14,3,2],[11,2,1],[11,1,3]])

print('Matrix A:')
print(A)
print("Matrix A':")
print(A_dash)
print('------------------------------')

print('Determinant of Matrix A:')
print(np.around(np.linalg.det(A), decimals=4))   # Rounding the value
print("Determinant of Matrix A':")
print(np.around(np.linalg.det(A_dash), decimals=4))   # Rounding the value

"""
Matrix A:
[[1 3 2]
 [3 2 1]
 [2 1 3]]
Matrix A':
[[14  3  2]
 [11  2  1]
 [11  1  3]]
------------------------------
Determinant of Matrix A:
-18.0
Determinant of Matrix A':
-18.0
"""

print("="*30)

# 7) determinant Identity = 1

A = np.array([[1,0,0],[0,1,0],[0,0,1]])
print('Determinant of Matrix A:')
print(np.linalg.det(A))
# Determinant of Matrix A:
# 1.0

print("="*30)

# 8) If Matrix has a zero-row, determinant = 0

A = np.array([[0,0,0],[0,1,0],[0,0,1]])
print('Determinant of Matrix A:')
print(np.linalg.det(A))
# Determinant of Matrix A:
# 0.0

print("="*30)

# 9) The product of the determinants of two matrices of the same order is equal to the determinant of the product of those matrices.
# |AB| = |A| * |B|
A = np.array([[1,3,2],[3,2,1],[2,1,3]])
B = np.array([[2,8,5],[1,5,7],[6,4,9]])
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

AB = np.matmul(A,B)  # Matrix multiplication
det_AB = np.linalg.det(AB)

print('Matrix A:')
print(A)
print("Matrix B:")
print(B)
print('Matrix AB:')
print(AB)
print('------------------------------')
print('Determinant of Matrix A:')
print(np.around(det_A, decimals=4))   # Rounding the value
print('Determinant of Matrix B:')
print(np.around(det_B, decimals=4))   # Rounding the value
print('------------------------------')
print('Multiplication of Determinants of the matrices A and B (|A|x|B|):')
print(det_A*det_B)
print('Determinant of Matrix AB (|AB|):')
print(np.around(det_AB, decimals=4))   # Rounding the value

"""
Matrix A:
[[1 3 2]
 [3 2 1]
 [2 1 3]]
Matrix B:
[[2 8 5]
 [1 5 7]
 [6 4 9]]
Matrix AB:
[[17 31 44]
 [14 38 38]
 [23 33 44]]
------------------------------
Determinant of Matrix A:
-18.0
Determinant of Matrix B:
168.0
------------------------------
Multiplication of Determinants of the matrices A and B (|A|x|B|):
-3023.999999999999
Determinant of Matrix AB (|AB|):
-3024.0
"""

print("="*30)

# 10) The determinants of a Triangular Matrix and Diagonal Matrix (elements on one side of the principal diagonal are all zeros) are the product of all the diagonal elements.
A = np.array([[1,2,3],[0,4,5],[0,0,6]]) # Upper Triangular Matrix
B = np.array([[4,0,0],[0,3,0],[0,0,7]]) # Diagonal Matrix

print('Matrix A:')
print(A)
print('Determinant of Matrix A:')
print(np.around(np.linalg.det(A), decimals=4))   # Rounding the value
print('Multiplication of Diagonal Elements (1x4x6):')
print(1*4*6)
print('------------------------------')

print("Matrix B:")
print(B)
print('Determinant of Matrix B:')
print(np.around(np.linalg.det(B), decimals=4))   # Rounding the value
print('Multiplication of Diagonal Elements (4x3x7):')
print(4*3*7)

"""
Matrix A:
[[1 2 3]
 [0 4 5]
 [0 0 6]]
Determinant of Matrix A:
24.0
Multiplication of Diagonal Elements (1x4x6):
24
------------------------------
Matrix B:
[[4 0 0]
 [0 3 0]
 [0 0 7]]
Determinant of Matrix B:
84.0
Multiplication of Diagonal Elements (4x3x7):
84
"""

print("="*30)

# 11) determinant A^T == determinant A

A = np.array([[2,8,5],[1,5,7],[6,4,9]])
AT = A.T

print('Matrix A:')
print(A)
print('Determinant of Matrix A:')
print(np.around(np.linalg.det(A), decimals=4))   # Rounding the value
print('------------------------------')
print('Matrix AT:')
print(AT)
print('Determinant of Matrix A^T:')
print(np.around(np.linalg.det(AT), decimals=4))   # Rounding the value

"""
Matrix A:
[[2 8 5]
 [1 5 7]
 [6 4 9]]
Determinant of Matrix A:
168.0
------------------------------
Matrix AT:
[[2 1 6]
 [8 5 4]
 [5 7 9]]
Determinant of Matrix A^T:
168.0
"""
