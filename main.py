from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import RestauranteServicio

def menu():
    servicio = RestauranteServicio()

    while True:
        print("\n=== SISTEMA DE GESTIÓN RESTAURANTE ===")
        print("1. Registrar Usuario")
        print("2. Registrar Producto")
        print("3. Buscar Producto por Código")
        print("4. Buscar Usuario por Identificación")
        print("5. Realizar Venta")
        print("6. Consultar Ventas por Usuario")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Identificación: ")
            nombre = input("Nombre: ")
            rol = input("Rol (Cliente/Empleado): ")
            if servicio.registrar_usuario(Usuario(cedula, nombre, rol)):
                print("¡Usuario registrado con éxito!")
            else:
                print("Error: El usuario ya existe.")

        elif opcion == "2":
            codigo = input("Código de producto: ")
            nombre = input("Nombre de producto: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock inicial: "))
            if servicio.registrar_producto(Producto(codigo, nombre, precio, stock)):
                print("¡Producto registrado con éxito!")
            else:
                print("Error: El código de producto ya existe.")

        elif opcion == "3":
            codigo = input("Ingrese el código del producto a buscar: ")
            prod = servicio.buscar_producto(codigo)
            if prod:
                print(f"Producto Encontrado -> Nombre: {prod.nombre} | Precio: ${prod.precio} | Stock: {prod.stock}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            cedula = input("Ingrese la identificación a buscar: ")
            u = servicio.buscar_usuario(cedula)
            if u:
                print(f"Usuario Encontrado -> Nombre: {u.nombre} | Rol: {u.rol}")
            else:
                print("Usuario no encontrado.")

        elif opcion == "5":
            id_v = input("ID Venta: ")
            cedula = input("Identificación del Usuario: ")
            codigo = input("Código del Producto: ")
            cant = int(input("Cantidad: "))
            exito, msg = servicio.registrar_venta(id_v, cedula, codigo, cant)
            print(f"Resultado: {msg}")

        elif opcion == "6":
            cedula = input("Ingrese la identificación del usuario: ")
            ventas = servicio.consultar_ventas_por_usuario(cedula)
            if ventas:
                print(f"Ventas registradas para {cedula}:")
                for v in ventas:
                    print(f"- ID Venta: {v.id_venta} | Producto: {v.codigo_producto} | Cantidad: {v.cantidad} | Total: ${v.total}")
            else:
                print("No se encontraron ventas para este usuario.")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()