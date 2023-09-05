#Laboratorio de programacion seccion 17
# 5/09/2023
# Kevin Eduardo Garcia Miralda
#Objetivo: Crear un programa en Python que calcule la raiz de un numero.
#Entrada: Numero 1, Numero 2
#Proceso: 
# Paso 1: Solicitar al usuario que ingrese los números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Paso 2: Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Asegurémonos de que el denominador no sea cero antes de realizar la división
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero."

# Paso 3: Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
