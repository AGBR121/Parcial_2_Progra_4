from modelo.Fertilizante import Fertilizante
from modelo.ControlPlaga import ControlPlaga
from modelo.Antibiotico import Antibiotico
from datetime import date

class CRUDProducto:
    def __init__(self):
        self._productos = []

    @property
    def productos(self):
        return self._productos[:]

    def CrearFertilizante(self, nombre: str, valor: float, registro: str, frecuencia: str, fecha_aplicacion: date):
        fertilizante = Fertilizante(nombre, valor, registro, frecuencia, fecha_aplicacion)
        self._productos.append(fertilizante)
        return fertilizante

    def CrearControlPlaga(self, nombre: str, valor: float, registro: str, frecuencia: str, periodo_carencia: str):
        controlPlaga = ControlPlaga(nombre, valor, registro, frecuencia, periodo_carencia)
        self._productos.append(controlPlaga)
        return controlPlaga
    
    def CrearAntibiotico(self, nombre: str, valor: float, dosis: float, tipoAnimal: str):
        antibiotico = Antibiotico(nombre, valor, dosis, tipoAnimal)
        self._productos.append(antibiotico)
        return antibiotico
    
    def ListarProductos(self):
        if not self._productos:
            print("No hay productos de control registrados aún.")
            return 

        print("\n=== PRODUCTOS DE CONTROL REGISTRADOS ===")
        for number, producto in enumerate(self._productos, 1):
            tipo = producto.__class__.__name__
            print(f"{number}. [{tipo}] {producto.nombre} - Valor: ${producto.valor}")
        print("========================================\n")
