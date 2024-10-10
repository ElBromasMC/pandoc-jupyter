import numpy as np
from .legendre import legendre_method

# f: Funcion de dos variables a integrar representada por una funcion lambda
# a: Cota inferior de la integral exterior
# b: Cota superior de la integral exterior
# n: Numero de raices a utilizar en la integral exterior
# c: Funcion lambda que representa la cota inferior de la integral interior
# d: Funcion lambda que representa la cota superior de la integral interior
# m: Numero de raices a utilizar en la integral interior
# return:
#   integral: Aproximacion de la integral doble de f
def legendre_double_method(f, a, b, n, c, d, m):
    # Usamos el metodo de Legendre para simplificar la integral interior
    g = lambda x : legendre_method((lambda y : f(x, y)), c(x), d(x), m)
    # Volvemos a usar el metodo de Legendre para calcular la integral exterior
    integral = legendre_method(g, a, b, n)
    return integral
