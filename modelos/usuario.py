class Usuario:
    def __init__(self, identificacion: str, nombre: str, rol: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.rol = rol

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            rol=datos["rol"]
        )