import numpy as np

# f: Funcion a integrar representada por una funcion lambda
# a: Cota inferior
# b: Cota superior
# n: Numero de raices a utilizar
# return:
#   integral: Aproximacion de la integral de f en [a,b]
def legendre_method(f, a, b, n):
    R, W = np.polynomial.legendre.leggauss(n)
    # Normalizamos el intervalo de integracion a [-1, 1]
    g = lambda t : f(((b-a)*t+(b+a))/2)*(b-a)/2
    integral = 0
    for i in range(n):
        integral += W[i]*g(R[i])
    return integral
