from modelo.Producto import Producto

class ProductoControl(Producto):
    def __init__(self, nombre: str, valor: float, registroICA: str, frecuenciaAplicacion: str):
        super().__init__(nombre, valor)
        self.registroICA = registroICA
        self.frecuenciaAplicacion = frecuenciaAplicacion

    def __str__(self):
        return (f"{self.nombre} (ICA: {self.registroICA}, "
            f"Frecuencia: {self.frecuenciaAplicacion}) - ${self.valor}")
