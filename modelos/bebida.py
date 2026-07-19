"""
Clase Bebida
"""
from modelos.producto import Producto


class Bebida(Producto):
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        envase: str,
    ) -> None:

        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = tamano
        self.envase = envase

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Bebida: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Tamaño: {self.tamano} | "
            f"Envase: {self.envase}"
        )