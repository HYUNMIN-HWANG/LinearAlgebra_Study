# Rank
# pivot의 개수를 구할 수 있다.

import numpy as np

x1 = np.array([[2,4],[3,6]])
print(x1)
print(np.linalg.matrix_rank(x1))    # 1

x2 = np.array([[2,7],[5,1]])
print(np.linalg.matrix_rank(x2))    # 2

x3 = np.array([[1,3,3,2],[2,6,9,7],[-1,-3,3,4]])
print(np.linalg.matrix_rank(x3))    # 2
