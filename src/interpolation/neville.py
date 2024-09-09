import numpy as np

def neville(X, Y , x):
    n = len(X)
    matrix_neville = np.zeros((n, n), dtype=object)
    matrix_neville[:,0] = Y
    for j in range(1, n):
        for i in range(j, n):
            top1 = (x - X[i - j]) * matrix_neville[i][j - 1]
            top2 = (x - X[i])*matrix_neville[i - 1][j - 1]
            bot  = X[i] - X[i - j]
            matrix_neville[i,j] = (top1 - top2)/bot
    return matrix_neville

# X: Lista de los nodos de la interpolación
# Y: Lista de los valores de la interpolación
# x: Punto a evaluar
# res: Polinomio de interpolación evaluado en x
def neville_recursive(X, Y, x):
    n = len(X)
    def helper(i, j):
        if (i == j):
            return Y[i]
        else:
            top1 = (x - X[i])*helper(i+1, j)
            top2 = (x - X[j])*helper(i, j-1)
            bottom = X[j]-X[i]
            return (top1 - top2)/bottom
    res = helper(0, n-1)
    return res
