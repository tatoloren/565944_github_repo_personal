
# Declarar lista global de temperaturas
temperaturas = [22, 24, 19, 23, 25, 21, 20]

# 1. Mostrar todas las temperaturas
print("Temperaturas de la semana:")
for temp in temperaturas:
    print(temp)

# 2. Calcular promedio, máximo y mínimo
suma = 0
for temp in temperaturas:
    suma += temp

promedio = suma / len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

print("\nPromedio:", promedio)
print("Temperatura máxima:", maxima)
print("Temperatura mínima:", minima)

# 3. Contar días con temperatura mayor a 22
contador = 0
for temp in temperaturas:
    if temp > 22:
        contador += 1

print("Días con temperatura mayor a 22:", contador)