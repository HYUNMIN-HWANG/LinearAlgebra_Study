# 대각행렬
# Diagonal Matrix

import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(np.diag(x))
# [1 5 9]
print(np.diag(x, k=1))
# [2 6]
print(np.diag(x, k=-1))
# [4 8]

print("---------------")
# 대각 행렬이외의 공간은 0인 행렬을 만들자.

a = np.zeros(x.shape, int)
print(a)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

np.fill_diagonal(a, np.diag(x))
print(a)
# [[1 0 0]
#  [0 5 0]
#  [0 0 9]]