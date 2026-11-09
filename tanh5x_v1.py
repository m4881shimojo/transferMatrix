# 機械回路多直列要素の振動フィルタ
#工学解析　page 388-395　図11.19に相当
#20261023 shimojo
import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Meiryo'

# 1. グラフ描画用の高解像度 r データ (0.001刻み)
r = np.arange(0, 5.001, 0.001)
a = 1.0 - 0.5 * r**2  #cosh(x) = a
x = np.arccos(a.astype(complex)) * 1j  #cosh(x) = a
"""
「実数配列 a を複素数型にキャスト（変換）した上で、逆余弦関数（arccos）を定義域の制限なく計算する」
cosh(x) = a の解が x = i arccos(a)と表せる数学的な理由は、
双曲線関数（cosh）と三角関数（cos）を複素数上で結びつける関係式に由来します。
任意の複素数 x に対して次の基本関係式が成立します。cosh(ix) = cos(x) 
"""

y_5x = np.abs(1.0 / np.cosh(5.0 * x))
y_1x = np.abs(1.0 / np.cosh(x))

# Impedanceの計算　Z
# .astype(complex) を使用して、sqrtの中身が負になっても複素数として計算できるように修正
yy_5x = np.abs(np.sqrt((1.0 - y_5x**2).astype(complex)) / np.sqrt((r**2 - 0.25).astype(complex)))
yy_1x = np.abs(np.sqrt((1.0 - y_1x**2).astype(complex)) / np.sqrt((r**2 - 0.25).astype(complex)))

# 2. グラフの描画
plt.figure(figsize=(10, 6))
plt.plot(r, yy_5x, 'b-', linewidth=1.2, label=r'$Z_{5x}$')
plt.plot(r, yy_1x, 'r--', linewidth=1.2, label=r'$Z_{1x}$')

plt.xlabel(r'$\omega / \omega_n$', fontsize=12)
plt.ylabel('Impedance', fontsize=12)
plt.title('入出力端動インピーダンス', fontsize=13)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)

# 縦軸の極端なピークで見づらくなるのを防ぐために表示範囲を設定
#plt.ylim(0, 10)
plt.yscale('log')

plt.show()