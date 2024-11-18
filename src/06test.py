import numpy as np
from ode import inver_power_translation

matrix = np.array([[0, 11, -5],
                   [-2, 17, -7],
                   [-4, 26, -10]])

vector = (np.array([1,1,1])).T
alpha = 4.2
iterations = 4

eigenvalue, eigenvector = inver_power_translation(alpha, matrix, vector, iterations)

print(f"Valor propio aproximado: {eigenvalue}")
print(f"Vector propio aproximado: {eigenvector}")
