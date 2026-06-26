
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Creación del restaurante
restaurante_principal = Restaurante("El rincón del sabor")

# Creación de los productos
producto_1 = Producto(
    "Patacones con camarones apanados",
    "Plato a la carta",
    8.50,
    True
)

producto_2 = Producto(
    "Jugo de maracuyá",
    "Bebida",
    3.00,
    False
)

# Creación de los clientes
cliente_1 = Cliente(
    "Vicente Alban",
    33,
    "vi_alban@hotmail.com",
    True
)

cliente_2 = Cliente(
    "Maria Macias",
    54,
    "ma_macias@gmail.com",
    False
)

# Agregar productos al restaurante
restaurante_principal.agregar_producto(producto_1)
restaurante_principal.agregar_producto(producto_2)

# Agregar clientes al restaurante
restaurante_principal.agregar_cliente(cliente_1)
restaurante_principal.agregar_cliente(cliente_2)

# Mostrar información registrada
print("=================================")
print(f"RESTAURANTE: {restaurante_principal.nombre}")
print("=================================")

restaurante_principal.mostrar_productos()
restaurante_principal.mostrar_clientes()