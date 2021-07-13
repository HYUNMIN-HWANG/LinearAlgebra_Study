# rotation matrix

import numpy as np
import matplotlib.pyplot as plt

theta = np.radians(30)

c, s = np.cos(theta), np.sin(theta)
R = np.array(((c, -s), (s, c))) # rotation matrix
print('rotation matrix:')
print(R)
# [[ 0.8660254 -0.5      ]
#  [ 0.5        0.8660254]]

v = np.array((0,1))
print("vector v : ")
print(v)
# [0 1]

print('apply the rotation matrix r to v: r*v')
print( R.dot(v) )
# [-0.5        0.8660254]

# plot the results
plt.figure(figsize = (10,8))
plt.plot(v[0],v[1], 'bo')
plt.plot(R.dot(v)[0],R.dot(v)[1], 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.show()