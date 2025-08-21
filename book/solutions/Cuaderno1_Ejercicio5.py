pi = 3.14
steps = 10
dt = 0.1    # en segundos
cum_x = 0   # valor acumulado de x

for step in range(steps):
    t = step * dt    # usa dt aquí
    x = 2 * pi / 0.01 * t
    cum_x = cum_x + x
    
print(f"x acumulado =", cum_x)