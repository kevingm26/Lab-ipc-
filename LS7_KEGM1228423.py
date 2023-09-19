#Laboratorio Introduccion a la programacion
#19/09/2023
#Kevin Garcia
#Objetivo: Que el sistema realice las operaciones que se le piden al comando usando tambien la formula cuadratica 
import math

while True:
    print("Ejercicio 3: Jerarquía de operaciones")
    print("1. Calcular a * b + c")
    print("2. Calcular a * (b + c)")
    print("3. Calcular a / b * c")
    print("4. Calcular 3*a + 2*b / c^2")
    print("5. Calcular la fórmula cuadrática")
    print("6. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    if opcion == "6":
        print("Hasta la proxima")
        break

    try:
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
    except ValueError:
        print("Ingrese números válidos.")
        continue

    if opcion == "1":
        resultado = a * b + c
    elif opcion == "2":
        resultado = a * (b + c)
    elif opcion == "3":
        resultado = a / b * c
    elif opcion == "4":
        resultado = 3 * a + 2 * b / (c ** 2)
    elif opcion == "5":
        if a == 0:
            print("Error: a no puede ser igual a 0.")
            continue
        discriminante = b ** 2 - 4 * a * c
        if discriminante < 0:
            print("Error: b^2 - 4ac es menor que 0. No se puede calcular la raíz cuadrada de un número negativo.")
            continue
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        resultado = f"x1 = {x1}, x2 = {x2}"
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    print(f"Resultado: {resultado}\n")

