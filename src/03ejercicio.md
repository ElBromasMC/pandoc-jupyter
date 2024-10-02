## SIS (dinámica vital)

Similar al anterior modelo, solo que se le añade nacimientos y muertes, lo que hace que la población sea dinámica. Ejemplos: Herpes.

$$
\left\{
\begin{split}
S' &= -\alpha SI + \beta I + \mu S -\eta S \\
I' &= \alpha SI - \beta I  + \mu I -\eta I
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

    \draw[line basic] ($(S.north) + (0, 1)$) -- (S.north) node[midway, left] {\(\mu\)};
    \draw[line basic] ($(I.north) + (0, 1)$) -- (I.north) node[midway, left] {\(\mu\)};

    \draw[line basic] (S.south) -- ($(S.south) - (0, 1)$) node[midway, left] {\(\eta\)};
    \draw[line basic] (I.south) -- ($(I.south) - (0, 1)$) node[midway, left] {\(\eta\)};

\end{tikzpicture}
\end{center}
```

### Solución

Sumamos las 2 ecuaciones para despejar la población.

$$
\begin{split}
(S+I)'=(\mu - \eta)(S+I)
\end{split}
$$

1. Si $\mu = \eta$, tendríamos un modelo similiar al SIS (sin inmunidad).
1. Si $\mu \neq \eta$, observamos que la población ya no es constante. 

**Puntos de equilibrio**

Hallaremos los puntos de equilibrio

$$
\left\{
\begin{split}
0 &= -\alpha SI + \beta I + \mu S -\eta S\\
0 &= \alpha SI - \beta I  + \mu I -\eta I
\end{split}
\right.
$$

$$
\begin{split}
0=I(\alpha S - \beta +\mu-\eta) \quad \Rightarrow\quad I=0 \quad\land\quad S=\frac{\beta+\eta-\mu}{\alpha}
\end{split}
$$

Analicemos ambos casos:

1. Para $I=0$

    $$0=(\mu-\eta)S \quad\Rightarrow\quad \mu=\eta \quad\lor\quad S=0$$

    Como $\mu\neq\eta$, entonces un punto seria $(0,0)$

1. Para $S=\frac{\beta+\eta-\mu}{\alpha}$

    $$
    \begin{split}
    I &= \cfrac{-(\mu-\eta)S}{\beta-\alpha S}= \cfrac{\beta+\eta-\mu}{\alpha}\\
    0&< \cfrac{\beta+\eta-\mu}{\alpha}
    \end{split}
    $$

    El punto seria $\left(\cfrac{\beta+\eta-\mu}{\alpha},\cfrac{\beta+\eta-\mu}{\alpha} \right)$

**Analicemos su equilibrio con el jacobiano**

$$
\begin{split}
J(S, I) =
    \begin{bmatrix}
        -\alpha I +\mu-\eta  & -\alpha S +\beta  \\
        \alpha I & \alpha S - \beta   + \mu  -\eta 
    \end{bmatrix}
\end{split}
$$

1. Para el primer punto $(0,0)$

    $$
    \begin{split}
    &A = J(0, 0) =
        \begin{bmatrix}
            \mu-\eta  &  +\beta  \\
            0 &  - \beta   + \mu  -\eta 
        \end{bmatrix} \\
    &tr(A) = 2(\mu-\eta) -\beta \\
    &det(A) =(\mu-\eta)^2 -\beta(\mu-\eta) \\
    &\Delta =\beta ^2
    \end{split}
    $$

1. Para el segundo punto $\left(\cfrac{\beta+\eta-\mu}{\alpha},\cfrac{\beta+\eta-\mu}{\alpha} \right)$

    $$
    \begin{split}
    &A = J\left(\frac{\beta+\eta-\mu}{\alpha},\frac{\beta+\eta-\mu}{\alpha}\right) =
        \begin{bmatrix}
            2(\mu-\eta) -\beta  & \mu-\eta   \\
            \beta +\eta-\mu& 0
        \end{bmatrix} \\
    &tr(A) = 2(\mu-\eta) -\beta \\
    &det(A) =-[(\mu-\eta)^2 -\beta(\mu-\eta)] \\
    &\Delta =8(\mu-\eta)^2 -8\beta(\mu-\eta) +\beta^2
    \end{split}
    $$

### Conclusiones

1. Para el punto $(0,0)$
    1. Se tiene que $tr(A) = 2(\mu - \eta) - \beta$ y $\Delta = (\mu - \eta)^2 - \beta(\mu - \eta)$.
    1. La estabilidad depende de los valores de $\mu - \eta$:
        1. Si $\mu - \eta < 0$ y $\beta > 0$, $tr(A) < 0$ y $\Delta > 0$ implican que $(0,0)$ es un **punto de silla**.
        1. Si $\mu - \eta > 0$ y $\Delta > 0$, entonces el punto $(0,0)$ es un **punto estable**.
1. Para el punto $\left(\frac{\beta + \eta - \mu}{\alpha}, \frac{\beta + \eta - \mu}{\alpha}\right)$
    1. Se tiene que $tr(A) = 2(\mu - \eta) - \beta$ y $det(A) = -[(\mu - \eta)^2 - \beta(\mu - \eta)]$.
    1. La estabilidad también depende de los valores de $\mu - \eta$:
        1. Si $\mu - \eta < 0$ y $\beta > 0$, $tr(A) < 0$ y $\Delta > 0$ implican que $\left(\frac{\beta + \eta - \mu}{\alpha}, \frac{\beta + \eta - \mu}{\alpha}\right)$ es un **punto de silla**.
        1. Si $\mu - \eta > 0$ y $\Delta > 0$, entonces el punto $\left(\frac{\beta + \eta - \mu}{\alpha}, \frac{\beta + \eta - \mu}{\alpha}\right)$ es un **punto estable**.
