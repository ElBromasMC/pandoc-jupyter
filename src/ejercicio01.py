import numpy as np
from interpolation import hermite_table

f = lambda x : 3*x*np.exp(x) - np.exp(2*x)
df = lambda x : np.exp(x)*(3+3*x)-2*np.exp(2*x)

X = np.array([1, 1.05, 1.07])
Y = f(X)
Z = df(X)

P, H = hermite_table(X, Y, Z)

print(P)
print(H.transpose())
