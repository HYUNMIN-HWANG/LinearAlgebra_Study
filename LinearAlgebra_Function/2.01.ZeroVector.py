# zero vector νννκΈ°

'''numpy.zeros'''
import numpy as np

print(np.zeros(5))
# [0. 0. 0. 0. 0.]
print(np.zeros((5,), dtype=int))
# [0 0 0 0 0]

print(np.zeros((2,1)))
# [[0.]
#  [0.]]

s = (2,2)
print(np.zeros(s))
# [[0. 0.]
#  [0. 0.]]