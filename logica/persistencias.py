from datos.subproductos import Electronica, Ropa, Hogar, Deportes
from datos.tacanyo import Tacanyo
from datos.normal import Normal
from datos.desesperado import Desesperado
from logica.excepciones import MarketplaceError


class GestorDatos:
    FILE_INVENTARIO = "almacen/inventario.txt"
    FILE_HISTORIAL = "almacen/historial_ventas.txt"

    @classmethod
    def guardar_inventario(cls, lista_productos): #Funcion para guardar el inventario actual de la tienda.
        """Usa el modo 'w' para sobrescribir el catálogo actual."""
        try:
            with open(cls.FILE_INVENTARIO, "w", encoding="utf-8") as f:
                for p in lista_productos:
                    # Formato: ID|Nombre|Precio|Vendedor|TipoVendedor|Categoria
                    tipo_v = p.vendedor.__class__.__name__
                    cat = p.__class__.__name__
                    linea = f"{p.id_prod}|{p.nombre}|{p.precio}|{p.vendedor.nombre}|{tipo_v}|{cat}\n"
                    f.write(linea)
        except Exception as e:
            print(f"[!] Error al escribir en el fichero: {e}")

    @classmethod
    def cargar_inventario(cls, mercado_obj): #Funcion para cagar el inventario de la tienda.
        """Usa el modo 'r' para leer y reconstruir los objetos."""
        try:
            with open(cls.FILE_INVENTARIO, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split("|")
                    if len(datos) < 6: continue

                    id_p, nom, precio, v_nom, v_tipo, p_cat = datos

                    # 1. Recrear Vendedor
                    if v_tipo == "Tacanyo":
                        v = Tacanyo(v_nom)
                    elif v_tipo == "Desesperado":
                        v = Desesperado(v_nom)
                    else:
                        v = Normal(v_nom)

                    # 2. Recrear Producto según categoría
                    if p_cat == "Electronica":
                        nuevo = Electronica(int(id_p), nom, float(precio), v)
                    elif p_cat == "Ropa":
                        nuevo = Ropa(int(id_p), nom, float(precio), v)
                    elif p_cat == "Hogar":
                        nuevo = Hogar(int(id_p), nom, float(precio), v)
                    else:
                        nuevo = Deportes(int(id_p), nom, float(precio), v)

                    # 3. Meter en el inventario (usando el += que definiste)
                    mercado_obj += nuevo
                    # Ajustar el contador para que los nuevos IDs no choquen
                    if int(id_p) >= mercado_obj.contador_ids:
                        mercado_obj.contador_ids = int(id_p) + 1
        except FileNotFoundError:
            # Si no existe, no pasa nada, el programa inicia vacío o con los de defecto
            pass

    @classmethod
    def generar_factura(cls, producto, precio_final): #Generamos una factura de los productos comprados a lo largo de la sesion que se ejecuta al finalizar.
        """Crea factura (modo 'w') y actualiza el historial (modo 'a')."""
        ruta_fac = f"almacen/factura_{producto.id_prod}.txt"

        # 1. Crear la factura individual (Sobrescribe si el ID se repite)
        with open(ruta_fac, "w", encoding="utf-8") as f:
            f.write("********** FACTURA **********\n")
            f.write(f"ID Producto: {producto.id_prod}\n")
            f.write(f"Nombre: {producto.nombre}\n")
            f.write(f"Vendedor: {producto.vendedor.nombre}\n")
            f.write(f"Precio pagado: {precio_final}€\n")
            f.write("*****************************\n")

        # 2. Anexar al historial global (No borra lo anterior)
        with open(cls.FILE_HISTORIAL, "a", encoding="utf-8") as f:
            f.write(f"VENTA: {producto.nombre} | Precio: {precio_final}€ | Vendedor: {producto.vendedor.nombre}\n")