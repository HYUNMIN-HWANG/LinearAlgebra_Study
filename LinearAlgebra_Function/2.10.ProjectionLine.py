# line 밖에 있는 점에서 line에 수직선을 그었을 때, line에 만나는 점

import numpy as np
import matplotlib.pyplot as plt

def point_on_line(a, b, p):
    ap = p - a
    ab = b - a
    print(ap)
    print(ab)
    print("np.dot(ap, ab) : ", np.dot(ap, ab))  # 점A와 점P의 거리
    print("np.dot(ab, ab) : ", np.dot(ab, ab))  # 점A와 점B의 거리
    print(np.dot(ap, ab) / np.dot(ab, ab) * ab)
    result = a + np.dot(ap, ab) / np.dot(ab, ab) * ab
    return result

A = np.array([2, 0])    # line 위의 점
B = np.array([4, 4])    # line 위의 점
P = np.array([1, 3])    # line 밖의 점
projected = point_on_line(A, B, P)
print(projected)

plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.axis('equal')

x_values = [A[0], B[0]]
y_values = [A[1], B[1]]

plt.plot(B[0], B[1], 'ro')
plt.plot(A[0], A[1], 'ro')
plt.plot(P[0], P[1], 'ro')
plt.plot(x_values, y_values, 'b-')
plt.plot(projected[0], projected[1], 'rx')

plt.show()