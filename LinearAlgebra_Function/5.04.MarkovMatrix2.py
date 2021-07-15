# Markov matrix

# all the sum stored in this 1D array is equal to 1,
# 컬럼을 다 더했을 때 1이어야 한다.

def checkMarkov(m) :
     
    # Outer loop to access rows
    # and inner to access columns
    for i in range(0, len(m)) :
         
        # Find sum of current row
        sm = 0
        for j in range(0, len(m[i])) :
            sm = sm + m[i][j]
 
        if (sm != 1) :
            return False
             
    return True
     
# Matrix to check
m = [ [ 0, 0, 1 ],
      [ 0.5, 0, 0.5 ],
      [ 1, 0, 0 ]      ]
 
# Calls the function check()
if (checkMarkov(m)) :
    print(" yes ")
else :
    print(" no ")

# yes
     
# This code is contributed by Nikita Tiwari.