# Jacobian matrix
# m차원에서 n차원으로 가는 함수 f가 있다고 할 때 각각의 차원에 대해 모든 편미분 값을 모아놓은 matrix

import autograd.numpy as np
from autograd import grad, jacobian

x = np.array([5,3], dtype=float)

def cost(x):
    return x[0]**2 / x[1] - np.log(x[1])

gradient_cost = grad(cost)
jacobian_cost = jacobian(cost)

print(gradient_cost(x))
print('==================')
print(jacobian_cost(np.array([x,x,x])))

# [ 3.33333333 -3.11111111]
# ==================
# [[[ 2.          0.        ]
#   [-1.2         0.        ]
#   [ 0.          0.        ]]

#  [[ 0.          2.        ]
#   [ 0.         -1.33333333]
#   [ 0.          0.        ]]]
