# Introduccion a la programacion laboratorio
# 26/09/2023
# Kevin Garcia 1228423
# Objetivo: Realizar un programa el cual realice un trabajo factorial o secuancial de Fibonacci segun lo pedido

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = [0, 1]
        while len(seq) < n:
            next_num = seq[-1] + seq[-2]
            seq.append(next_num)
        return seq

while True:
    # Mostrar el menú
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    # Solicitar la opción al usuario
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Opción 1: Calcular el factorial
        try:
            numero = int(input("Ingrese un número: "))
            resultado = factorial(numero)
            print(f"{numero}! = {resultado}")
        except ValueError:
            print("Ingrese un número válido.")
    
    elif opcion == "2":
        # Opción 2: Mostrar la secuencia de Fibonacci
        try:
            numero = int(input("Ingrese un número: "))
            secuencia = fibonacci(numero)
            print("Secuencia de Fibonacci:", ", ".join(map(str, secuencia)))
        except ValueError:
            print("Ingrese un número válido.")
    
    elif opcion == "3":
        # Opción 3: Salir del programa
        print("¡Hasta luego!")
        break
    
    else:
        # Opción inválida
        print("seleccione una opción válida.")

