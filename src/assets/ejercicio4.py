import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definimos nuestra función
def right_side(y, t, k1, k2):
    """
    t: La variable independiente
    y: La variable dependiente
    return:
    dydt: La derivada de y evaluada en t
    """
    dydt = [y[1], -k1*y[1] - k2*np.sin(y[0])]
    return dydt

# Nuestra condición inicial
y0 = [0.1, 0.6]
k1, k2 = 0.1, 0.8
t = np.linspace(0, 100, 300)

# Usamos odeint para resolver la EDO numéricamente
sol = odeint(right_side, y0, t, args=(k1,k2)) 

# Graficamos las soluciones
plt.plot(t, sol[:, 0], 'b', label='x1')
plt.plot(t, sol[:, 1], 'r', label='x2')
plt.title('Solución numérica')
plt.legend()
plt.xlabel('t')
plt.grid()
plt.savefig('ejercicio4.png')

