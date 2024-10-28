import numpy as np
import sympy as sp
import math

def taylor_method(k, f_sym, y0, a, b, n):
    """
    k: Orden de la expansión de Taylor.
    f_sym: Función simbólica con variables 't' e 'y'
    que representa la EDO de dimensión 1.
    y0: Valor inicial de la función en 'a'.
    a, b: Intervalo de tiempo.
    n: Número de intervalos a utilizar.
    """
    # Normalizamos la entrada
    y0 = np.array(y0)
    
    # Inicializamos variables y matrices
    dim = len(y0)
    h = (b - a)/n
    t = np.linspace(a, b, n+1)
    y = np.zeros((n+1, dim))

    # Valor inicial
    y[0,:] = y0

    # Calculamos las derivadas
    derivs = get_derivs(f_sym, k)

    # Iteramos los valores restantes
    for i in range(1, n+1):
        y_prev = y[i-1,:]
        t_prev = t[i-1]
        taylor = np.copy(y_prev)
        for j in range(1, k+1):
            taylor += h**j/math.factorial(j)*derivs[j-1](y_prev, t_prev)
        y[i,:] = taylor
    
    return t, y

def get_derivs(f_sym, k):
    # Inicializamos los símbolos
    y, t = sp.symbols('y t')

    # Calculamos las derivadas de f_sym
    derivs = [f_sym]
    for _ in range(1, k):
        last = derivs[-1]
        der = sp.diff(last, t) + sp.diff(last, y)*last
        derivs.append(der)

    # Convertimos las expresiones simbólicas en funciones numpy
    derivs = [sp.lambdify((y,t), expr, 'numpy') for expr in derivs]
    
    return derivs

