import numpy as np
from .compose import trapezium_method

def romberg_trapezium(f, a, b, n):
    R = np.zeros((n, n))
    for i in range(n):
        R[0][i] = trapezium_method(f, a, b, 2**i)
    for i in range(1, n):
        for j in range(n-i):
            top = 4**i*R[i-1][j+1]-R[i-1][j]
            bottom = 4**i - 1
            R[i][j] = top/bottom    
    return R
