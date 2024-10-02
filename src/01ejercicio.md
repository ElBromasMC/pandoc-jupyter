# Análisis cualitativo

## Modelo SIR

$$
\left\{
\begin{split}
S' &= \alpha N - \alpha S - \beta SI \\
I' &= \beta SI - \alpha I - \Psi I \\
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
    \node[node basic] (I) at (2, 0) {\(I\)};
    \node[node basic] (R) at (4, 0) {\(R\)};

    % Arrows
    \draw[line basic] ($(S.north) + (0, 1)$) -- (S.north) node[midway, left] {\(\alpha N\)};

    \draw[line basic] (S.east) -- (I.west) node[midway, above] {\(\beta\)};
    \draw[line basic] (I.east) -- (R.west) node[midway, above] {\(\Psi\)};

    \draw[line basic] (S.south) -- ($(S.south) - (0, 1)$) node[midway, left] {\(\alpha\)};
    \draw[line basic] (I.south) -- ($(I.south) - (0, 1)$) node[midway, left] {\(\alpha\)};
    \draw[line basic] (R.south) -- ($(R.south) - (0, 1)$) node[midway, left] {\(\alpha\)};

\end{tikzpicture}
\end{center}
```

### Solución

Sumamos las 3 ecuaciones para despejar la población.

$$
\begin{split}
(S + I + R)' &= \alpha N - \alpha S - \alpha I - \alpha R \\
(S + I + R)' &= \alpha (N - (S + I + R)) \\
N' &= \alpha (N - N) = 0 \\
\therefore\quad N &= cte.
\end{split}
$$

Como la población es constante, podemos a reducir el sistema a dos ecuaciones.

$$
\left\{
\begin{split}
S' &= \alpha N - \alpha S - \beta SI \\
I' &= \beta SI - \alpha I - \Psi I
\end{split}
\right.
$$

**Puntos de equilibrio**

Hallaremos los puntos de equilibrio

$$
\left\{
\begin{split}
\alpha N - \alpha S - \beta SI &= 0 \\
\beta SI - \alpha I - \Psi I &= 0
\end{split}
\right.
$$

De la segunda ecuación:

$$
\begin{split}
&I(\beta S - \alpha - \Psi) = 0 \\
\therefore\quad &I = 0 \quad\lor\quad S = \frac{\alpha + \Psi}{\beta}
\end{split}
$$

Analicemos ambos casos:

1. Para $I=0$

    $$
    \begin{split}
    &\alpha N - \alpha S = 0 \\
    &\underline{S = N} \\
    &S + I + R = N \\
    &\underline{R = 0}
    \end{split}
    $$

    Por lo tanto, un punto de equilibrio es $(N, 0, 0)$

1. Para $S = \frac{\alpha + \Psi}{\beta}$

    $$
    \begin{split}
    &\alpha N - \alpha S - \beta SI = 0 \\
    &I = \frac{\alpha}{\beta}\left(\frac{N}{S} - 1\right) \\
    &\underline{I = \frac{\alpha}{\beta}\left(\frac{\beta N}{\alpha + \Psi} - 1\right)} \\
    &R = N - S - I \\
    &R = N - \frac{\alpha + \Psi}{\beta} - \frac{\alpha N}{\alpha + \Psi} + \frac{\alpha}{\beta} \\
    &R = \frac{\Psi N}{\alpha + \Psi} - \frac{\Psi}{\beta} \\
    &\underline{R = \frac{\Psi}{\beta}\left(\frac{\beta N}{\alpha + \Psi} - 1\right)}
    \end{split}
    $$

    Por lo tanto, un punto de equilibrio es $\left(\frac{\alpha + \Psi}{\beta}, \frac{\alpha}{\beta}\left(\frac{\beta N}{\alpha + \Psi} - 1\right), \frac{\Psi}{\beta}\left(\frac{\beta N}{\alpha + \Psi} - 1\right)\right)$

    Además como $I, R > 0$ se tiene que:

    $$
    \begin{split}
        \frac{\beta N}{\alpha + \Psi} - 1 &> 0 \\
        \frac{\beta N}{\alpha + \Psi} &> 1 \\
    \end{split}
    $$

**Analicemos su equilibrio con el jacobiano**

En el sistema reducido:

$$
\begin{split}
J(S, I) =
    \begin{bmatrix}
        - \alpha - \beta I & - \beta S \\
        \beta I & \beta S - \alpha - \Psi
    \end{bmatrix}
\end{split}
$$

1. Para el primer punto $(N, 0)$

    $$
    \begin{split}
    &J(N, 0) =
        \begin{bmatrix}
            - \alpha & - \beta N \\
            0 & \beta N - \alpha - \Psi
        \end{bmatrix} \\
    &tr(J(N. 0)) = - 2\alpha + \beta N - \Psi \\
    &det(J(N, 0)) = -\alpha(\beta N - (\alpha+\Psi))
    \end{split}
    $$

    Usando $\frac{\beta N}{\alpha + \Psi} > 1$

    $$
    \begin{split}
        tr(J(N, 0)) &> 0 \\
        det(J(N, 0)) &< 0
    \end{split}
    $$

1. Para el segundo punto $\left(\frac{\alpha + \Psi}{\beta}, \frac{\alpha}{\beta}\left(\frac{\beta N}{\alpha + \Psi} - 1\right)\right)$

    Sean $K_0 = \frac{\beta N}{\alpha + \Psi} - 1$

    $$
    \begin{split}
    &A = J\left(\frac{\alpha + \Psi}{\beta}, \frac{\alpha}{\beta}K_0\right) =
        \begin{bmatrix}
            -\alpha(K_0+1)  & -(\alpha +\Psi) \\
            \alpha K_0 & 0
        \end{bmatrix} \\
    &tr(A) = -\alpha(K_0+1) \\
    &det(A) = (\alpha K_0)(\alpha+\Psi) \\
    &\Delta = \alpha^2(K_0+1)^2 - 4\alpha K_0(\alpha+\Psi)
    \end{split}
    $$

    Usando $\frac{\beta N}{\alpha + \Psi} > 1$

    $$
    \begin{split}
        tr(J(N, 0)) &< 0 \\
        det(J(N, 0)) &> 0
    \end{split}
    $$

### Conclusiones

1. En el punto de equilibrio $(N;0;0)$ observamos que la $det(A) < 0$ y $tr(A) > 0 $ por lo tanto es un **punto silla**.
1. En el punto de equilibrio $\left( \cfrac{\alpha + \Psi}{\beta}; \quad \left(\cfrac{\alpha} {\beta}\right)K_0; \quad\left(\cfrac{\Psi}{\beta}\right)K_0 \right)$, observamos que con la $det(A)> 0$ y $tr(A) < 0 $  llegamos a que es un **punto estable**. Pero para saber más sobre su naturaleza, debemos saber si $\Delta$ es mayor, menor o igual a 0.
    - Si $\Delta > 0$ el punto es **nodo**
    - Si $\Delta < 0$ el punto es **espiral**
    - Si $\Delta = 0$ el punto es **degenerado**
