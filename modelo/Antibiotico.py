from modelo.Producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, valor: float, dosis: float, tipoAnimal: str):
        super().__init__(nombre, valor)
        if not 400 <= dosis <= 600:
            raise ValueError("La dosis debe estar entre 400 y 600 kg.")
        if tipoAnimal.lower() not in ("bovino", "porcino", "caprino"):
            raise ValueError("El tipo de animal debe ser bovino, porcino o caprino.")
        self.dosis = dosis
        self.tipoAnimal = tipoAnimal.capitalize()
    
    def __str__(self):
        return (f"Antibiótico: {self.nombre} "
            f"(Dosis: {self.dosis} mg, Animal: {self.tipoAnimal}) - ${self.valor}")

