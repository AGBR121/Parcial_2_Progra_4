from datetime import date
from Producto import Producto

class Factura:
    def __init__(self, fecha: date, cliente):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = []
        self.total = 0.0

    def agregarProducto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def calcular_total(self) -> float:
        self.total = sum(p.valor for p in self.productos)
        return self.total
