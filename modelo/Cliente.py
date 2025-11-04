from modelo.Factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: int):
        self.nombre = nombre
        self.cedula = cedula
        self.pedidos = []  

    def agregarFactura(self, factura: Factura) -> None:
        self.pedidos.append(factura)

    def mostrarHistorial(self):
        for factura in self.pedidos:
            print(factura)

    def __str__(self):
        return f"Nombre: {self.nombre}, Cédula: {self.cedula}, Facturas: {len(self.pedidos)}"
