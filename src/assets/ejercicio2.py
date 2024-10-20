import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definimos nuestra función
def right_side(y, t):
    """
    t: La variable independiente
    y: La variable dependiente
    return:
    dydt: La derivada de y evaluada en t
    """
    dydt = (-y + 2*np.heaviside(t - 10, 1))/20
    return dydt

# Nuestra condición inicial
y0 = 1
t = np.linspace(0, 100, 1200)

# Usamos odeint para resolver la EDO numéricamente
sol = odeint(right_side, y0, t) 

# Usamos nuestra solución analítica
exact_sol = np.exp(-1/20*t) + 2*(1-np.exp(-1/20*(t-10)))*np.heaviside(t-10, 1)

# Graficamos las soluciones
fig, axs = plt.subplots(1,2)
axs[0].plot(t, sol[:, 0], 'b', label='Solución numérica')
axs[0].legend()
axs[0].set_xlabel('t')
axs[0].grid()
axs[1].plot(t, exact_sol, 'r', label='Solución analítica')
axs[1].legend()
axs[1].set_xlabel('t')
axs[1].grid()
plt.savefig('ejercicio2.png')
