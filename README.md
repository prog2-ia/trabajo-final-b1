[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)
# Marketplace

Simulador de mercado. Permite gestionar un catálogo de productos y negociar precios con vendedores que poseen personalidades diferentes. 

Al iniciar, el sistema carga los productos de sesiones anteriores. Puedes vender productos nuevos, comprarlos mediante regateo o gestionar tus publicaciones. **Al finalizar, el sistema genera facturas y registros detallados en la carpeta `almacen`.**

## Características
* **Jerarquía de Clases:** Categorías de Electrónica, Ropa, Hogar y Deportes.
* **Vendedores con personalidades:** Tipos **Tacaño**, **Normal** y **Desesperado** con estrategias de negociación y frases únicas.
* **Gestión de Ficheros (Persistencia):** * **Inventario:** Los productos se guardan en `inventario.txt`, manteniendo un rastro separado por cada ejecución mediante marcas visuales.
    * **Historial de Ventas:** Registro acumulativo de todas las transacciones en `historial_ventas.txt`.
    * **Facturación:** Generación automática de archivos `.txt` y `.pkl` individuales por cada compra realizada.
* **Negociación Persistente:** Bucle de regateo activo hasta cerrar el trato o cancelar la oferta.
* **Encapsulamiento y Excepciones:** Protección de precios mediante miembros privados y gestión de errores personalizados (ID no encontrado, errores de validación, etc.).

## Estructura del Proyecto
El proyecto está organizado en paquetes para una mayor modularidad:

* **`datos/`**: Contiene las definiciones de `vendedor.py`, `producto.py`, `subproductos.py` y las diferentes lógicas de los vendedores (`desesperado.py`, `normal.py`, `tacanyo.py`).
* **`logica/`**: 
    * `marketplace.py`: Gestión del inventario en memoria.
    * `persistencias.py`: Motor de manejo de ficheros de texto y binarios.
    * `excepciones.py`: Definición de errores personalizados.
* **`interfazcarp/`**: Contiene todos los archivos de la interfaz, incluyendo `interfaz.py` para el manejo de menús y mensajes.
* **`almacen/`**: Carpeta de destino de todos los archivos generados (Facturas, Inventario y Logs).
* **`mainpro.py`**: Punto de entrada que coordina la carga inicial y el bucle principal.

## Cómo ejecutar el programa
1. **Instalación:** Para instalar las dependencias, ejecuta:
```bash
pip install -r requirements.txt
```
2. **Ejecución:** Inicia el Marketplace desde la terminal:
```bash
python mainpro.py
```
## Notas sobre el Sistema de Archivos
**Separación por Ejecución:** Cada vez que inicies el programa, verás una marca en inventario.txt e historial_ventas.txt que indica el inicio de una "NUEVA SESIÓN", permitiendo conservar y distinguir los datos antiguos de los nuevos.

**Facturas:** Las facturas se generan con el nombre factura_ID.txt. Si se realiza una compra con un ID que ya existía en una sesión anterior, el archivo se actualizará con los nuevos datos.
