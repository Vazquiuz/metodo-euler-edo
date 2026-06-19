# Resolución de EDO Separable: Analítico vs. Método de Euler

Se seleccionó el Problema de Valor Inicial:
$$\frac{dy}{dt} = t \cdot y, \quad \text{con } y(0) = 1$$

### 1. Solución Analítica
Separando variables e integrando:
$$y(t) = e^{\frac{t^2}{2}}$$

### 2. Solución Numérica
Se aplica el método de Euler en $t \in [0, 1]$ con pasos de $h = 0.2$:
$$y_{i+1} = y_i + h \cdot (t_i \cdot y_i)$$

## Requisitos
Librerías necesarias para correr el script de forma local:
`numpy`, `sympy`, `matplotlib`.
