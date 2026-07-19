Sistema de Restaurante

Nombre
Vicente Alban Defilippi

Descripción del sistema

Este proyecto consiste en un sistema básico para la gestión de productos, bebidas y clientes de un restaurante. 
El programa permite registrar información mediante un menú interactivo y posteriormente consultar los productos y clientes almacenados.
El sistema fue desarrollado en Python utilizando programación orientada a objetos. 
Además, se aplican conceptos como herencia, polimorfismo y algunos principios SOLID para mantener una estructura organizada, clara y fácil de ampliar.

Estructura del proyecto

```text
restaurante_app/
│
├── main.py
├── README.md
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
└── servicios/
    ├── __init__.py
    └── restaurante.py

Responsabilidad de cada clase y archivo
Producto
La clase "Producto" representa un producto general del restaurante.
Contiene los datos comunes de los productos, como el código, nombre, categoría y precio.
También define el método mostrar_informacion(), utilizado para mostrar los datos del producto.

Bebida
La clase "Bebida" hereda de la clase Producto.
Además de utilizar los atributos generales de un producto, incorpora información propia de una bebida, como el tamaño y el tipo de envase.
La clase también sobrescribe el método mostrar_informacion() para mostrar sus datos específicos.

Cliente
La clase "Cliente" representa la información básica de un cliente registrado.
Sus atributos principales son la identificación, el nombre y el correo electrónico.
Su responsabilidad se limita a representar los datos y mostrar la información del cliente.

Restaurante
La clase "Restaurante" se encarga de administrar las colecciones de productos y clientes.
Entre sus responsabilidades se encuentran registrar productos, registrar clientes, validar códigos de productos repetidos, validar identificaciones duplicadas y listar la información almacenada.
La clase "Restaurante" no necesita mantener una lista separada para las bebidas, ya que estas pueden almacenarse dentro de la misma lista de productos.

main.py
El archivo main.py es el punto de entrada del programa.
Se encarga de mostrar el menú, solicitar los datos mediante input(), crear los objetos correspondientes y llamar a los métodos de la clase Restaurante.
La administración directa de las listas se mantiene fuera de este archivo para conservar una mejor separación de responsabilidades.

Relación entre Producto y Bebida
Existe una relación de herencia entre las clases "Producto" y "Bebida".
La clase Producto funciona como clase base porque contiene las características comunes de los productos del restaurante.
La clase "Bebida" es una clase especializada que hereda esas características y agrega información específica, como el tamaño y el tipo de envase.
Gracias a esta relación, una instancia de Bebida puede ser tratada como un Producto.
Por esta razón, tanto los productos generales como las bebidas pueden almacenarse en una misma colección.
Durante el listado, el sistema ejecuta el método común mostrar_informacion() sin tener que preguntar si el objeto es un producto o una bebida.
Cada clase se encarga de mostrar la información correspondiente a su propia implementación. Esto demuestra el uso del polimorfismo.

Principios SOLID aplicados

SRP - Principio de Responsabilidad Única

Cada clase tiene una responsabilidad específica:
Producto representa productos generales.
Bebida representa una especialización de producto.
Cliente representa los datos de un cliente.
Restaurante administra las colecciones y operaciones del sistema.
main.py coordina la interacción con el usuario.
Esta separación evita que una sola clase concentre demasiadas responsabilidades.

OCP - Principio Abierto/Cerrado

El sistema puede ampliarse mediante nuevas clases derivadas de Producto sin tener que modificar la lógica general de registro y listado del servicio.
Por ejemplo, podría agregarse en el futuro una clase como Postre heredando de Producto.
Esta nueva clase podría sobrescribir mostrar_informacion() y utilizarse dentro de la misma colección de productos.

LSP - Principio de Sustitución de Liskov
Una instancia de Bebida puede utilizarse en cualquier lugar donde se espera un objeto Producto, sin provocar errores.
Por ejemplo, el método registrar_producto() puede recibir tanto un objeto Producto como un objeto Bebida, porque Bebida mantiene la relación y el comportamiento esperado de la clase base.

Reflexión
Diseñar proyectos mantenibles es importante porque un programa no solo debe funcionar en el momento de su creación, sino que también debe poder modificarse y ampliarse en el futuro.
Cuando las responsabilidades están bien separadas, resulta más sencillo encontrar errores, agregar nuevas funcionalidades y comprender el código.
En este proyecto, la separación entre modelos, servicios y la interacción con el usuario permite que cada parte tenga una función clara. Además, el uso de herencia y polimorfismo evita repetir lógica innecesariamente. Considero que aplicar estos principios desde proyectos pequeños ayuda a desarrollar mejores hábitos de programación y facilita la creación de sistemas más ordenados y sostenibles.
