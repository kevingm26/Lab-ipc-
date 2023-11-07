#Kevin Garcia 1228423
#Laboratorio programacion 
#Ingenieria civil 
class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = True
        self.tipoCambioDolar = 1.0  # Valor por defecto de cambio a dólares
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def CalcularPrecioEnDolares(self):
        return self.precio / self.tipoCambioDolar

    def MostrarInformacion(self):
        disponibilidad = self.MostrarDisponibilidad()
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares ${self.CalcularPrecioEnDolares()} {disponibilidad}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.DefinirPrecio(self.precio - miDescuento)

        # Ejemplo de uso:
auto = Automovil()
auto.DefinirMarca("BMW")
auto.DefinirModelo(2023)
auto.DefinirPrecio(501768.3)
auto.DefinirTipoCambio(7.94)
auto.CambiarDisponibilidad()
auto.AplicarDescuento(500)
print(auto.MostrarInformacion())
