dt = 0.001       # en segundos
i_mean = 25e-11  # en amperios

# Itera sobre 10 pasos, la variable 'step' toma valores de 0 a 9
for step in range(10):
  # Calcula el valor de t
  t = step * dt

  # Calcula el valor de I en el instante t
  i = i_mean * (1 + np.sin(2 * np.pi / 0.01 * t))

  print(i)