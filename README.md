# Restaurante App - Optimización con Colecciones (Semana 12)

Evolución del sistema modular `restaurante_app` enfocado en la mejora de rendimiento mediante el uso eficiente de colecciones en memoria.

## Mejoras de Rendimiento Aplicadas

1. **Índices con Diccionarios (`dict`)**:
   - `indice_productos`: Permite la búsqueda directa de productos por su código en tiempo $O(1)$, evitando iterar la lista de productos.
   - `indice_usuarios`: Búsqueda instantánea de usuarios por su número de identificación en tiempo $O(1)$.
   - `indice_ventas_usuario`: Agrupa las ventas asociadas a cada usuario en un diccionario (`dict[str, list]`), reduciendo el costo de consulta sin necesidad de filtrar toda la colección de ventas.

2. **Validación de Unicidad con Conjuntos (`set`)**:
   - `codigos_productos_set`: Utilizado para la comprobación rápida de existencia de códigos al momento de registrar nuevos productos.

3. **Sincronización y Reconstrucción Automática**:
   - Al iniciar la aplicación, los datos cargados desde las fuentes `.json` pasan por el método `reconstruir_indices()`, asegurando coherencia.
   - Cada inserción o modificación actualiza dinámicamente las listas y los índices en memoria antes de persistir a los archivos.
