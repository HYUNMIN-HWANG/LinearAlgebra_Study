# Vector Projection

import numpy as np

# [1] Projection of a Vector on another vector
u = np.array([1, 2, 3])   # vector u
v = np.array([5, 6, 2])   # vector v
  
# Task: Project vector u on vector v
  
# finding norm of the vector v
v_norm = np.sqrt(sum(v**2))    
  
# Apply the formula as mentioned above
# for projecting a vector onto another vector
# find dot product using np.dot()
proj_of_u_on_v = (np.dot(u, v)/v_norm**2)*v
  
print("Projection of Vector u on Vector v is: ", proj_of_u_on_v)
# Projection of Vector u on Vector v is:  [1.76923077 2.12307692 0.70769231]

################################################################

# [2] Projection of a Vector onto a Plane
# vector u 
u = np.array([2, 5, 8])       
  
# vector n: n is orthogonal vector to Plane P
n = np.array([1, 1, 7])       
   
# Task: Project vector u on Plane P
  
# finding norm of the vector n 
n_norm = np.sqrt(sum(n**2))    
   
# Apply the formula as mentioned above
# for projecting a vector onto the orthogonal vector n
# find dot product using np.dot()
proj_of_u_on_n = (np.dot(u, n)/n_norm**2)*n
  
# subtract proj_of_u_on_n from u: 
# this is the projection of u on Plane P
print("Projection of Vector u on Plane P is: ", u - proj_of_u_on_n)
# Projection of Vector u on Plane P is:  [ 0.76470588  3.76470588 -0.64705882]

