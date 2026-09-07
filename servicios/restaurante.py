from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        # Colecciones principales (Listas para ordenamiento, iteración y persistencia)
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []

        # Estructuras auxiliares e Índices en Memoria para optimización (O(1))
        self.indice_productos: dict[str, Producto] = {}        # Clave: codigo -> Producto
        self.indice_usuarios: dict[str, Usuario] = {}          # Clave: identificacion -> Usuario
        self.indice_ventas_usuario: dict[str, list[Venta]] = {} # Clave: id_usuario -> Lista de Ventas
        self.codigos_productos_set: set[str] = set()           # Set para validaciones instantáneas de pertenencia

        # Cargar datos al iniciar y construir índices
        self.cargar_datos()

    def reconstruir_indices(self):
        """Reconstruye todos los índices auxiliares en memoria a partir de las listas principales."""
        self.indice_productos = {p.codigo: p for p in self.productos}
        self.indice_usuarios = {u.identificacion: u for u in self.usuarios}
        self.codigos_productos_set = {p.codigo for p in self.productos}
        
        self.indice_ventas_usuario = {}
        for v in self.ventas:
            if v.id_usuario not in self.indice_ventas_usuario:
                self.indice_ventas_usuario[v.id_usuario] = []
            self.indice_ventas_usuario[v.id_usuario].append(v)

    def guardar_datos(self):
        """Persiste la información en archivos JSON."""
        ArchivoServicio.guardar_json("datos/productos.json", [p.a_diccionario() for p in self.productos])
        ArchivoServicio.guardar_json("datos/usuarios.json", [u.a_diccionario() for u in self.usuarios])
        ArchivoServicio.guardar_json("datos/ventas.json", [v.a_diccionario() for v in self.ventas])

    def cargar_datos(self):
        """Carga objetos desde JSON y ejecuta la reconstrucción de índices."""
        raw_p = ArchivoServicio.cargar_json("datos/productos.json")
        self.productos = [Producto.desde_diccionario(p) for p in raw_p]

        raw_u = ArchivoServicio.cargar_json("datos/usuarios.json")
        self.usuarios = [Usuario.desde_diccionario(u) for u in raw_u]

        raw_v = ArchivoServicio.cargar_json("datos/ventas.json")
        self.ventas = [Venta.desde_diccionario(v) for v in raw_v]

        self.reconstruir_indices()

    # --- REGISTROS Y MANTENIMIENTO DE ÍNDICES ---

    def registrar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self.codigos_productos_set:  # Búsqueda O(1) con Set
            return False
        
        self.productos.append(producto)
        # Sincronización inmediata de índices
        self.indice_productos[producto.codigo] = producto
        self.codigos_productos_set.add(producto.codigo)
        self.guardar_datos()
        return True

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.identificacion in self.indice_usuarios:  # Búsqueda O(1) con Dict
            return False
        
        self.usuarios.append(usuario)
        # Sincronización inmediata de índice
        self.indice_usuarios[usuario.identificacion] = usuario
        self.guardar_datos()
        return True

    # --- BÚSQUEDAS OPTIMIZADAS ---

    def buscar_producto(self, codigo: str) -> Producto | None:
        """Búsqueda directa O(1) evitando recorrer la lista."""
        return self.indice_productos.get(codigo)

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        """Búsqueda directa O(1) evitando recorrer la lista."""
        return self.indice_usuarios.get(identificacion)

    def consultar_ventas_por_usuario(self, identificacion: str) -> list[Venta]:
        """Consulta O(1) agrupada por usuario sin recorrer todas las ventas."""
        return self.indice_ventas_usuario.get(identificacion, [])

    # --- LÓGICA DE NEGOCIO ---

    def registrar_venta(self, id_venta: str, id_usuario: str, codigo_producto: str, cantidad: int) -> tuple[bool, str]:
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            return False, "Usuario no encontrado."

        producto = self.buscar_producto(codigo_producto)
        if not producto:
            return False, "Producto no encontrado."

        if producto.stock < cantidad:
            return False, f"Stock insuficiente. Disponible: {producto.stock}"

        # Actualizar stock
        producto.stock -= cantidad
        total = producto.precio * cantidad

        # Crear y almacenar venta
        nueva_venta = Venta(id_venta, id_usuario, codigo_producto, cantidad, total)
        self.ventas.append(nueva_venta)

        # Sincronizar índice agrupado de ventas por usuario
        if id_usuario not in self.indice_ventas_usuario:
            self.indice_ventas_usuario[id_usuario] = []
        self.indice_ventas_usuario[id_usuario].append(nueva_venta)

        self.guardar_datos()
        return True, "Venta registrada con éxito."