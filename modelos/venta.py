class Venta:
    def __init__(self, id_venta: str, id_usuario: str, codigo_producto: str, cantidad: int, total: float):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.total = total

    def a_diccionario(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            id_venta=datos["id_venta"],
            id_usuario=datos["id_usuario"],
            codigo_producto=datos["codigo_producto"],
            cantidad=datos["cantidad"],
            total=datos["total"]
        )