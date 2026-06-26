# Clase que representa a un cliente registrado

class Cliente:
    def __init__(
        self,
        nombre: str,
        edad: int,
        correo: str,
        cliente_frecuente: bool
    ):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.cliente_frecuente = cliente_frecuente

    def __str__(self):
        tipo_cliente = (
            "Frecuente"
            if self.cliente_frecuente
            else "Ocasional"
        )

        return (
            f"Cliente: {self.nombre} | "
            f"Edad: {self.edad} años | "
            f"Correo electrónico: {self.correo} | "
            f"Tipo de cliente: {tipo_cliente}"
        )