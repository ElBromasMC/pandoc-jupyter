import numpy as np

# f: Función lambda que representa la función cuya derivada se quiere aproximar
# x0: Es el punto donde se quiere evaluar la derivada
# h: Es el tamaño de la diferencia
# n: Denota que se va a aproximar hasta D_n
# return:
#   R: Tabla que contiene las aproximaciones de la derivada
def central_extrapolation(f, x0, h, n):
    d1 = lambda h : (f(x0+h)-f(x0-h))/(2*h)
    R = np.zeros((n,n))
    for i in range(n):
        R[0,i] = d1(h/(2)**i)
    
    for i in range(1, n):
        for j in range(n-i):
            R[i,j] = R[i-1,j+1] + (R[i-1,j+1]-R[i-1,j])/(4**(i)-1)
    return R
