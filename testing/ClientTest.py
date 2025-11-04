import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import date
from modelo.Cliente import Cliente
from modelo.Factura import Factura
from modelo.Antibiotico import Antibiotico

print("===== INICIO TEST CLIENTE =====")

def test_historial_cliente():
    # Preparar datos
    cliente = Cliente("Carlos Ramírez", 123456789)
    factura1 = Factura(date(2025, 11, 1), cliente)
    factura2 = Factura(date(2025, 11, 3), cliente)

    producto_1 = Antibiotico("Penicilina", 48000, 500, "Porcino")
    producto_2 = Antibiotico("TetraVet", 52000, 550, "Bovino")
    producto_3 = Antibiotico("Acetaminofen", 55000, 550, "Bovino")

    # Agregar productos a las facturas
    factura1.agregarProducto(producto_1)
    factura1.agregarProducto(producto_3)
    factura2.agregarProducto(producto_2)

    # Validar contenido
    assert factura1.productos[0].nombre == "Penicilina"
    assert factura1.productos[1].nombre == "Acetaminofen"
    assert factura2.productos[0].nombre == "TetraVet"

    # Asociar facturas al cliente
    cliente.agregarFactura(factura1)
    cliente.agregarFactura(factura2)

    # Validar relaciones
    assert len(cliente.pedidos) == 2
    assert len(factura1.productos) == 2
    assert len(factura2.productos) == 1

    # Calcular totales
    total1 = factura1.calcular_total()
    total2 = factura2.calcular_total()
    assert total1 == 103000
    assert total2 == 52000

    # Mostrar resultados
    print("\nHistorial de facturas del cliente:")
    cliente.mostrarHistorial()

    print("\nComposición del cliente -> facturas -> productos:")
    for f in cliente.pedidos:
        print(f"Factura ({f.fecha}) contiene {len(f.productos)} productos:")
        for p in f.productos:
            print("   →", p)

if __name__ == "__main__":
    test_historial_cliente()
    print("===== FIN TEST CLIENTE =====")