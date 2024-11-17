import numpy as np


def power_method(matrix, vector, iterations=4):
    """
    Ejemplo:
    matrix = np.matrix([[2, 1, 1],
                        [1, 2, 1], 
                        [1, 1, 2]])
    vector = np.matrix([1, -1, 2]).T
    C, xi = normalize_iterations(matrix, vector)

    Parámetros:
    matrix (numpy.matrix): La matriz cuadrada para multiplicar.
    vector (numpy.matrix): El vector inicial para iterar.
    iterations (int): El número de iteraciones a realizar.

    Retorna:
    - C : Lista de autovalores
    - xi : lista de autovectores
    """
    C = []       
    xi = []  

    for i in range(iterations):
        x1 = matrix.dot(vector)
        # print(f"x{i+1}: {x1}\n")
        n = float(max(abs(x1)).item())
        
        #redondeo a 6 decimales
        vector = np.round(x1 / n, 6)
        
        xi.append(vector)
        C.append(n)
    
    return C, xi

def inverse_powers_method(matrix, vector, iterations=4):
    """
    Parámetros:
    matrix (numpy.matrix): La matriz que se hallara su inversa.
    vector (numpy.matrix): El vector inicial para iterar.
    iterations (int): El número de iteraciones a realizar.

    Retorna:
    - C : Lista de autovalores
    - xi : lista de autovectores
    """

    inverse_matrix = np.linalg.inv(matrix)

    return power_method(inverse_matrix, vector, iterations=4)

def aitken_acceleration(r):
    """
    Aplica la aceleración de Aitken a una sucesión {r_k}.
    
    Parámetros:
    r (list of float): La sucesión original de autovalores.
    
    Retorna:
    s (list of float): La sucesión acelerada .
    """
    s = []  # Lista para almacenar los valores acelerados {s_k}
    
    # Asegúrate de que hay suficientes elementos en la sucesión para aplicar Aitken
    if len(r) < 3:
        print("La sucesión debe tener al menos 3 elementos para aplicar la aceleración de Aitken.")
        return s
    
    # Aplicar la fórmula de Aitken a partir del índice 2 (correspondiente a k=3)
    for k in range(2, len(r)):
        numerator = (r[k] - r[k-1]) ** 2
        denominator = r[k] - 2 * r[k-1] + r[k-2]
        
        if denominator != 0:  # Evitar división por cero
            s_k = r[k] - numerator / denominator
            s.append(s_k)
        else:
            # Si el denominador es cero, se suspende la aceleración de Aitken
            print("Denominador cero en k =", k+1, "La aceleración se suspende.")
            break
            
    return s
