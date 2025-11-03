from Factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: int):
        self.nombre = nombre
        self.cedula = cedula
        self.pedidos = []  

    def agregarFactura(self, factura: Factura) -> None:
        self.pedidos.append(factura)

