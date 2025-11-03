from Producto import Producto

class ProductoControl(Producto):
    def __init__(self, nombre: str, valor: float, registroICA: str, frecuenciaAplicacion: str):
        super().__init__(nombre, valor)
        self.registroICA = registroICA
        self.frecuenciaAplicacion = frecuenciaAplicacion
