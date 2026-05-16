import pickle  # Para el manejo de ficheros binarios
import os  # Para comprobar existencia y eliminar físicamente

# Todos los imports de datos agrupados al principio de forma limpia
from datos.tacanyo import Tacanyo
from datos.normal import Normal
from datos.desesperado import Desesperado
from datos.subproductos import Electronica, Ropa, Hogar, Deportes


class GestorDatos:
    FILE_INVENTARIO = "almacen/inventario.txt"
    FILE_HISTORIAL = "almacen/historial_ventas.txt"

    @classmethod
    def limpiar_sesion_anterior(cls):
        """
        Busca y elimina físicamente los archivos de facturas (.txt y .pickle)
        para que la carpeta 'almacen' empiece completamente limpia.
        """
        for i in range(1, 20):  # Escanea un rango razonable de posibles IDs
            ruta_txt = f"almacen/factura_{i}.txt"
            ruta_pickle = f"almacen/factura_{i}.pickle"

            if os.path.exists(ruta_txt):  # Comprueba si existe el archivo de texto (Pág. 19)
                os.remove(ruta_txt)  # Lo elimina físicamente (Pág. 27)
            if os.path.exists(ruta_pickle):  # Comprueba si existe el binario (Pág. 19)
                os.remove(ruta_pickle)  # Lo elimina físicamente (Pág. 27)

    @classmethod
    def guardar_inventario(cls, mercado):
        """
        EJEMPLO TEXTO PLANO ('w'): Sobrescribe el archivo para que
        siempre muestre el último estado real del inventario (la foto actual).
        """
        try:
            with open(cls.FILE_INVENTARIO, "w", encoding="utf-8") as f:
                for p in mercado:
                    tipo_v = p.vendedor.__class__.__name__
                    cat = p.__class__.__name__
                    linea = f"{p.id_prod}|{p.nombre}|{p.precio}|{p.vendedor.nombre}|{tipo_v}|{cat}\n"
                    f.write(linea)
        except Exception as e:
            print(f"[!] Error al actualizar inventario de texto: {e}")

    @classmethod
    def cargar_inventario(cls, mercado):
        """EJEMPLO TEXTO PLANO ('r'): Lee el archivo de texto al arrancar."""
        try:
            with open(cls.FILE_INVENTARIO, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split("|")
                    if len(datos) < 6: continue

                    id_p, nom, precio, v_nom, v_tipo, p_cat = datos

                    if v_tipo == "Tacanyo":
                        v = Tacanyo(v_nom)
                    elif v_tipo == "Desesperado":
                        v = Desesperado(v_nom)
                    else:
                        v = Normal(v_nom)

                    if p_cat == "Electronica":
                        nuevo = Electronica(int(id_p), nom, float(precio), v)
                    elif p_cat == "Ropa":
                        nuevo = Ropa(int(id_p), nom, float(precio), v)
                    elif p_cat == "Hogar":
                        nuevo = Hogar(int(id_p), nom, float(precio), v)
                    else:
                        nuevo = Deportes(int(id_p), nom, float(precio), v)

                    mercado += nuevo
                    if int(id_p) >= mercado.contador_ids:
                        mercado.contador_ids = int(id_p) + 1
        except FileNotFoundError:
            pass

    @classmethod
    def generar_factura(cls, producto, precio_final):
        """
        DEMOSTRACIÓN DOBLE: CREACIÓN DE FICHERO DE TEXTO Y BINARIO.
        """
        # --- 1. FACTURA EN TEXTO PLANO (Modo 'w') ---
        ruta_txt = f"almacen/factura_{producto.id_prod}.txt"
        try:
            with open(ruta_txt, "w", encoding="utf-8") as f_txt:
                f_txt.write("==================================\n")
                f_txt.write("       FACTURA DE COMPRA (TEXTO)  \n")
                f_txt.write("==================================\n")
                f_txt.write(f"ID Producto: {producto.id_prod}\n")
                f_txt.write(f"Artículo:    {producto.nombre}\n")
                f_txt.write(f"Vendedor:    {producto.vendedor.nombre}\n")
                f_txt.write(f"Precio Final: {precio_final}€\n")
                f_txt.write("==================================\n")
        except Exception as e:
            print(f"[!] Error al generar factura de texto: {e}")

        # --- 2. FACTURA EN BINARIO / BYTES WITH PICKLE (Modo 'wb')
        ruta_pickle = f"almacen/factura_{producto.id_prod}.pickle"
        # Estructuramos en un diccionario organizado para evitar fallos de orden
        datos_binarios = {
            'id': producto.id_prod,
            'articulo': producto.nombre,
            'nombre_vendedor': producto.vendedor.nombre,
            'total_pagado': float(precio_final)
        }
        try:
            with open(ruta_pickle, "wb") as f_bin:  # Modo 'wb' para escribir bytes
                pickle.dump(datos_binarios, f_bin)  # Serializa el objeto directamente
        except Exception as e:
            print(f"[!] Error al generar factura binaria pickle: {e}")

        # --- 3. ANEXAR AL HISTORIAL DE VENTAS DE TEXTO (Modo 'a') ---
        try:
            with open(cls.FILE_HISTORIAL, "a", encoding="utf-8") as f_hist:
                f_hist.write(f"VENTA REALIZADA: {producto.nombre} (ID: {producto.id_prod}) | Precio: {precio_final}€\n")
        except Exception as e:
            print(f"[!] Error al escribir en el historial: {e}")