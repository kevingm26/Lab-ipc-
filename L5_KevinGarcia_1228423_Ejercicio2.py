# Introduccion a la programacion
# 12/09/2023
# Kevin Garcia 1228423
# Objetivo: hacer un comando para determinar los dias de la semana ingresando un numero del 1 al 7

#Ejercicio 02
#entrada: numero del dia
#proceso:
x = input(" Ingrese un número de día: ")
x = int(x)
d=""
if x<0 or x>7:
    d="Ingresar unicamente un numero entre 1 y 7"
elif x==1:
    d="lunes"
elif x==2:
    d="martes"
elif x==3:
    d="miercoles"
elif x==4:
    d="jueves"
elif x==5:
    d="viernes"
elif x==6:
    d="sabado"
else:
    d="domingo"
#salida:
print("Día: " +d)