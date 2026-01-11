"""
Programa: Conversión de temperatura de Celsius a Fahrenheit
YENSY MAYERLY CASTILLO MONSERRATE
Descripción:
Este programa solicita una temperatura en grados Celsius,
la convierte a grados Fahrenheit y muestra el resultado.
"""

# Solicitar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversión de Celsius a Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Variable booleana para verificar si la temperatura es mayor a 0 grados
sobre_congelacion = celsius > 0

# Mostrar resultados
print("Temperatura en Fahrenheit:", fahrenheit)
print("¿Está sobre el punto de congelación?", sobre_congelacion)

# Primer programa subido a GitHub


