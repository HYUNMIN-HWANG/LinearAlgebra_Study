# gram_schmidt orthogonalization
# 직교하는 vector를 구한다.

import numpy as np

def gram_schmidt(X):
    """
    Implements Gram-Schmidt orthogonalization.

    Parameters
    ----------
    X : an n x k array with linearly independent columns

    Returns
    -------
    U : an n x k array with orthonormal columns

    """

    # Set up
    n, k = X.shape
    U = np.empty((n, k))
    I = np.eye(n)           # identity matrix

    # The first col of U is just the normalized first col of X
    v1 = X[:,0]
    U[:, 0] = v1 / np.sqrt(np.sum(v1 * v1))

    for i in range(1, k):
        # Set up
        b = X[:, i]       # The vector we're going to project
        Z = X[:, 0:i]     # First i-1 columns of X

        # Project onto the orthogonal complement of the col span of Z
        M = I - Z @ np.linalg.inv(Z.T @ Z) @ Z.T
        u = M @ b

        # Normalize
        U[:, i] = u / np.sqrt(np.sum(u * u))

    return U

y = [1, 3, -3]

X = [[1,  0],
     [0, -6],
     [2,  2]]

X, y = [np.asarray(z) for z in (X, y)]
print(X)
print(y)

# p = P*b = X (X^T * X)^-1 * X^T * y 
Py1 = X @ np.linalg.inv(X.T @ X) @ X.T @ y
print(Py1)
# [-0.56521739  3.26086957 -2.2173913 ]

U = gram_schmidt(X)
print(U)
# [[ 0.4472136  -0.13187609]
#  [ 0.         -0.98907071]
#  [ 0.89442719  0.06593805]]

Py2 = U @ U.T @ y
print(Py2)
# [-0.56521739  3.26086957 -2.2173913 ]
# Py1과 same!
