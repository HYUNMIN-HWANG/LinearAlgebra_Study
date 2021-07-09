# 행렬곱

import numpy as np

# 배열에서 행렬로 변환
a = np.array([[1,2],[3,4]])
print(type(a))  # <class 'numpy.ndarray'>
b = np.asmatrix(a)
print(type(b))  # <class 'numpy.matrix'>
print(b)
# [[1 2]
#  [3 4]]

# 행렬곱
# 1)
print(b*b)
# [[ 7 10]
#  [15 22]]

# 2)
print(np.matmul(b,b))
# [[ 7 10]
#  [15 22]]

# 3)
print(b@b)
# [[ 7 10]
#  [15 22]]

# 4)
print(np.dot(b,b))
# [[ 7 10]
#  [15 22]]

# 5)
print(b.dot(b))
# [[ 7 10]
#  [15 22]]