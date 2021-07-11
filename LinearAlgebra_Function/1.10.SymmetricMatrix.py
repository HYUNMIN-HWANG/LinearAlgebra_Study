# 대칭행렬
# Symmetric Matrix
# A^T = A

import numpy as np
# M = np.array([[2,3,4], [3,45,8], [4,8,78]])
M = np.array([[1,2,3], [3,4,5], [4,5,6]])
print("Matrix M :\n", M)

# Transposing matrix M
print("Transposing matrix M : \n",M.T)

print("\nIs it Symmetric????")
# if M.T.all() == M.all() and np.shape(M) == np.shape(M.T):
#     print("\tYes, Tranpose is equal to M!")
# else :
#     print("\tNo, Not Tranpose!")

if np.array_equal(M, M.T) and np.shape(M) == np.shape(M.T):
    print("\tYes, Tranpose is equal to M!")
else :
    print("\tNo, Not Tranpose!")

"""
ex1)
Matrix M :
 [[ 2  3  4]
 [ 3 45  8]
 [ 4  8 78]]
Transposing matrix M :
 [[ 2  3  4]
 [ 3 45  8]
 [ 4  8 78]]

Is it Symmetric????
        Yes, Tranpose is equal to M!


ex2)
Matrix M :
 [[1 2 3]
 [3 4 5]
 [4 5 6]]
Transposing matrix M :
 [[1 3 4]
 [2 4 5]
 [3 5 6]]

Is it Symmetric????
        No, Not Tranpose!
"""
