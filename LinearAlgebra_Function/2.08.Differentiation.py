# Differentiation 미분

import math
import sympy as sp
from sympy import symbols, limit, Derivative

'''sympy.diff'''
# 미분

x = sp.symbols('x') # x라는 변수가 기호라는 것을 알려준다.
y =  3 * (x**2) - 4 * x + 1
yp = sp.diff(y)
print(yp)   # 6*x - 4
print("==============================")

'''Limit()'''
# 두 점의 기울기를 구해서 미분을 구함

x, a, h = symbols('x, a, h')

fx = 3 * (x**2) - 4 * x + 1 # 함수 f(x) 정의
fxa = fx.subs({x:a})    # f(x)에 x = a 대입
fxh = fx.subs({x:a+h})    # f(x)에 x = a+h 대입

result = limit( (fxh-fxa)/h,h,0 ).doit()    # 극한값(미분계수) 계산
result = limit( (fxh-fxa)/h,h,0 )    # 위와 동일한 결과 나옴

print(fx)   # 3*x**2 - 4*x + 1
print(fxa)  # 3*a**2 - 4*a + 1
print(fxh)  # -4*a - 4*h + 3*(a + h)**2 + 1

print("미분 결과 : \n", result) #  6*a - 4
print("==============================")

'''Derivative()'''
# 도함수를 구해서 미분함

x = symbols('x')
fx = 3 * (x**2) - 4 * x + 1
fprime = Derivative(fx,x).doit()    
print("fx의 도함수는 : ", fprime)
# fx의 도함수는 :  6*x - 4
n = fprime.subs({x:3})
print("fx에서 x=3에서의 순간변화율(미분계수는) : ", n)
# fx에서 x=3에서의 순간변화율(미분계수는) :  14

