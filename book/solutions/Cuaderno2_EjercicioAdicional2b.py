import numpy as np

# Primero definimos el numero de filas y columnas que queremos para nuestra matriz
num_filas = 3
num_cols = 3

def generar_matriz(num_filas, num_cols, rango):
    minimo = rango[0]
    maximo = rango[1]
    return minimo + np.random.rand(num_filas, num_cols) * (maximo - minimo)

def generar_muestra(matriz, n):
    return np.random.choice(matriz.flatten(), size=n)

# Establecemos el generador de números aleatorios
np.random.seed(0)

print(generar_muestra(generar_matriz(3, 3, [10, 20]), 3))
