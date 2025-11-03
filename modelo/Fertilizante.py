from ProductoControl import ProductoControl

class Fertilizante(ProductoControl):
    def __init__(self, nombre: str, valor: float, registroICA: str, 
                 frecuenciaAplicacion: str, fechaUltimaAplicacion: str):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        self.fechaUltimaAplicacion = fechaUltimaAplicacion
