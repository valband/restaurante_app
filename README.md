Nombre
Vicente Alban Defilippi

Descripción del sistema
Este proyecto consiste en un sistema básico de gestión de un restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). 
El sistema permite registrar productos y clientes, almacenarlos mediante listas y administrarlos desde una clase de servicio denominada Restaurante. 
Su finalidad es demostrar el uso correcto de clases, objetos, constructores, importaciones entre módulos, tipos de datos básicos e identificadores descriptivos dentro de un proyecto organizado de forma modular.

Estructura del proyecto
restaurante_app/
│
├── modelos/
│   ├── _init_.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── _init_.py
│   └── restaurante.py
│
├── main.py
└── README.md

Breve explicación
modelos/: contiene las clases que representan las entidades principales del sistema.
producto.py: define la clase Producto, utilizada para representar los productos disponibles en el restaurante.
cliente.py: define la clase Cliente, utilizada para almacenar la información de los clientes registrados.
servicios/: contiene la lógica principal del sistema.
restaurante.py: implementa la clase Restaurante, encargada de administrar las listas de productos y clientes mediante distintos métodos.
main.py: es el punto de inicio del programa. En este archivo se crean los objetos, se registran dentro del restaurante y finalmente se muestra toda la información almacenada en la consola.

Tipos de datos utilizados
str =	Nombre del producto, categoría, nombre del cliente y correo electrónico.
int	= Edad del cliente.
float	= Precio de los productos del restaurante.
bool	= Estado de disponibilidad del producto y condición de cliente frecuente.
list	= Almacenamiento de múltiples productos y clientes dentro de la clase Restaurante.

Reflexión
El uso de identificadores descriptivos facilita la lectura y comprensión del código, permitiendo reconocer rápidamente la función de cada clase, atributo y método. 
Asimismo, seleccionar tipos de datos adecuados ayuda a representar correctamente la información y reduce la posibilidad de errores durante la ejecución del programa. 
Finalmente, el empleo de listas dentro de una estructura modular permite organizar los objetos de forma eficiente, favoreciendo un código más ordenado, reutilizable y sencillo de mantener conforme el proyecto crece.
