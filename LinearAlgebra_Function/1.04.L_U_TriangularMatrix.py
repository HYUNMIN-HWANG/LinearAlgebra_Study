# Extract upper or lower triangular part of a matrix

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 대각선을 기준으로 위에만 숫자가 있는 형태 -> U
upper_tri_mat = np.triu(a, k=0)
print(upper_tri_mat)
# [[1 2 3]
#  [0 5 6]
#  [0 0 9]]

# 대각선을 기준으로 아래에만 숫자가 있는 형태 -> L
lower_tri_mat = np.tril(a, k=0)
print(lower_tri_mat)
# [[1 0 0]
#  [4 5 0]
#  [7 8 9]]
