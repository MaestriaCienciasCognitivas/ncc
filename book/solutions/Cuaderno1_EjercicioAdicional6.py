def es_vocal(letra):
  vocales = ['a','e','i','o','u']
  # notar que el .lower() hace que la funcion
  # funcione icluso si el caracter se le da en
  # mayuscula
  return letra.lower() in vocales 

print(es_vocal("a"))
print(es_vocal("f"))