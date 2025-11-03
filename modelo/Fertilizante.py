from ProductoControl import ProductoControl

from datetime import date

class Fertilizante(ProductoControl):
    def __init__(self, nombre: str, valor: float, registroICA: str,
                 frecuenciaAplicacion: str, fechaUltimaAplicacion: date):
        super().__init__(nombre, valor, registroICA, frecuenciaAplicacion)
        if not isinstance(fechaUltimaAplicacion, date):
            raise TypeError("La fecha de última aplicación debe ser un objeto date.")
        self.fechaUltimaAplicacion = fechaUltimaAplicacion
