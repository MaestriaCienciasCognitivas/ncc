def superposicion(lista1,lista2):
  superponen = False
  for i in lista1:
    if i in lista2:
      superponen = True
      break

  return superponen

print(superposicion([0, 1, 2], [2, 3, 4]))
print(superposicion([0, 1, 2], [3, 4, 5]))