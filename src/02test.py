import numpy as np
import scipy.integrate as integrate
from integration import legendre_double_method

# Datos
f = lambda x, y : np.cos(x)**2 + y**2
a, b = 0, 1
c = lambda x: 0
d = lambda x: x

# Desarrollo
integral, error = integrate.dblquad(lambda y, x: f(x,y), a, b, c, d)

# Testeamos la funcion
for i in range(2, 10):
    print(f"Legendre para n={i}:", legendre_double_method(f, a, b, i, c, d, i) - integral)
