def inversa(texto):
  largo = len(texto)
  inversa = ''
  for i in range(largo):
    #recordar que python comienza a contar en 0
    inversa += texto[largo-1-i]

  return inversa

print(inversa("estoy probando"))
print(inversa("radar"))