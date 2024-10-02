# Análisis cualitativo

## Modelo SIRS (inmunidad parcial)

El modelo SIRS es un modelo epidemiológico utilizado para describir la propagación de enfermedades infecciosas que no confieren inmunidad permanente. A diferencia del modelo SIR clásico, en el modelo SIRS, los individuos que se recuperan de la enfermedad pueden volver a ser susceptibles después de un tiempo debido a la pérdida de inmunidad. Algunos ejemplos en la vida real son Neumonía bacteriana, Tos ferina y Gripe estacional.

$$
\left\{
\begin{split}
S' &= \alpha R - \beta SI \\
I' &= \beta SI - \Psi I \\
R' &= \Psi I - \alpha R
\end{split}
\right.
$$

### Diagrama compartamental

```{=latex}
\begin{center}
\begin{tikzpicture}
    \tikzset{node basic/.style={draw, very thick, minimum size=2em}}
    \tikzset{line basic/.style={thick, ->}}

    % Nodes
    \node[node basic] (S) at (0, 0) {\(S\)};
    \node[node basic] (I) at (2, 1) {\(I\)};
    \node[node basic] (R) at (4, 0) {\(R\)};

    % Arrows
    \draw[line basic] (S.east) -- (I.west) node[midway, above] {\(\beta\)};
    \draw[line basic] (I.east) -- (R.west) node[midway, above] {\(\Psi\)};

    \draw[line basic] ($(R.west)!0.5!(R.south west)$) -- ($(S.east)!0.5!(S.south east)$) node[midway, below] {\(\alpha\)};

\end{tikzpicture}
\end{center}
```

### Solución

Sumaremos y veremos como se comporta la población.

$$
\begin{split}
(S + I + R)' &= 0 \\
N' &= 0 \\
\therefore\quad N &= cte.
\end{split}
$$

**Puntos de equilibrio**

$$
\begin{split}
0 &= \alpha R - \beta SI \quad \\
0 &= \beta SI - \Psi I \quad \\
0 &= \Psi I - \alpha R \quad \\
0 &= I\cdot(\beta S - \Psi ) \\
\Rightarrow \quad  I&=0 \quad\lor\quad S = \frac{\Psi}{\beta}
\end{split}
$$

Analicemos ambos casos:

1. Para $I=0$

    Reemplazando
    
    $$0=\alpha R \quad\Rightarrow\quad R = 0$$
    
    Sabemos que $N=S+R+I$, entonces

    $$N=S+R+I \quad\Rightarrow\quad N = S$$

    Un punto de equilibrio es $(N,0,0)$

1. Para $S = \cfrac{\Psi}{\beta}$

    $$0 = \Psi I - \alpha R  \quad\Rightarrow\quad R =\cfrac{\Psi I}{\alpha}$$
    
    Sabemos que $N=S+R+I$, entonces
    
    $$N=\cfrac{\Psi}{\beta}+\cfrac{\Psi I}{\alpha}+I \quad\Rightarrow\quad \left(N -\frac{\Psi}{\beta}\right)\left(\frac{\alpha}{\alpha + \Psi}\right) = I$$

    Como $I>0$ y las tasas son positivas:
    
    $$K_0=N - \frac{\Psi}{\alpha} > 0 \Rightarrow N > \frac{\Psi}{\alpha}$$
    
    Un punto de equilibrio es $\left(\cfrac{\Psi}{\beta},K_0\left(\frac{\alpha}{\alpha + \Psi}\right),K_0\left(\frac{\Psi}{\alpha + \Psi}\right)\right)$

**Analicemos su equilibrio con el jacobiano**

En el sistema reducido:

$$
\begin{split}
J(S, I) =
    \begin{bmatrix}
        -\alpha -\beta I  & -\alpha-\beta S \\
        \beta I & \beta S - \Psi
    \end{bmatrix}
\end{split}
$$

1. Para el primer punto $(N, 0)$

    $$
    \begin{split}
    &A = J(N, 0) =
        \begin{bmatrix}
            -\alpha & -\alpha - \beta N \\
            0 & \beta N - \Psi
        \end{bmatrix} \\
    &det(A) = -\alpha (\beta N - \Psi) < 0
    \end{split}
    $$

1. Para el segundo punto $\left(\cfrac{\Psi}{\beta},K_0\left(\frac{\alpha}{\alpha + \Psi}\right)\right)$

    $$
    \begin{split}
    &A = J\left(\cfrac{\Psi}{\beta},K_0\left(\frac{\alpha}{\alpha + \Psi}\right)\right) =
        \begin{bmatrix}
            -\alpha - \cfrac{\beta\alpha K_0}{\alpha + \Psi} &  -\alpha-\Psi\\
            \cfrac{\beta\alpha K_0}{\alpha + \Psi} & 0
        \end{bmatrix} \\
    &tr(A) = -\alpha\left(1+\cfrac{\beta K_0}{\alpha + \Psi}\right) < 0 \\
    &det(A) = \beta\alpha K_0 > 0 \\
    &\Delta = \alpha^2(K_0+1)^2 - 4\alpha K_0(\alpha+\Psi)
    \end{split}
    $$

### Conclusiones

1. En el nodo $(N,0,0)$, ya que $det(A) < 0$, se mostró que es un **punto silla**.
1. En el nodo $\left(\cfrac{\Psi}{\beta},K_0\left(\frac{\alpha}{\alpha + \Psi}\right),K_0\left(\frac{\Psi}{\alpha + \Psi}\right)\right)$, ya que $tr(A) < 0$, se mostró que es un **punto estable**.

\newpage
