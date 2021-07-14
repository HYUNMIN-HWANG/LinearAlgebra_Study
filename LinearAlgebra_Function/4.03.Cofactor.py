# Minors and Cofactors of a Matrix using Python
# Minor matrix : Aij -> i행, j열을 제거한 Submatirx

import numpy as np

# Minor matrix의 determinant
def minor_of_element(A,i,j):
    sub_A = np.delete(A,i-1,0)     # Delete i-th row
    sub_A = np.delete(sub_A,j-1,1) # Delete j-th column
    M_ij = np.linalg.det(sub_A)    # Minor of the element at ith row and jth column
    return np.around(M_ij,decimals=3)  # Rounding the value

P = np.array([[1,3,5],[2,0,4],[4,2,7]])
print('Matrix P:')
print(P)
print('Minor of the element at 1st row and 1st column:')
print(minor_of_element(P,1,1))
print('Minor of the element at 3rd row and 2nd column:')
print(minor_of_element(P,3,2))

# Matrix P:
# [[1 3 5]
#  [2 0 4]
#  [4 2 7]]
# Minor of the element at 1st row and 1st column:
# -8.0
# Minor of the element at 3rd row and 2nd column:
# -6.0

print("="*30)

# 각각의 Minor matrix의 determinant들로 만든 새로운 행렬
def minor_matrix(A):
    m = np.shape(A)[0]    # Order of the matrix
    M_A = np.zeros([m,m])   # Initializing the minor matrix with zeros
    for i in range(1,m+1):
        for j in range(1,m+1):
            M_A[i-1,j-1] = minor_of_element(A,i,j)
    return M_A

P = np.array([[1,3,5],[2,0,4],[4,2,7]])
print('Matrix P:')
print(P)
print('Minor Matrix of P:')
print(minor_matrix(P))

# Matrix P:
# [[1 3 5]
#  [2 0 4]
#  [4 2 7]]
# Minor Matrix of P:
# [[ -8.  -2.   4.]
#  [ 11. -13. -10.]
#  [ 12.  -6.  -6.]]

print("="*30)

# row의 pivoting 횟수만큼 부호가 바뀐다. : (-1) 을 i + j 제곱한 값이 부호가 됨
def cofactor_matrix(A):
    m = np.shape(A)[0]   # Order of the matrix
    C_A = np.zeros([m,m])   # Initializing the cofactor matrix with zeros
    for i in range(1,m+1):
        for j in range(1,m+1):
            C_A[i-1,j-1] = pow(-1,i+j)*minor_of_element(A,i,j)
    return C_A

P = np.array([[1,3,5],[2,0,4],[4,2,7]])
print('Matrix P:')
print(P)
print('Cofactor Matrix of P:')
print(cofactor_matrix(P))

# Matrix P:
# [[1 3 5]
#  [2 0 4]
#  [4 2 7]]
# Cofactor Matrix of P:
# [[ -8.   2.   4.]
#  [-11. -13.  10.]
#  [ 12.   6.  -6.]]
