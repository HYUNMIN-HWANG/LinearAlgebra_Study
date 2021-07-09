# 전치행렬
# Transpose Matrix

import numpy as np
a = np.array([[1, 2], [3, 4],[5,6]])
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]

print(a.transpose())
# [[1 3 5]
#  [2 4 6]]

print(np.transpose(a))
# [[1 3 5]
#  [2 4 6]]

print(a.T)
# [[1 3 5]
#  [2 4 6]]