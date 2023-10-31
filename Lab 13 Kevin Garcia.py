# Lab Intro a la programación sec. 17
# 31/10/2023
# Kevin Garcia
from datetime import datetime

class Persona:
    def _init_(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = None

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} {self.apellido_casada}"
        else:
            return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def obtener_edad(self):
        if self.fecha_nacimiento:
            hoy = datetime.now()
            edad = hoy.year - self.fecha_nacimiento.year
            if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
                edad -= 1
            return edad
        else:
            return None

# Ejemplo de uso:
persona = Persona()
persona.insertar_nombres("Juan")
persona.insertar_apellidos("Pérez")
persona.insertar_apellido_casada("Gómez")
persona.insertar_fecha_nacimiento(datetime(1980, 5, 15))

print(f"Nombre completo: {persona.obtener_nombre_completo()}")
print(f"Edad: {persona.obtener_edad()} años")