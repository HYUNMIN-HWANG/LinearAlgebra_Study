# 벡터의 크기

import numpy as np

# 2d
a = np.array([1,2])
print(a)
# [[1 2]]

a_len = np.linalg.norm(a)
print(a_len)
# 2.23606797749979
l1 = np.linalg.norm(a, ord=1) # L1 Norm 구하기
print(l1)   
# 3.0
l2 = np.linalg.norm(a, ord=2) # L2 Norm 구하기
print(l2)
# 2.23606797749979

# 3d
b = np.array([3, -15, 8])
print(b)
# [[  3 -15   8]]
print(np.linalg.norm(b))
# 17.26267650163207
print(np.linalg.norm(b, ord=1))
# 26.0
print(np.linalg.norm(b, ord=2))
# 17.26267650163207