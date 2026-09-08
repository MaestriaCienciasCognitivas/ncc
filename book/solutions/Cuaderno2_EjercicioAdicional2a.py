import numpy as np

# Primero definimos el numero de filas y columnas que queremos para nuestra matriz
num_filas = 3
num_cols = 3

def generar_matriz(num_filas, num_cols, rango):
    minimo = rango[0]
    maximo = rango[1]
    return minimo + np.random.rand(num_filas, num_cols) * (maximo - minimo)

# Establecemos el generador de números aleatorios
np.random.seed(0)

print(generar_matriz(3, 3, [10, 20]))
