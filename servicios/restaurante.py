# Clase que administra productos y clientes

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n=== PRODUCTOS REGISTRADOS ===")

        if len(self.productos) == 0:
            print("No existen productos registrados.")
        else:
            for producto in self.productos:
                print(producto)

    def mostrar_clientes(self):
        print("\n=== CLIENTES REGISTRADOS ===")

        if len(self.clientes) == 0:
            print("No existen clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)