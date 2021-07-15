# Differential Equation
# http://allman84.blogspot.com/2018/10/sympy-1.html

from sympy import *

x, y, z, t = symbols('x y z t')
f, g, h = symbols('f, g, h', cls=Function)

# 미분 방정식 해 구하기
y = symbols('y', cls=Function)
deq = Eq( y(t).diff(t), -2*y(t) )
result = dsolve( deq, y(t) )
print(result)
# Eq(y(t), C1*exp(-2*t))

# 연립미분방정식
y1, y2 = symbols('y1 y2', cls=Function)
eq1 = Eq( y1(t).diff(t), -0.02*y1(t)+0.02*y2(t) )
eq2 = Eq( y2(t).diff(t), 0.02*y1(t)-0.02*y2(t) )
result = dsolve( [ eq1, eq2 ] )
print(result)
# [Eq(y1(t), -1.0*C1*exp(-0.04*t) + 1.0*C2), Eq(y2(t), 1.0*C1*exp(-0.04*t) + 1.0*C2)]

