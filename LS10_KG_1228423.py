#Lab de intro a la programación seccion 17
#10/10/2023
#Kevin Garcia
#1228423
#Objetivo: Crear un módulo para convertir una cantidad expresada en centímetros 
#Entrada
# Módulo de conversiones
def centimetros_a_metros(cantidad):
    return cantidad / 100

def centimetros_a_kilometros(cantidad):
    return cantidad / 100000

def centimetros_a_pulgadas(cantidad):
    return cantidad / 2.54

def centimetros_a_pies(cantidad):
    return cantidad / 30.48

# Módulo principal
while True:
    try:
        centimetros = float(input("Ingrese la cantidad en centímetros: "))
        print("Seleccione la unidad de medida a la que desea convertir:")
        print("1. Metros")
        print("2. Kilómetros")
        print("3. Pulgadas")
        print("4. Pies")
        opcion = int(input("Opción: "))

        if opcion == 1:
            resultado = centimetros_a_metros(centimetros)
            unidad = "metros"
        elif opcion == 2:
            resultado = centimetros_a_kilometros(centimetros)
            unidad = "kilómetros"
        elif opcion == 3:
            resultado = centimetros_a_pulgadas(centimetros)
            unidad = "pulgadas"
        elif opcion == 4:
            resultado = centimetros_a_pies(centimetros)
            unidad = "pies"
        else:
            print("Opción no válida")
            continue

        print(f"{centimetros} centímetros son {resultado} {unidad}")

        respuesta = input("¿Desea realizar otra conversión? (Sí/No): ")
        if respuesta.lower() != "si":
            break

    except ValueError:
        print("Por favor, ingrese una cantidad válida en centímetros.")