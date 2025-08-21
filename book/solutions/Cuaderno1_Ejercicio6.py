steps = 10
umbral = 5

for step in range(steps):
    if step > umbral:
        print(step, "cruza el umbral")
    else:
        print(step, "no cruza el umbral")