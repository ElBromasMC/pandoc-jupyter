import numpy as np
from interpolation import hermite_table

CONV = 22/15

X = np.array([0, 0.4])
Y = np.array([0, 55.5])
Z = np.array([95, 92])

P, H = hermite_table(X, Y, Z)

print(P)
print(H)

# Punto a
DP = P.deriv()
print(DP)
print("La velocidad de la bola de beisbol aproximadamente en t=0.2 es ", DP(0.2))

# Punto b
roots = DP.deriv().roots()
sol = roots[(0 <= roots) & (roots <= 0.4)]
print(sol)
print(DP(sol))

print("Por otro lado")
P2, H2 = hermite_table(X, Y, CONV*Z)
print(P2)
print(H2)

DP2 = P2.deriv()
print(DP2)
print("La velocidad de la bola de beisbol aproximadamente en t=0.2 es ", DP2(0.2), DP2(0.2)/CONV)

roots = DP2.deriv().roots()
sol = roots[(0 <= roots) & (roots <= 0.4)]
print(sol)
print(DP2(sol), DP2(sol)/CONV)

