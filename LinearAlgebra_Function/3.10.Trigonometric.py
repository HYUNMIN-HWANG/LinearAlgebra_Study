# 삼각함수 기본

import math 

a = math.pi # 원주율 파이 상수 
b = math.radians(360) # 360도를 라디안 표기법으로 
c = math.degrees(2 * math.pi) # 2파이 라디안을 degree 표기법으로 
print(f"math.pi : {a}") 
print(f"math.radians(360) : {b}") 
print(f"math.degrees(2 * math.pi) : {c}")
# math.pi : 3.141592653589793
# math.radians(360) : 6.283185307179586
# math.degrees(2 * math.pi) : 360.0

print('\n')

# sin, cos, tan
print("degree\tsin(x)\tcos(x)\ttan(x)") 
print("=" * 40) 
degrees = [0, 30, 45, 60, 90] # 0, π/6, π/4, π/3, π/2 
for val in degrees: 
    a = math.sin(math.pi * (val / 180)) 
    b = math.cos(math.pi * (val / 180)) 
    c = math.tan(math.pi * (val / 180)) 
    print(f"{val:2d}\t{a:.4f}\t{b:.4f}\t{c:.4f}") 

# degree  sin(x)  cos(x)  tan(x)
# ========================================
#  0      0.0000  1.0000  0.0000
# 30      0.5000  0.8660  0.5774
# 45      0.7071  0.7071  1.0000
# 60      0.8660  0.5000  1.7321
# 90      1.0000  0.0000  16331239353195370.0000
