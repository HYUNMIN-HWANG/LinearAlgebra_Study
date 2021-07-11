# 4 foundamental Subspace in A
    # 1) Column Space
    # 2) Null Space
    # 3) Row Space
    # 4) Left Null Space

from sympy import *

# M = Matrix([[1,0,0],[0,0,0]])
M = Matrix([[1,3,3,2],[2,6,9,7],[-1,-3,3,4]])
print("M : " , M)
# M :  Matrix([[1, 0, 0], [0, 0, 0]])

M_T = M.T
print("M Transpose : ", M_T)
# M Transpose :  Matrix([[1, 0], [0, 0], [0, 0]])

print("============ 1) Column Space ===============")

M_columnspace = M.columnspace()
print(M_columnspace)
# [Matrix([
# [1],
# [0]])]

print("============ 3) Row Space ===============")

M_rowspace = M.rowspace()
print(M_rowspace)
# [Matrix([[1, 0, 0]])]

M_rowspace2 = M_T.columnspace()
print(M_rowspace2)
# [Matrix([
# [1],
# [0],
# [0]])]

print("============ 2) Null Space ===============")

M_nullspace = M.nullspace()
print("Nullspace of a matrix : {}".format(M_nullspace))  
# Nullspace of a matrix : [Matrix([
# [0],
# [1],
# [0]]), Matrix([
# [0],
# [0],
# [1]])]

print("============ 4) Left Null Space ===============")

M_left_nullspace = M_T.nullspace()
print(M_left_nullspace)
# [Matrix([
# [0],
# [1]])]


"""
M :  Matrix([[1, 3, 3, 2], [2, 6, 9, 7], [-1, -3, 3, 4]])
M Transpose :  Matrix([[1, 2, -1], [3, 6, -3], [3, 9, 3], [2, 7, 4]])
============ 1) Column Space ===============
[Matrix([
[ 1],
[ 2],
[-1]]), Matrix([
[3],
[9],
[3]])]
============ 3) Row Space ===============
[Matrix([[1, 3, 3, 2]]), Matrix([[0, 0, 3, 3]])]
[Matrix([
[1],
[3],
[3],
[2]]), Matrix([
[2],
[6],
[9],
[7]])]
============ 2) Null Space ===============
Nullspace of a matrix : [Matrix([
[-3],
[ 1],
[ 0],
[ 0]]), Matrix([
[ 1],
[ 0],
[-1],
[ 1]])]
============ 4) Left Null Space ===============
[Matrix([
[ 5],
[-2],
[ 1]])]
"""