# Least Squares
# 해방정식을 근사적으로 구하는 방법 : 구하려는 해와 실제 해의 오차의 제곱의 합이 최소가 되는 해를 구하는 방법

# 샘플 데이터
import numpy as np
import matplotlib.pyplot as plt

def make_linear(w=0.5, b=0.8, size=50, noise=1.0):
    # w : 기울기, b : y 절편

    x = np.arange(size)
    y = w * x + b
    noise = np.random.uniform(-abs(noise), abs(noise), size=y.shape)    # 노이즈 생성
    yy = y + noise  # 노이즈 추가

    # 시각화
    plt.figure(figsize=(10, 7))
    plt.plot(x, y, color='r', label=f'y = {w}*x + {b}')
    plt.scatter(x, yy, label='data')
    plt.legend(fontsize=20)
    plt.show()
    print(f'w: {w}, b: {b}')
    return x, yy

def least_square(x, y) :
    # Least Square 공식으로 w와 b 구하기

    x_bar = x.mean()
    y_bar = y.mean()

    # w 계수
    calculated_weight = ((x - x_bar) * (y - y_bar)).sum() / ((x - x_bar)**2).sum()
    print('w: {:.2f}'.format(calculated_weight))

    # b
    calculated_bias = y_bar - calculated_weight * x_bar
    print('b: {:.2f}'.format(calculated_bias))

x, y = make_linear(size=50, w=1.5, b=0.8, noise=5.5)
least_square(x, y)
# w: 1.5, b: 0.8
# w: 1.49
# b: 0.82

# 노이즈 더 추가
print("========Add noise=========")
y[5]=60
y[10]=60
y[15]=60
least_square(x, y)
# w: 1.30
# b: 7.92
# outlier에 취약하다.
