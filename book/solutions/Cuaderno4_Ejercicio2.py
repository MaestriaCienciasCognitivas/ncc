# 1. No hay un único par correcto. Una distancia de entre 8 y 12 píxeles entre los centros
# suele dar correlaciones en ese rango.
# Abajo elegimos un ejemplo:

centro1 = np.array([32, 28])
centro2 = np.array([32, 36])

campo1 = L(n=64, centro=centro1)
campo2 = L(n=64, centro=centro2)

respuesta1 = np.sum(estimulos * campo1, axis=(1, 2))
respuesta2 = np.sum(estimulos * campo2, axis=(1, 2))

X = np.stack([respuesta1, respuesta2], axis=1)