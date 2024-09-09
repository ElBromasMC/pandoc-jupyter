import numpy as np
from numpy.polynomial import Polynomial
from .interpolation import newton

def natural_cubic_spline(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    n = len(X)
    
    # Calculamos los a_j
    A = Y[:]

    # Calculamos los h_j
    H = X[1:] - X[:-1]
    
    # Calculamos los c_j
    M = np.zeros((n, n))
    M[0,0] = 1
    M[-1,-1] = 1
    for i in range(1, n-1):
        M[i,i-1] = H[i-1]
        M[i,i+1] = H[i]
        M[i,i] = 2*(H[i-1]+H[i])
    b = np.zeros(n)
    for i in range(1, n-1):
        b[i] = 3/H[i]*(A[i+1]-A[i]) - 3/H[i-1]*(A[i]-A[i-1])
    C = np.linalg.solve(M, b)

    # Calculamos los b_j
    B = np.zeros(n-1)
    for i in range(n-1):
        B[i] = (A[i+1]-A[i])/H[i]-(2*C[i]+C[i+1])*H[i]/3
    
    # Calculamos los d_j
    D = np.zeros(n-1)
    for i in range(n-1):
        D[i] = (C[i+1]-C[i])/(3*H[i])

    # Debemos hallar el trazador de la forma:
    # S_j(x) = a_j + b_j*(x-x_j) + c_j*(x-x_j)^2 + d_j*(x-x_j)^3
    CS = []
    for i in range(n-1):
        p = A[i] + B[i]*Polynomial([-X[i], 1]) + C[i]*Polynomial([-X[i], 1])**2 + D[i]*Polynomial([-X[i], 1])**3
        CS.append(p)
    return CS

def conditional_cubic_spline(X, Y, dfa, dfb):
    X = np.array(X)
    Y = np.array(Y)
    n = len(X)
    
    # Calculamos los a_j
    A = Y[:]

    # Calculamos los h_j
    H = X[1:] - X[:-1]
    
    # Calculamos los c_j
    M = np.zeros((n, n))
    M[0,0] = 2*H[0]
    M[0,1] = H[0]
    M[-1,-1] = 2*H[n-2]
    M[-1,-2] = H[n-2]
    for i in range(1, n-1):
        M[i,i-1] = H[i-1]
        M[i,i+1] = H[i]
        M[i,i] = 2*(H[i-1]+H[i])
    b = np.zeros(n)
    for i in range(0, n):
        if i == n-1:
            left = 3*dfb
        else:
            left = 3/H[i]*(A[i+1]-A[i])
        if i == 0:
            right = 3*dfa
        else:
            right = 3/H[i-1]*(A[i]-A[i-1])
        b[i] = left - right
    C = np.linalg.solve(M, b)

    # Calculamos los b_j
    B = np.zeros(n-1)
    for i in range(n-1):
        B[i] = (A[i+1]-A[i])/H[i]-(2*C[i]+C[i+1])*H[i]/3
    
    # Calculamos los d_j
    D = np.zeros(n-1)
    for i in range(n-1):
        D[i] = (C[i+1]-C[i])/(3*H[i])

    # Debemos hallar el trazador de la forma:
    # S_j(x) = a_j + b_j*(x-x_j) + c_j*(x-x_j)^2 + d_j*(x-x_j)^3
    CS = []
    for i in range(n-1):
        p = A[i] + B[i]*Polynomial([-X[i], 1]) + C[i]*Polynomial([-X[i], 1])**2 + D[i]*Polynomial([-X[i], 1])**3
        CS.append(p)
    return CS

def lineal_spline(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    n = len(X)

    CS = []
    for i in range(n-1):
        itr, _ = newton(X[i:i+2], Y[i:i+2])
        CS.append(itr)
    return CS

def eval_spline(CS, X, I):
    X = np.array(X)
    I = np.array(I)
    n = len(X)

    R = np.zeros(I.shape)
    for i in range(n-1):
        C = (X[i] <= I) & (I <= X[i+1])
        R[C] = CS[i](I[C])
    return R
