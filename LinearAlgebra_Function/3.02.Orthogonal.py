# Orthogonal Vector
# A^T * B = 0

import numpy as np


# 직교하는지 아닌지 확인 :  A^T * B = 0
v1 = np.array([[1, -2, 4]])
v2 = np.array([[2,5,2]])

# v1 = np.array([[1,0]])
# v2 = np.array([[0,1]])

T_v1 = np.transpose(v1)

result = np.dot(v2, T_v1)
print("Result : ", result)
# Result :  [[0]]

# 두 벡터가 cross 하는 점
print(np.cross(v1, v2))

# 1) [[-24   6   9]]
# 2) [1]
