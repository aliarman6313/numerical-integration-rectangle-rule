# integration1.py
import numpy as np
import matplotlib.pyplot as plt

# تابعی که می‌خواهیم انتگرال بگیریم
def f(x):
    return np.sin(x)

# تابعی برای انتگرال‌گیری عددی به روش مستطیلی (Left Riemann)
def rectangular_integral(f, a, b, N):
    x = np.linspace(a, b, N + 1)
    dx = (b - a) / N
    y = f(x[:-1])  # مقدار تابع در سمت چپ هر بازه
    return np.sum(y * dx)

# مقدار دقیق انتگرال برای sin(x) در بازه [0, pi] برابر است با 2
a, b = 0, np.pi
exact = 2
Ns = np.array([10, 50, 100, 200, 500, 1000])
errors = []

for N in Ns:
    integral = rectangular_integral(f, a, b, N)
    err = abs(integral - exact)
    errors.append(err)
    print(f"N = {N:<5} Integral ≈ {integral:.8f}, Error = {err:.2e}")

# نمودار خطای نسبی برحسب N
plt.figure(figsize=(8, 5))
plt.plot(Ns, errors, 'o-', label="Rectangular Error")
plt.xlabel("N (number of intervals)")
plt.ylabel("Absolute Error")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.title("Error vs N in Rectangular Integration")
plt.legend()
plt.tight_layout()
plt.show()