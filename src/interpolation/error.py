import numpy as np
import sympy as sp
import math

def m_error_bound(f_sym, n, a, b):
    x_sym = sp.symbols('x')

    # Calculamos la n derivada de la función
    ndf = sp.lambdify(x_sym, sp.diff(f_sym, x_sym, n), "numpy")

    I = np.linspace(a, b, 1000)
    
    # Calculamos la cota de error
    M = np.max(np.abs(ndf(I)))
    
    return M

# f_sym: Es una función simbólica de variable 'x' que representa la función a aproximar
# nodes: Lista que contiene los nodos de la interpolación
# xs: Lista de puntos donde evaluar el error
# error_bound: Lista de las cotas de error
def general_error_bound(f_sym, nodes, xs):
    n = len(nodes)
    a = min(nodes)
    b = max(nodes)

    M = m_error_bound(f_sym, n, a, b)
    error_bound = []
    for elem in xs:
        P = 1
        for i in range(n):
            P *= abs(elem - nodes[i])
        error_bound.append(P*M/math.factorial(n))
    return error_bound

# f_sym: Es una función simbólica de variable 'x' que representa la función a aproximar
# n: Es el número de nodos que se van a utilizar en la interpolación
# a, b: Intervalo de la interpolación
# error_bound: La cota del error para una interpolación con nodos igualmente espaciados
def evenly_error_bound(f_sym, n, a, b):
    M = m_error_bound(f_sym, n, a, b)
    h = (b-a)/(n-1)
    error_bound = h**n*M/(4*n)
    
    return error_bound
