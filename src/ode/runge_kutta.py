import numpy as np

def general_runge_kutta_method(phi, f_, y0, a, b, n):
    """
    phi: Función de incremento (una aproximación adecuada para la pendiente
    en [t_i , t_{i+1}]).
    f: Función que representa la derivada de la función en un punto y momento
    concreto. Tiene de argumentos (y, t) respectivamente.
    y0: Valor inicial de la función en 'a'.
    a, b: Intervalo de tiempo.
    n: Número de intervalos a utilizar.
    """
    # Normalizamos la entrada
    f = lambda y, t : np.array(f_(y, t))
    y0 = np.array(y0)
    
    # Inicializamos variables y matrices
    dim = len(y0)
    h = (b - a)/n
    t = np.linspace(a, b, n+1)
    y = np.zeros((n+1, dim))

    # Valor inicial
    y[0,:] = y0

    # Iteramos los valores restantes
    for i in range(1, n+1):
        t_prev = t[i-1]
        y_prev = y[i-1,:]
        next = y_prev + phi(f, h, y_prev, t_prev)
        y[i,:] = next

    return t, y



def runge_third_order(f, h, y, t):
    k1 = h*f(y, t) 
    k2 = h*f(y + k1/2, t + h/2)
    k3 = h*f(y - k1 + 2*k2, t + h)
    res = (1/6)*(k1 + 4*k2 + k3)

    return res

def runge_fourth_order(f, h, y, t):
    k1 = h*f(y, t)
    k2 = h*f(y + k1/2, t + h/2)
    k3 = h*f(y + k2/2, t + h/2)
    k4 = h*f(y + k3, t + h)
    res = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    return res
