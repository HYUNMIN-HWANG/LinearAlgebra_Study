# Integration

import numpy as np
import sympy as sp
import scipy.integrate as integrate

'''integrate.quad()'''
x2 = lambda x: x**2
x2_int = integrate.quad(x2, 0, 4)   # 0부터 4까지, x**2 적분
print(x2_int)
# (21.333333333333336, 2.368475785867001e-13)

x2_int = integrate.quad(x2, 0, np.inf)   # 0부터 무한대까지, x**2 적분
print(x2_int)
# (-0.33271664651150246, 0.00040260851867113256)

