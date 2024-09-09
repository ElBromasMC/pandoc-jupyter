import numpy as np
from numpy.polynomial import Polynomial

# x: Lista de los nodos de la interpolación
# y: Lista de los valores de la interpolación
# return:
#   itr: El polinomio de interpolación
#   L: Lista que contiene los polinomios base
def lagrange(x, y):
    n = len(x)
    # Calculamos los polinomios base
    L = []
    itr = Polynomial(0)
    for i in range(n):
        base = Polynomial([1])
        for j in range(n):
            if j != i:
                factor = Polynomial([-x[j], 1])/(x[i]-x[j])
                base = base * factor
        L.append(base)
        itr += y[i] * base
    return itr, L

# x: Lista de los nodos de la interpolación
# y: Lista de los valores de la interpolación
# return:  
#   itr: El polinomio de interpolación
#   N: Matriz que representa la tabla de diferencias divididas
def newton(x, y):
    n = len(x)
    N = np.zeros((n, n))
    # Completamos la tabla de diferencias divididas
    N[0,:] = y
    for i in range(1,n):
        for j in range(n-i):
            top = N[i-1,j] - N[i-1,j+1]
            bottom = x[j] - x[j+i]
            N[i,j] = top/bottom
    # Calculamos los polinomios base
    itr = Polynomial(0)
    for i in range(n):
        base = Polynomial([1])
        for j in range(i):
            factor = Polynomial([-x[j], 1])
            base = base * factor
        itr += N[i,0] * base
    return itr, N

def forward_differences(Y):
    n = len(Y)
    F = np.zeros((n,n))
    F[0,:] = Y
    for i in range(1,n):
        for j in range(0, n-i):
            diff = F[i-1,j+1] - F[i-1,j]
            F[i,j] = diff
    return F

def backward_differences(Y):
    n = len(Y)
    F = np.zeros((n,n))
    F[0,:] = Y
    for i in range(1,n):
        for j in range(i, n):
            diff = F[i-1,j] - F[i-1,j-1]
            F[i,j] = diff
    return F
