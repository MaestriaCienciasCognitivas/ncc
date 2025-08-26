def generar_n_caracteres(n, caracter):
  caracteres = ''
  for i in range(n):
    caracteres += caracter

  return caracteres

print(generar_n_caracteres(5, "x"))
print(generar_n_caracteres(3, "*"))