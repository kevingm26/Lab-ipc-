# Introduccion a la programacion
# 12/09/2023
# Kevin Garcia 1228423
# Objetivo: hacer un comando para determinar si un numero es positivo, negativo o cero

#Entrada: numero entero

#proceso
print("Ejercicio 1")
try:
    numero = int(input("Ingresar un número que sea entero: "))
except ValueError:
    print(" Unicamente valido los numeros enteros, intentar de nuevo")
    exit(1)
if numero > 0:
    resultado = "positivo"
elif numero < 0:
    resultado = "negativo"
else:
    resultado = "cero"
    #salida
print("RESULTADO:", resultado)

