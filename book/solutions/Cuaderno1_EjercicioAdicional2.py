def max_de_tres(x, y, z):
  if x > y:
    if x > z:
      return x
    else:
      return z
  else:
    if y > z:
      return y
    else:
        return z

print(max_de_tres(4, 3, 2))
print(max_de_tres(2, 3, 1))
print(max_de_tres(-1, 0, 1))
print(max_de_tres(-7, -5, -4))