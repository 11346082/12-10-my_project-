print("Hello yoyoyo")

import numpy as np
import matplotlib.pyplot as plt

# 定義愛心形狀的參數方程
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# 繪製愛心
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')
plt.title('Heart Shape', fontsize=16)
plt.axis('off')  # 關閉座標軸
plt.show()
