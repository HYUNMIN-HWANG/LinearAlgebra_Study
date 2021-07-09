# 선형 연립방정식 풀기
import numpy as np

'''np.linalg.solve'''
# 2-D
A = np.array([[1,2],[4,5]])
B = np.array([3,6])
C = np.linalg.solve(A,B)
# A * [x y] = B
print(C) # [-1.  2.]

# 3-D
A = np.array([[2,1,1],[4,-6,0],[-2,7,2]])
B = np.array([5,-2,9])
C = np.linalg.solve(A,B)
# A * [x y] = B
print(C) # [1. 1. 2.]


'''np.linalg.inv (역행렬 활용)'''
# 2-D
A = np.array([[1,2],[4,5]])
B = np.array([3,6])
C = np.linalg.inv(A)    # A의 역행렬
D = np.dot(C,B)
# [x y] = A^-1 * B
print(D)    # [-1.  2.]

# 3-D
A = np.array([[2,1,1],[4,-6,0],[-2,7,2]])
B = np.array([5,-2,9])
C = np.linalg.inv(A)
D = np.dot(C,B)
# [x y] = A^-1 * B
print(D)    # [1. 1. 2.]
