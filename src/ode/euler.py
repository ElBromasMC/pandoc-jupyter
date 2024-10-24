import numpy as np

def euler_method(f, y0, a, b, n):
    """
    f: Función que representa la derivada de la función en un punto y momento
    concreto. Tiene de argumentos (y, t) respectivamente.
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

    # Iteramos los valores restantes
    for i in range(1, n+1):
        t_prev = t[i-1]
        y_prev = y[i-1,:]
        f_prev = np.array(f(y_prev, t_prev))
        y[i,:] = y_prev + h*f_prev

    return t, y

def heun_method(f, y0, a, b, n):
    """
    f: Función que representa la derivada de la función en un punto y momento
    concreto. Tiene de argumentos (y, t) respectivamente.
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

    # Iteramos los valores restantes
    for i in range(1, n+1):
        t_prev = t[i-1]
        t_curr = t[i]
        y_prev = y[i-1,:]
        f_prev = np.array(f(y_prev, t_prev))
        f_curr = np.array(f(y_prev + h*f_prev, t_curr))
        y[i,:] = y_prev + 1/2*h*f_prev + 1/2*h*f_curr

    return t, y

