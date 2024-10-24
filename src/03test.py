import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from ode import *

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
a, b = 0, 100
k1, k2 = 0.1, 0.8
t = np.linspace(a, b, 301)

# Usamos odeint para resolver la EDO numéricamente
sol = odeint(right_side, y0, t, args=(k1,k2)) 

# Usamos nuestra función para resolver la EDO
t_heun, sol_heun = heun_method(lambda y, t : right_side(y,t,k1,k2), y0, 0, 100, 300)
t_runge, sol_runge = runge_kutta_method(lambda y, t : right_side(y,t,k1,k2), y0, 0, 100, 300)

# Graficamos las soluciones
fig, axs = plt.subplots(2,2)
axs[0,0].plot(t_heun, sol_heun[:, 0], 'b', label='x1')
axs[0,0].plot(t_heun, sol_heun[:, 1], 'r', label='x2')
axs[0,0].legend()
axs[0,0].set_xlabel('t')
axs[0,0].grid()
axs[0,0].set_title('Heun')
axs[1,0].plot(t_heun, abs(sol[:, 0] - sol_heun[:, 0]), 'b', label='x1')
axs[1,0].plot(t_heun, abs(sol[:, 1] - sol_heun[:, 1]), 'r', label='x2')
axs[1,0].legend()
axs[1,0].set_xlabel('t')
axs[1,0].grid()
axs[0,1].plot(t_runge, sol_runge[:, 0], 'b', label='x1')
axs[0,1].plot(t_runge, sol_runge[:, 1], 'r', label='x2')
axs[0,1].legend()
axs[0,1].set_xlabel('t')
axs[0,1].grid()
axs[0,1].set_title('Runge-Kutta')
axs[1,1].plot(t_runge, abs(sol[:, 0] - sol_runge[:, 0]), 'b', label='x1')
axs[1,1].plot(t_runge, abs(sol[:, 1] - sol_runge[:, 1]), 'r', label='x2')
axs[1,1].legend()
axs[1,1].set_xlabel('t')
axs[1,1].grid()
plt.savefig('out.png')

