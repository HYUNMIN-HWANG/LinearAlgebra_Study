'''행렬식'''
# determinant(det) = 0이면 역행렬이 존재하지 않는다.
# det != 0 이면 역행렬이 존재한다.

import numpy as np
d = np.array([[1,2],[3,4]])
print(np.linalg.det(d))
# -2.0000000000000004
# 0이 아니기 때문에 역행렬이 존재한다.


'''역행렬'''
import numpy as np
from numpy.linalg import inv

a = np.array([[1,2],[3,4]])
print(a)
# [[1 2]
#  [3 4]]

ainv = inv(a)
print(ainv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

ainv2 = inv(np.matrix(a))
print(ainv2)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

'''A*A^-1 = I'''
# 원래의 행렬 x 역행렬 = 단위행렬
print(a.dot(ainv))
# [[1.00000000e+00 1.11022302e-16]
#  [0.00000000e+00 1.00000000e+00]]
