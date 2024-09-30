import numpy as np

# X: Conjunto de puntos igualmente espaciados
# Y: Imagenes de dicho conjunto
# return:
#   integral: Aproximacion de la integral de f en X
def mod_trapezium_method(X, Y):
    a = min(X)
    b = max(X)
    n = len(X) - 1
    if n <= 0:
        raise Exception("n debe ser positivo!")
    h = (b - a)/n
    sum = Y[0] + Y[-1]
    for i in range(1,n):
        sum += 2*Y[i]
    integral = (h/2)*sum
    return integral

def mod_simpson_method(X, Y):
    a = min(X)
    b = max(X)
    n = len(X) - 1
    if n % 2 != 0 or n <= 0:
        raise Exception("n debe ser par y positivo!")
    h = (b - a)/n
    sum = Y[0] + Y[-1]
    for i in range(2,n,2):
        sum += 2*Y[i]
    for i in range(1,n,2):
        sum += 4*Y[i]
    integral = (h/3)*sum
    return integral

def mod_simpson_3_8_method(X, Y):
    a = min(X)
    b = max(X)
    n = len(X) - 1
    if n % 3 != 0 or n <= 0:
        raise Exception(f"n debe ser multiplo de 3 y positivo!")
    h = (b - a)/n
    sum = Y[0] + Y[-1]
    for i in range(1,n,3):
        sum += 3*Y[i]
    for i in range(2,n,3):
        sum += 3*Y[i]
    for i in range(3,n,3):
        sum += 2*Y[i]
    integral = (3*h/8)*sum
    return integral

# Realiza el metodo 1/3 de Simpson y luego el metodo 3/8 de Simpson para los intervalos restantes
def mod_combined_method(X, Y):
    n = len(X) - 1
    r = n % 2
    if r == 0:
        integral = mod_simpson_method(X, Y)
        return integral
    elif r == 1:
        integral = mod_simpson_method(X[:-3], Y[:-3]) + mod_simpson_3_8_method(X[-4:], Y[-4:])
        return integral
