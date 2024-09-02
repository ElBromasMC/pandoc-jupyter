---
title: "Resolución del Laboratorio 1 - Interpolación"
# subtitle: ""
author: ["Espinoza Huaman, Diego Alexhander", "Linares Rojas, Ander Rafael", "Delgado Perez, Jose Alexis"]
# date: \today{}
institute: "Universidad Nacional Mayor de San Marcos"
# keywords: []
lang: es-PE
toc: true
numbersections: true
# Specific to eisvogel
titlepage: true
toc-own-page: true
footer-left: "Lab 1"
---

# Código utilizado

Módulos locales que importamos en los ejercicios:

## Interpolación polinómica

### Método de Lagrange

```python
import numpy as np
from numpy.polynomial import Polynomial

# x: Lista de los nodos de la interpolación
# y: Lista de los valores de la interpolación
# return:
#   itr: El polinomio de interpolación
#   L: Lista que contiene los polinomios base
def lagrange(x, y):
    n = len(x)
    # Calculamos los polinomios base
    L = []
    itr = Polynomial(0)
    for i in range(n):
        base = Polynomial([1])
        for j in range(n):
            if j != i:
                factor = Polynomial([-x[j], 1])/(x[i]-x[j])
                base = base * factor
        L.append(base)
        itr += y[i] * base
    return itr, L
```

### Método de Newton

```python
import numpy as np
from numpy.polynomial import Polynomial

# x: Lista de los nodos de la interpolación
# y: Lista de los valores de la interpolación
# return:  
#   itr: El polinomio de interpolación
#   N: Matriz que representa la tabla de diferencias divididas
def newton(x, y):
    n = len(x)
    N = np.zeros((n, n))
    # Completamos la tabla de diferencias divididas
    N[0,:] = y
    for i in range(1,n):
        for j in range(n-i):
            top = N[i-1,j] - N[i-1,j+1]
            bottom = x[j] - x[j+i]
            N[i,j] = top/bottom
    # Calculamos los polinomios base
    itr = Polynomial(0)
    for i in range(n):
        base = Polynomial([1])
        for j in range(i):
            factor = Polynomial([-x[j], 1])
            base = base * factor
        itr += N[i,0] * base
    return itr, N
```

## Error en la interpolación

### Error general

```python
import numpy as np
import sympy as sp
import math

# f_sym: Es una función simbólica de variable 'x' que representa la función a aproximar
# nodes: Lista que contiene los nodos de la interpolación
# xs: Lista de puntos donde evaluar el error
# error_bound: Lista de las cotas de error
def general_error_bound(f_sym, nodes, xs):
    n = len(nodes)
    a = min(nodes)
    b = max(nodes)
    x_sym = sp.symbols('x')

    # Calculamos la n derivada de la función
    nth_derivative = sp.diff(f_sym, x_sym, n)

    # Calculamos las cota de error
    M = sp.maximum(nth_derivative, x_sym, sp.Interval(a, b)).evalf()
    error_bound = []
    for elem in xs:
        P = 1
        for i in range(n):
            P *= abs(elem - nodes[i])
        error_bound.append(P*M/math.factorial(n))
    return error_bound
```

### Error en intervalos equiespaciados

```python
import numpy as np
import sympy as sp
import math

# f_sym: Es una función simbólica de variable 'x' que representa la función a aproximar
# n: Es el número de nodos que se van a utilizar en la interpolación
# a, b: Intervalo de la interpolación
# error_bound: La cota del error para una interpolación con nodos igualmente espaciados
def evenly_error_bound(f_sym, n, a, b):
    x_sym = sp.symbols('x')

    # Calculamos la n derivada de la función
    nth_derivative = sp.diff(f_sym, x_sym, n)
    
    # Calculamos la cota de error
    M = sp.maximum(nth_derivative, x_sym, sp.Interval(a, b)).evalf()
    h = (b-a)/(n-1)
    error_bound = h**n*M/(4*n)
    
    return error_bound

```