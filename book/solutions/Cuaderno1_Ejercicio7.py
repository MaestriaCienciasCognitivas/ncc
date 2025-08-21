def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)

print(f"{10}! =", factorial(10))