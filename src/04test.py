import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from ode import taylor_method

y, t = sp.symbols("y t")
f_sym = 2*(y/t) + (t**2)*sp.exp(t)
f = sp.lambdify((y, t), f_sym, 'numpy')

y0 = [0]
k = 3
a, b = 1, 2
n = 10

# Nuestra aproximación de orden 'k'
t, y = taylor_method(k, f_sym, y0, a, b, n)

# Solución aproximada por odeint
sol = odeint(f, y0, t)

plt.scatter(t, y[:, 0], label='Método de Taylor')
plt.plot(t, sol[:, 0], label='Odeint', linestyle="--", color="red")
plt.legend()
plt.grid()
#plt.savefig('hi.png')
plt.show()
