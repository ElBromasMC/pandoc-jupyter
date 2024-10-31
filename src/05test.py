import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from ode import general_runge_kutta_method, runge_fourth_order

def right_side(arg, t):
    x, y = arg
    dxdy = [-y + t, x - t]
    return dxdy

y0 = [-3, 5]
a, b = 0, 10
n = 25

t, y = general_runge_kutta_method(runge_fourth_order, right_side, y0, a, b, n)

# Odeint
sol = odeint(right_side, y0, t)

plt.scatter(t, y[:, 0], label='Método de Runge')
plt.plot(t, sol[:, 0], label='Odeint', linestyle="--", color="red")
plt.legend()
plt.grid()
plt.savefig('hi.png')
# plt.show()
