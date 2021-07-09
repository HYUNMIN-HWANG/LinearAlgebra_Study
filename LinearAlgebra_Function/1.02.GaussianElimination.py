# 가우스 소거법
# 연립 방정식을 풀기 위해 고안된 방법
# Forward Elimination -> Backward Elimination

import sys
import numpy as np

'''Gaussian Elimination'''

def GE(A,x):
    n = len(A)
    print("n : ", n)    # 3

    # Forward Elimination
    # 입력받은 행렬 A의 크기만큼 loop을 돌면서
    for i in range(n):
        # A[i][i]가 0.0 같게 되면 가우스 소거법이 불가능한 행렬, division error 수행
        if A[i][i] == 0.0:
            sys.exit("Divide by zero detected!")
        # i+1열의 A에 대해 i행과 j행의 비율을 구해 준 후, 그 ration만큼 j-i*ratio 해준다.
        # 결과는 a[i][i] 좌측의 행 전부 0이 됨
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
            for k in range(n+1):
                A[j][k] -= ratio * A[i][k]
    
    # Backward Elimination
    # A를 구해주고, 맨 끝 X[n-1] == A[n-1][n] / A[n-1][n-1] 취해준다.
    x[n-1] = A[n-1][n] / A[n-1][n-1]
    for i in range(n-2, -1, -1) :
        # x[i]를 구하기 위해 back substitution 시행
        x[i] = A[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j]*x[j]
        x[i] = x[i]/A[i][i]
    
    return [A,x]

'''result'''
# 실행 결과
a = [[1,1,1,9],[2,-3,4,13],[3,4,5,40]]

a = np.array(a)
a = a.astype(float)
print(a)
# [[ 1.  1.  1.  9.]
#  [ 2. -3.  4. 13.]
#  [ 3.  4.  5. 40.]]

x = np.zeros(len(a))
print(x)    # [0. 0. 0.]

a, b = GE(a,x)
print(a)
print(b)

# [[ 1.   1.   1.   9. ] 
#  [ 0.  -5.   2.  -5. ] 
#  [ 0.   0.   2.4 12. ]]
# [1. 3. 5.]