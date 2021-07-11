# Spanning 
# all linear combinations of vectors {v1, v2, v3, ,,, ,vn} construct a vector space
# 벡터를 조합해서 만들 수 있는 모든 조합

# 2-D
import matplotlib.pyplot as plt

# u = [1, 3]
# v = [2, 1]

u = [2, 3]
v = [1, 1]

# Ploting a sample of the set of points in the span of u and v
for a in range(-10, 10):
    for b in range(-10, 10):
        plt.scatter(u[0] * a + v[0] * b, u[1] * a + v[1] * b, marker='.', color='blue')
    
# Defining x and y sizes
plt.xlim(-50, 50)
plt.ylim(-50, 50)

# Draw axes
plt.axvline(x=0, color='#A9A9A9')
plt.axhline(y=0, color='#A9A9A9')

plt.show()
plt.close()