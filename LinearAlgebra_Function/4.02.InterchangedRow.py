# Interchanged Row

import numpy as np

a = np.array([[4,3,1], [5,7,0], [9,9,3], [8,2,4]])
print(a) 
# [[4 3 1]
#  [5 7 0]
#  [9 9 3]
#  [8 2 4]]

# 0 row <-> 2 row
a[[0, 2]] = a[[2, 0]]
print(a)
# [[9 9 3]
#  [5 7 0]
#  [4 3 1]
#  [8 2 4]]

# 0 column <-> 1 column
a[:,[0, 1]] = a[:,[1, 0]]
print(a)
# [[9 9 3]
#  [7 5 0]
#  [3 4 1]
#  [2 8 4]]
