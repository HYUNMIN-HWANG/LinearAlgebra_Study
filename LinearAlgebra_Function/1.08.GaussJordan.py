# n x n 행렬의 역행렬을 구하는 방법
# Gauss-Jordan Method

import numpy as np
import sys

from numpy.lib.financial import rate

# A * A^-1 = I

n = int(input("Enter order of matrix : "))

# Making numpy array of n x 2n size and initializing 
# to zero for storing augmented matrix
# A와 I를 a 행렬에 한꺼번에 표시한다.
a = np.zeros((n,2*n))

# Reading matrix coefficients
# 행렬 A를 입력한다.
print("Enter Matrix Coefficients > ")
for i in range(n):
    for j in range(n):
        a[i][j] = float(input("a[" + str(i) + "] [" + str(j) + "] = "))

print("\nORIGIN MATIRX IS : ")
for i in range(n) :
    for j in range(n) :
        print(a[i][j], end='\t')
    print()
print("==========================")

# Augmenting Identity Matrix of Order n
# I 행렬을 입력한다.
for i in range(n):
    for j in range(n) :
        if i == j :
            a[i][j+n] = 1
print("A | I :\n", a)
print("==========================")

# Guass Jordan Elimination
print("Guass Jordan Elimination : ")
for i in range(n) :
    if a[i][i] == 0.0 :
        sys.exit("Divide by zero detected!")    # 대각선에 0가 있으면 안됨
    
    for j in range(n) :
        if i!=j:
            ratio = a[j][i] / a[i][i]

            for k in range(2*n):
                a[j][k] = a[j][k]-ratio*a[i][k]
        print(a,"\n")

# to make principal diagonal element to 1
# Inverse 행렬로 만들어준다.
print("Make Identity Matrix : ")
for i in range(n) :
    divisor = a[i][i]
    for j in range(2*n):
        a[i][j] = a[i][j]/divisor
    print(a,"\n")

# Result
print("==========================")
print("\nINVERSE MATRIX IS : ")
for i in range(n) :
    for j in range(n, 2*n) :
        print(a[i][j], end='\t')
    print()

"""
Enter order of matrix : 3
Enter Matrix Coefficients > 
a[0] [0] = 2
a[0] [1] = 1
a[0] [2] = 1
a[1] [0] = 4
a[1] [1] = -6
a[1] [2] = 0
a[2] [0] = -2
a[2] [1] = 7
a[2] [2] = 2

ORIGIN MATIRX IS : 
2.0     1.0     1.0
4.0     -6.0    0.0
-2.0    7.0     2.0
==========================
A | I :
 [[ 2.  1.  1.  1.  0.  0.]
 [ 4. -6.  0.  0.  1.  0.]
 [-2.  7.  2.  0.  0.  1.]]
==========================
Guass Jordan Elimination :
[[ 2.  1.  1.  1.  0.  0.]
 [ 4. -6.  0.  0.  1.  0.]
 [-2.  7.  2.  0.  0.  1.]]

[[ 2.  1.  1.  1.  0.  0.]
 [ 0. -8. -2. -2.  1.  0.]
 [-2.  7.  2.  0.  0.  1.]]

[[ 2.  1.  1.  1.  0.  0.]
 [ 0. -8. -2. -2.  1.  0.]
 [ 0.  8.  3.  1.  0.  1.]]

[[ 2.     0.     0.75   0.75   0.125  0.   ]
 [ 0.    -8.    -2.    -2.     1.     0.   ]
 [ 0.     8.     3.     1.     0.     1.   ]]

[[ 2.     0.     0.75   0.75   0.125  0.   ]
 [ 0.    -8.    -2.    -2.     1.     0.   ]
 [ 0.     8.     3.     1.     0.     1.   ]]

[[ 2.     0.     0.75   0.75   0.125  0.   ]
 [ 0.    -8.    -2.    -2.     1.     0.   ]
 [ 0.     0.     1.    -1.     1.     1.   ]]

[[ 2.     0.     0.     1.5   -0.625 -0.75 ]
 [ 0.    -8.    -2.    -2.     1.     0.   ]
 [ 0.     0.     1.    -1.     1.     1.   ]]

[[ 2.     0.     0.     1.5   -0.625 -0.75 ]
 [ 0.    -8.     0.    -4.     3.     2.   ]
 [ 0.     0.     1.    -1.     1.     1.   ]]

[[ 2.     0.     0.     1.5   -0.625 -0.75 ]
 [ 0.    -8.     0.    -4.     3.     2.   ]
 [ 0.     0.     1.    -1.     1.     1.   ]]

Make Identity Matrix :
[[ 1.      0.      0.      0.75   -0.3125 -0.375 ]
 [ 0.     -8.      0.     -4.      3.      2.    ]
 [ 0.      0.      1.     -1.      1.      1.    ]]

[[ 1.      0.      0.      0.75   -0.3125 -0.375 ]
 [-0.      1.     -0.      0.5    -0.375  -0.25  ]
 [ 0.      0.      1.     -1.      1.      1.    ]]

[[ 1.      0.      0.      0.75   -0.3125 -0.375 ]
 [-0.      1.     -0.      0.5    -0.375  -0.25  ]
 [ 0.      0.      1.     -1.      1.      1.    ]]

==========================

INVERSE MATRIX IS :
0.75    -0.3125 -0.375
0.5     -0.375  -0.25
-1.0    1.0     1.0
"""