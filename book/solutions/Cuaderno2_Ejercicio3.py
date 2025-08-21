dt = 0.001       # en segundos
i_mean = 25e-11  # en amperios
steps = 10
i = np.zeros(steps)

# Itera sobre varios pasos, la variable 'step' toma valores de 0 a `steps`
for step in range(steps):
  # Calcula el valor de t
  t = step * dt

  # Calculá el valor de I en el instante t y guardalo en el array `i`
  i[step] = i_mean * (1 + np.sin(2 * np.pi / 0.01 * t))

plt.scatter(np.linspace(0, steps * dt, num=steps, endpoint=False), i)
plt.show()