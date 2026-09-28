def regla_hebbiana(eta, x_pre, x_post):
    """Regla de Hebb

    Parameters
    ----------
    eta : float
        Tasa de aprendizaje.
    x_pre : ndarray
        Actividad de las neuronas pre-sinápticas.
    x_post : float
        Actividad de la neurona post-sináptica.

    Returns
    -------
    delta_w : ndarray
        Cambio en los pesos sinápticos.
    """
    return  eta * x_pre * x_post

# Sólo la célula 1 dispara
x_pre = np.array([1, 0])

# Pesos iguales para las dos células
w = np.array([0.5, 0.5])

# Cálculamos como debería disparar la neurona post-sináptica en esta configuración
x_post = x_pre @ w
print(f"x_post = {x_post}")

delta_w = regla_hebbiana(eta=0.1, x_pre=x_pre, x_post=x_post)
print(f"delta_w = {delta_w}")