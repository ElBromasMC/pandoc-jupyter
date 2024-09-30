import numpy as np

# f: Funcion a integrar representada por una funcion lambda
# a: Cota inferior
# b: Cota superior
# n: Numero de intervalos
# return:
#   integral: Aproximacion de la integral de f en [a,b]
def trapezium_method(f, a, b, n):
    if a == b:
        return 0
    if n <= 0:
        raise Exception("n debe ser positivo!")
    h = (b - a)/n
    X = np.linspace(a, b, n+1)
    Y = f(X)
    sum = Y[0] + Y[-1]
    for i in range(1,n):
        sum += 2*Y[i]
    integral = (h/2)*sum
    return integral

def simpson_method(f, a, b, n):
    if a == b:
        return 0
    if n % 2 != 0 or n <= 0:
        raise Exception("n debe ser par y positivo!")
    h = (b - a)/n
    X = np.linspace(a, b, n+1)
    Y = f(X)
    sum = Y[0] + Y[-1]
    for i in range(2,n,2):
        sum += 2*Y[i]
    for i in range(1,n,2):
        sum += 4*Y[i]
    integral = (h/3)*sum
    return integral

def simpson_3_8_method(f, a, b, n):
    if a == b:
        return 0
    if n % 3 != 0 or n <= 0:
        raise Exception(f"n debe ser multiplo de 3 y positivo!")
    h = (b - a)/n
    X = np.linspace(a, b, n+1)
    Y = f(X)
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
def combined_method(f, a, b, n):
    h = (b - a)/n
    r = 3*(n % 2)
    integral = simpson_method(f, a, b - r*h, n - r) + simpson_3_8_method(f, b - r*h, b, r)
    return integral

# Realiza el metodo 3/8 de Simpson y luego el metodo 1/3 de Simpson para los intervalos restantes
def another_combined_method(f, a, b, n):
    h = (b - a)/n
    res = n % 3
    r = 7*res - 3*res**2
    integral = simpson_3_8_method(f, a, b - r*h, n - r) + simpson_method(f, b - r*h, b, r)
    return integral

