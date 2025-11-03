from Producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, valor: float, dosis: float, tipoAnimal: str):
        super().__init__(nombre, valor)
        self.dosis = dosis
        self.tipoAnimal = tipoAnimal
