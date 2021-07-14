# cramer's rule
#  It expresses the solution in terms of the determinants of the (square) coefficient matrix 
# and of matrices obtained from it by replacing one column by the vector of right hand sides of the equations.

# xi = det Bi / det A
# Bi : A의 i번째 컬럼과 B 컬럼을 바꾼 행렬

# a simple implementation using numpy
from numpy import linalg

# 1)
A=[[2,-1,5,1],[3,2,2,-6],[1,3,3,-1],[5,-2,-3,3]]
B=[-3,-32,-47,49]
C=[[2,-1,5,1],[3,2,2,-6],[1,3,3,-1],[5,-2,-3,3]]

# 2)
# A=[[1,1],[2,-1]]
# B=[4,-1]
# C=[[1,1],[2,-1]]

X=[]

for i in range(0,len(B)):
    for j in range(0,len(B)):
        C[j][i]=B[j]
        if i>0:
            C[j][i-1]=A[j][i-1]
    X.append(round(linalg.det(C)/linalg.det(A),1))

print('w=%s'%X[0],'x=%s'%X[1],'y=%s'%X[2],'z=%s'%X[3])
# 1) w=2.0 x=-12.0 y=-4.0 z=1.0

print('w=%s'%X[0],'x=%s'%X[1])#,'y=%s'%X[2],'z=%s'%X[3])
# 2) w=1.0 x=3.0