# Dimension

import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
# [[1 2 3 4]
#  [5 6 7 8]]
print(a.shape)  # (2, 4)
print(len(a.shape)) # 2
print(a.ndim)   # 2


b = np.array([[1,0,0],[0,0,0]])
print(b)
# [[1 0 0]
#  [0 0 0]]
print(b.shape)  # (2, 3)
print(len(b.shape)) # 2
print(b.ndim)   # 2

bT = b.T
print(bT)
# [[1 0]
#  [0 0]
#  [0 0]]
print(bT.shape) # (3, 2)
print(len(bT.shape)) # 2
print(bT.ndim)  # 2

c = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(c)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
print(c.shape)  # (3, 3)
print(len(c.shape)) # 2
print(c.ndim)   # 2

x = np.array([[[0,1,1],[1,1,1],[3,3,3]]])
print(x)
# [[[0 1 1]
#   [1 1 1]
#   [3 3 3]]]
print(x.shape)  # (1, 3, 3)
print(len(x.shape)) # 3
print(x.ndim)   # 3
