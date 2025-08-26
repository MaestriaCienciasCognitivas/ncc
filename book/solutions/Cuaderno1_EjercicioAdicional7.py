def sum(lista):
  suma = 0
  for i in lista:
    suma += i

  return suma

def multip(lista):
  multiplicacion = 1
  for i in lista:
    multiplicacion = multiplicacion * i

  return multiplicacion

print(sum([1,2,3,4]))
print(multip([1,2,3,4]))