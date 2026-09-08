import imageio.v3 as iio
import matplotlib.pyplot as plt

# Cargamos la imagen desde la URL
imagen = iio.imread('https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg')

print(imagen.shape)

plt.imshow(imagen)
plt.show()

seleccion = imagen[1500:2000, 1000:1500, :]
plt.imshow(seleccion)    # descomenta esta línea
plt.show()
