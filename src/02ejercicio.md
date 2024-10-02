## SIS (sin inmunidad)

Las personas susceptibles \textbf{S} puedes infectarse \textbf{I} y luego regresar al estado de susceptibles tras la recuperación, sin desarrollar inmunidad. Ejemplos: Gonorrea, Malaria, etc.

$$
\left\{
\begin{split}
S' &= -\alpha SI + \beta I \\
I' &= \alpha SI - \beta I 
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

    % Arrows
    \draw[line basic] ($(S.east)!0.5!(S.north east)$) -- ($(I.west)!0.5!(I.north west)$) node[midway, above] {\(\alpha\)};
    \draw[line basic] ($(I.west)!0.5!(I.south west)$) -- ($(S.east)!0.5!(S.south east)$) node[midway, below] {\(\beta\)};

\end{tikzpicture}
\end{center}
```

### Solución

Sumamos las 2 ecuaciones para despejar la población.

$$
\begin{split}
(S+I)'&=0 \\
N &= cte.
\end{split}
$$

**Puntos de equilibrio**

Hallaremos los puntos de equilibrio

$$
\left\{
\begin{split}
0 &= -\alpha SI + \beta I \quad \\
0 &=  \alpha SI - \beta I  \quad
\end{split}
\right.
$$

$$
0=I(-\alpha S +\beta) \Rightarrow I=0 \quad\land\quad S = \frac{\beta}{\alpha}
$$

Analicemos ambos casos:

1. Para $I=0$

    $\quad$ Observamos que $N=S+I \quad\Rightarrow N=S$

    $\quad$ Un punto de equilibrio es $(N,0)$

1. Para $S=\cfrac{\beta}{\alpha}$

    $\quad$ Observamos que $N=S+I \quad\Rightarrow I=N-\cfrac{\beta}{\alpha}$

    $\quad$ Un punto de equilibrio es $(\frac{\beta}{\alpha},N-\frac{\beta}{\alpha})$

    Como sabemos que $I>0$, entonces $N-\frac{\beta}{\alpha} > 0$

**Analicemos su equilibrio con el jacobiano**

$$
\begin{split}
J(S, I) =
    \begin{bmatrix}
        -\alpha I  & -\alpha S +\beta  \\
        \alpha I & \alpha S -\beta
    \end{bmatrix}
\end{split}
$$

1. Para el primer punto $(N, 0)$

    $$
    \begin{split}
    &A = J(N, 0) =
        \begin{bmatrix}
            0  & -\alpha N +\beta  \\
            0 & \alpha N -\beta
        \end{bmatrix} \\
    &tr(A) = \alpha N -\beta > 0 \\
    &det(A) = 0 \\
    &\Delta = (\alpha N -\beta)^2 > 0
    \end{split}
    $$

1. Para el segundo punto $\left(\frac{\beta}{\alpha},N-\frac{\beta}{\alpha}\right)$

    $$
    \begin{split}
    &A = J\left(\frac{\beta}{\alpha},N-\frac{\beta}{\alpha}\right) =
        \begin{bmatrix}
            -\alpha N +\beta  & 0  \\
            \alpha N -\beta & 0
        \end{bmatrix} \\
    &tr(A) = -(\alpha N -\beta) < 0 \\
    &det(A) = 0 \\
    &\Delta = (\alpha N -\beta)^2 > 0
    \end{split}
    $$

### Conclusiones

1. Para el punto $(N,0)$, y los datos hallados con el jacobiano. Observamos que es un **punto inestable**.
1. Para el punto $\left(\frac{\beta}{\alpha},N-\frac{\beta}{\alpha}\right)$, y los datos hallados con el jacobiano. Observamos que es un **punto estable**.

\newpage
