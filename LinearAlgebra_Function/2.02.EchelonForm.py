# Echelon Form U

# A * x = 0 -> U * x = 0 -> R * x = 0
# Gaussian Elimination -> Echelon -> Row Reduced form

import sympy
A = sympy.Matrix([[1,3,3,2],[2,6,9,7],[-1,-3,3,4]])
print(A)
# Matrix([[1, 3, 3, 2], [2, 6, 9, 7], [-1, -3, 3, 4]])

'''sympy.rref()'''
print(A.rref())
# (Matrix([
# [1, 3, 0, -1],
# [0, 0, 1,  1],
# [0, 0, 0,  0]]), (0, 2))  <- pivot row