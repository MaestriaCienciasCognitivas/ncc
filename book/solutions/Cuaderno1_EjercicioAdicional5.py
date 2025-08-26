def es_palindromo(palabra):
  palabra_inversa = inversa(palabra)
  return palabra_inversa == palabra

print(es_palindromo("radar"))
print(es_palindromo("rodar"))