from ProductoControl import ProductoControl

class ControlPlaga(ProductoControl):
    def __init__(self, nombre: str, valor: float, registroICA: str, 
                 frecuenciaAplicacion: str, periodoCarencia: str):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        self.periodoCarencia = periodoCarencia
