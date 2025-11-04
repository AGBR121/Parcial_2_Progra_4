from datetime import date
from modelo.Producto import Producto

class Factura:
    def __init__(self, fecha: date, cliente):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = []
        self.total = 0.0

    def agregarProducto(self, producto: Producto) -> None:
        self.productos.append(producto)
        self.total = self.calcular_total()

    def calcular_total(self) -> float:
        self.total = sum(p.valor for p in self.productos)
        return self.total

    def __str__(self):
        nombres = [p.nombre for p in self.productos]
        return (f"Factura del {self.fecha} para {self.cliente.nombre}, "
            f"productos: {nombres}, total pagado: {self.total}")
