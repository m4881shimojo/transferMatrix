# 機械回路多直列要素の振動フィルタ
#工学解析　page 388-395　図11.19に相当
#20261023 shimojo
#
import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定（Windows標準フォント）
#plt.rcParams['font.family'] = 'MS Gothic'
plt.rcParams['font.family'] = 'Meiryo'

# 1. グラフ描画用の高解像度 r データ (0.001刻み)
# rは角振動数を固有振動数で正規化した値
r = np.arange(0, 5.001, 0.001) #r=omega/omega_n
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

# 2. 理論的な特異点 (ピーク) の r の値を計算
# 5x = i * (2k + 1) * pi / 2  =>  theta = (2k + 1) * pi / 10
k_values = np.arange(0, 5)  # k = 0, 1, 2, 3, 4
theta_singular = (2 * k_values + 1) * np.pi / 10.0
a_singular = np.cos(theta_singular)
r_singular = np.sqrt(2.0 * (1.0 - a_singular))

# 理論値をコンソールに出力
print("理論的な特異点 (ピーク) の r の値:")
for k, r_val in zip(k_values, r_singular):
    print(f"  k = {k}: r = {r_val:.5f}")

# 3. グラフの描画
plt.figure(figsize=(10, 6))
plt.plot(r, y_5x, 'b-', linewidth=1.2, label=r'$|1 / \cosh(5x)|$')
plt.plot(r, y_1x, 'r--', linewidth=1.2, label=r'$|1 / \cosh(x)|$')

# 理論的な特異点に赤い垂線を表示
for i, r_val in enumerate(r_singular):
    plt.axvline(x=r_val, color='red', linestyle=':', alpha=0.7, 
                label='Singularities' if i == 0 else "")

#plt.xlabel('r', fontsize=12)
plt.xlabel('ω/ω_n', fontsize=12)
plt.ylabel('Gain', fontsize=12)
#plt.title(r'Singularities of $|1 / \cosh(5x)|$ and Theoretical $r$ Values', fontsize=13)
plt.title(r'入出力変位振幅比 $|1 / \cosh(5x)|$ ', fontsize=13)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.yscale('log')
plt.show()