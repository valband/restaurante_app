"""
Archivo principal de la app.
"""

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def registrar_producto(restaurante: Restaurante) -> None:

    print("\nREGISTRAR PRODUCTO")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))

    producto = Producto(codigo, nombre, categoria, precio)

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Ya existe un producto con ese código.")


def registrar_bebida(restaurante: Restaurante) -> None:

    print("\nREGISTRAR BEBIDA")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    tamano = input("Tamaño: ")
    envase = input("Tipo de envase: ")

    bebida = Bebida(
        codigo,
        nombre,
        categoria,
        precio,
        tamano,
        envase,
    )

    if restaurante.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
    else:
        print("Ya existe un producto con ese código.")


def registrar_cliente(restaurante: Restaurante) -> None:

    print("\nREGISTRAR CLIENTE")

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    cliente = Cliente(identificacion, nombre, correo)

    if restaurante.registrar_cliente(cliente):
        print("Cliente registrado correctamente.")
    else:
        print("Ya existe un cliente con esa identificación.")


def mostrar_menu() -> None:

    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def main() -> None:

    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            registrar_bebida(restaurante)

        elif opcion == "3":
            registrar_cliente(restaurante)

        elif opcion == "4":
            restaurante.listar_productos()

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()