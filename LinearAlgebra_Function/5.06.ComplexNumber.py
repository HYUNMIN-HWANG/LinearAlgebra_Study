# 복소수와 켤레복소수
# 복소수 : a + b * j
    # a : real part
    # b : imaginary part
    # j**2 = -1
# 켤레복소수 : a + b*j, a - b*j


# 복소수 : a + b * j
a = 1 + 3j

print(a.real)   # 1.0
print(a.imag)   # 3.0


# 켤레복소수 : a + b*j, a - b*j
print(a.conjugate())    # (1-3j)

# 복소수의 절댓값 : root(a**2 + b**2)
print(abs(a))   # 3.1622776601683795


# complex number
real = 5
imag = -2
c = complex(real,imag)
print(c, c.real, c.imag)    # (5-2j) 5.0 -2.0