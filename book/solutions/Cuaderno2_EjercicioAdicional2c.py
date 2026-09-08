import numpy as np

def generar_matriz(num_filas, num_cols, rango):
    minimo = rango[0]
    maximo = rango[1]
    return minimo + np.random.rand(num_filas, num_cols) * (maximo - minimo)

def generar_muestra(matriz, n):
    return np.random.choice(matriz.flatten(), size=n)

def funcion(n_filas, n_columnas, rango, n_muestra):
  array = generar_matriz(n_filas, n_columnas, rango)
  muestra = generar_muestra(array, n_muestra)
  return array, muestra

# Establecemos el generador de números aleatorios
np.random.seed(0)

array, muestra = funcion(3, 2, [0, 20], 3)
print(array)
print(muestra)
