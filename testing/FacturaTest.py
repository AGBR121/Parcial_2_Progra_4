from datetime import date
from modelo.Cliente import Cliente
from modelo.Factura import Factura
from modelo.Antibiotico import Antibiotico
from modelo.Fertilizante import Fertilizante
from modelo.ControlPlaga import ControlPlaga


print("===== INICIO TEST FACTURA =====")

def test_factura_composicion_y_total():
    cliente = Cliente("Laura Gómez", 987654321)

    factura = Factura(date(2025, 11, 3), cliente)

    antibiotico = Antibiotico("Amoxivet", 48000, 500, "Porcino")
    fertilizante = Fertilizante("AgroVida", 40000, "ICA-F-1010", "Cada 30 días", date(2025, 10, 20))
    control_plaga = ControlPlaga("Cyperkill", 32000, "ICA-C-8899", "Cada 15 días", "10 días")

    factura.agregarProducto(antibiotico)
    factura.agregarProducto(fertilizante)
    factura.agregarProducto(control_plaga)

    
    total = factura.calcular_total()

    
    assert len(factura.productos) == 3, "La factura debe contener 3 productos."
    assert total == 120000, f"El total esperado es 120000, pero fue {total}"

    print("\nFactura generada correctamente:")
    print(factura)
    print(f"Cliente asociado: {factura.cliente.nombre}")
    print("Productos incluidos en la factura:")

    for productos in factura.productos:
        print("   →", productos)

    print("\nComposición de objetos:")
    print(f"Factura del {factura.fecha} contiene {len(factura.productos)} productos:")
    for producto in factura.productos:
        print(f"   Tipo: {producto.__class__.__name__} - {producto}")

if __name__ == "__main__":
    test_factura_composicion_y_total()
    print("===== FIN TEST FACTURA =====")