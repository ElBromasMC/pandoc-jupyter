import numpy as np
from numpy.polynomial import Polynomial
from .interpolation import lagrange

# X: Lista de los nodos de la interpolación
# Y: Lista de los valores de la interpolación
# DY: Lista de las derivadas de la interpolación
# return:
#   itr: El polinomio de interpolación
#   H, DH: Listas que contienen los polinomios base
def hermite(X, Y, DY):
    n = len(X)
    _, L = lagrange(X, Y)
    DL = [p.deriv() for p in L]
    H = []
    S1 = Polynomial(0)
    for i in range(n):
        r = (Polynomial(1)-2*Polynomial([-X[i],1])*DL[i](X[i]))*L[i]**2
        S1 += Y[i]*r
        H.append(r)

    DH = []
    S2 = Polynomial(0)
    for i in range(n):
        r = Polynomial([-X[i],1])*L[i]**2
        S2 += DY[i]*r
        DH.append(r)
    itr = S1 + S2
    return itr, H, DH

# X: Lista de los nodos de la interpolación
# Y: Lista de los valores de la interpolación
# DY: Lista de las derivadas de la interpolación
# return:
#   itr: El polinomio de interpolación
#   H: La tabla de diferencias divididas
def hermite_table(X, Y, DY):
    n = len(X)
    # Rellenamos el array de los z_i
    Z = np.zeros(2*n)
    for i in range(n):
        Z[2*i:2*i+2] = [X[i], X[i]]
    # Creamos la tabla de diferencias divididas
    H = np.zeros((2*n, 2*n))
    # Rellenamos con los valores
    for i in range(n):
        H[0, 2*i:2*i+2] = [Y[i], Y[i]]
    # Rellenamos con las derivadas
    for i in range(n):
        H[1, 2*i] = DY[i]
    # Rellenamos con las diferencias divididas
    for i in range(1, 2*n):
        for j in range(2*n-i):
            if i == 1 and j % 2 == 0:
                continue
            top = H[i-1,j] - H[i-1,j+1]
            bottom = Z[j] - Z[j+i]
            H[i,j] = top/bottom
    # Calculamos los polinomios base
    itr = Polynomial(0)
    for i in range(2*n):
        base = Polynomial([1])
        for j in range(i):
            factor = Polynomial([-Z[j], 1])
            base = base * factor
        itr += H[i,0] * base
    
    return itr, H
