import numpy as np
import sympy as sp
from integration import legendre_method

# Datos
x = sp.symbols('x')
f_sym = sp.sin(x) + 2*sp.cos(x)
a, b = 0, 3

# Desarrollo
f = sp.lambdify(x, f_sym, 'numpy')
integral = sp.integrate(f_sym, (x, a, b)).evalf()

# Testeamos la funcion
for i in range(2, 10):
    print(f"Legendre para n={i}:", legendre_method(f, a, b, i) - integral)
