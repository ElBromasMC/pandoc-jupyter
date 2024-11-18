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


def inver_power_translation(alpha, matrix, vector, iterations=4):
    """
    Función que realiza el método de la potencia inversa con un desplazamiento 
    para aproximar el valor propio más pequeño de una matriz. La función itera 
    para refinar el valor propio y el vector propio asociado.

    Parámetros:
    - alpha: float, el desplazamiento aplicado a la matriz para mejorar la convergencia.
    - matrix: arreglo n-dimensional, la matriz de la cual se desea encontrar el valor propio más pequeño.
    - vector: arreglo unidimensional, el vector inicial para el proceso de iteración.
    - iterations: int, opcional (por defecto es 4), el número de iteraciones a realizar.

    Retorna:
    - l1: float, la estimación del valor propio.
    - vect: arreglo 1D, el vector propio asociado con el valor propio más pequeño.
    """
    # Obtiene la dimensión de la matriz
    n = len(matrix)
    
    # Desplaza la matriz restando alpha en la diagonal y luego la invierte
    matrix = matrix - alpha * np.identity(n)
    matrix = np.linalg.inv(matrix)
    
    # Inicializa listas para almacenar valores propios y vectores propios en cada iteración
    C = []
    xi = []

    # Realiza el número especificado de iteraciones
    for _ in range(iterations):
        # Multiplica la matriz por el vector
        x1 = matrix.dot(vector)
        
        # Encuentra el valor absoluto más grande en x1 para escalar
        n = float(max(abs(x1)).item())
        
        # Ajusta el signo de n si no está en x1
        if n not in x1:
            n = -n    
                
        # Normaliza el vector y redondea para estabilidad
        vector = np.round(x1 / n, 6)
        
        # Almacena la aproximación del valor propio y vector propio en esta iteración
        C.append(n)
        xi.append(vector)
    
    # Calcula la aproximación final del valor propio usando el inverso del último factor de escala
    eigenvalue = round((1 / C[-1]) + alpha)
    eigenvector = xi[-1]
    
    return eigenvalue, eigenvector