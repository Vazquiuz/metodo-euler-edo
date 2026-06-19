import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# 1. SOLUCIÓN ANALÍTICA
t_sym = sp.symbols('t')
y_sym = sp.symbols('y', cls=sp.Function)
edo = sp.Eq(y_sym(t_sym).diff(t_sym), t_sym * y_sym(t_sym))
sol_exacta = sp.dsolve(edo, y_sym(t_sym), ics={y_sym(0): 1})
y_exacta_num = sp.lambdify(t_sym, sol_exacta.rhs, 'numpy')

# 2. MÉTODO DE EULER
def f(t, y): return t * y
h = 0.2
t_euler = np.arange(0.0, 1.0 + h, h)
y_euler = np.zeros(len(t_euler))
y_euler[0] = 1.0

for i in range(len(t_euler) - 1):
    y_euler[i+1] = y_euler[i] + h * f(t_euler[i], y_euler[i])

print("--- Resultados (h = 0.2) ---")
for ti, yi in zip(t_euler, y_euler):
    print(f"t: {ti:.1f} | Euler: {yi:.5f} | Exacta: {y_exacta_num(ti):.5f}")

# 3. GRAFICACIÓN
t_fino = np.linspace(0, 1, 100)
plt.figure(figsize=(8, 5))
plt.plot(t_fino, y_exacta_num(t_fino), label='Solución Exacta', color='blue')
plt.scatter(t_euler, y_euler, color='red', label=f'Euler (h={h})')
plt.legend()
plt.grid(True)
plt.show()
