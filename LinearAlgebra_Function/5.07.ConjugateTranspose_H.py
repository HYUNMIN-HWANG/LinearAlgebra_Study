# conjugate transpose : 켤레복소수를 구한 후, 행과 열 바꾸기
# Hermite (H)

'''numpy.matrix.H'''
import numpy as np

x = np.matrix(np.arange(12).reshape((3,4)))
print(x)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

z = x - 1j*x
print(z)
# [[ 0. +0.j  1. -1.j  2. -2.j  3. -3.j]
#  [ 4. -4.j  5. -5.j  6. -6.j  7. -7.j]
#  [ 8. -8.j  9. -9.j 10.-10.j 11.-11.j]]

z_H = z.getH()
print(z_H)
# [[ 0. -0.j  4. +4.j  8. +8.j]
#  [ 1. +1.j  5. +5.j  9. +9.j]
#  [ 2. +2.j  6. +6.j 10.+10.j]
#  [ 3. +3.j  7. +7.j 11.+11.j]]
