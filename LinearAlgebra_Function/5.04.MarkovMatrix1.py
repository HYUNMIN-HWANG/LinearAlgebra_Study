# Markov matrix
# state of probability

#the following code takes a list such as
#[1,1,2,6,8,5,5,7,8,8,1,1,4,5,5,0,0,0,1,1,4,4,5,1,3,3,4,5,4,1,1]
#with states labeled as successive integers starting with 0
#and returns a transition matrix, M,
#where M[i][j] is the probability of transitioning from i to j

import numpy as np

def transition_matrix(transitions):
    n = 1+ max(transitions) #number of states
    print("n : ", n)    # n :  9 총 9개의 상태가 있음

    M = [[0]*n for _ in range(n)]   # n * n zero matrix

    for (i,j) in zip(transitions,transitions[1:]):
        M[i][j] += 1
    print(np.array(M),"\n")
    # [[2 1 0 0 0 0 0 0 0]
    #  [0 4 1 1 2 0 0 0 0]
    #  [0 0 0 0 0 0 1 0 0]
    #  [0 0 0 1 1 0 0 0 0]
    #  [0 1 0 0 1 3 0 0 0]
    #  [1 1 0 0 1 2 0 1 0]
    #  [0 0 0 0 0 0 0 0 1]
    #  [0 0 0 0 0 0 0 0 1]
    #  [0 1 0 0 0 1 0 0 1]]

    #now convert to probabilities:
    for row in M:
        s = sum(row)
        if s > 0:
            row[:] = [f/s for f in row]
    print(np.array(M), "\n")
    # [[0.66666667 0.33333333 0.         0.         0.         0.       0.         0.         0.        ]
    # [0.         0.5        0.125      0.125      0.25       0.        0.         0.         0.        ]
    # [0.         0.         0.         0.         0.         0.        1.         0.         0.        ]
    # [0.         0.         0.         0.5        0.5        0.        0.         0.         0.        ]
    # [0.         0.2        0.         0.         0.2        0.6       0.         0.         0.        ]
    # [0.16666667 0.16666667 0.         0.         0.16666667 0.33333333  0.         0.16666667 0.        ]
    # [0.         0.         0.         0.         0.         0.        0.         0.         1.        ]
    # [0.         0.         0.         0.         0.         0.        0.         0.         1.        ]
    # [0.         0.33333333 0.         0.         0.         0.33333333  0.         0.         0.33333333]]
    return M

#test:

t = [1,1,2,6,8,5,5,7,8,8,1,1,4,5,5,0,0,0,1,1,4,4,5,1,3,3,4,5,4,1,1]
print(np.array(t))
print("================")
m = transition_matrix(t)
for row in m: print(' '.join('{0:.2f}'.format(x) for x in row))

# 0.67 0.33 0.00 0.00 0.00 0.00 0.00 0.00 0.00
# 0.00 0.50 0.12 0.12 0.25 0.00 0.00 0.00 0.00
# 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.00 0.00
# 0.00 0.00 0.00 0.50 0.50 0.00 0.00 0.00 0.00
# 0.00 0.20 0.00 0.00 0.20 0.60 0.00 0.00 0.00
# 0.17 0.17 0.00 0.00 0.17 0.33 0.00 0.17 0.00
# 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00
# 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00
# 0.00 0.33 0.00 0.00 0.00 0.33 0.00 0.00 0.33
