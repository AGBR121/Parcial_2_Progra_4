from modelo.ProductoControl import ProductoControl

class ControlPlaga(ProductoControl):
    def __init__(self, nombre: str, valor: float, registroICA: str, 
                 frecuenciaAplicacion: str, periodoCarencia: str):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        self.periodoCarencia = periodoCarencia

    def __str__(self):
        return (f"Control de plagas: {self.nombre} "
            f"(Carencia: {self.periodoCarencia}, "
            f"Frecuencia: {self.frecuenciaAplicacion}) - ${self.valor}")
