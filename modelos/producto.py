# Clase que representa un producto del restaurante

class Producto:
    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        disponible: bool
    ):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )