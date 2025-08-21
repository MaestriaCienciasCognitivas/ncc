v = -52.0
umbral = -55.0
periodo_refractario = True

pa = v > umbral and not periodo_refractario

print("Potencial de acción:", pa)