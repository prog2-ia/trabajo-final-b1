from interfazcarp import interfaz
from logica.marketplace import Marketplace
from datos.desesperado import Desesperado
from datos.normal import Normal
from datos.tacanyo import Tacanyo
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
from logica.excepciones import ProductoNoEncontradoError, ErrorValidacionPrecio
from logica.persistencias import GestorDatos
import random


def app() -> None: #Liampamos los nuevos archivos creados entre ejecuciones.
    # Sustituir archivos de cero
    with open("almacen/inventario.txt", "w", encoding="utf-8") as f:
        pass
    with open("almacen/historial_ventas.txt", "w", encoding="utf-8") as f:
        pass

    # Eliminamos todas las facturas de la ejecución anterior
    GestorDatos.limpiar_sesion_anterior()

    print("[SISTEMA] Ficheros e historial de 'almacen' eliminados y reiniciados para esta sesión.")

    mercado: Marketplace = Marketplace()

    # Intentamos cargar
    GestorDatos.cargar_inventario(mercado)

    try:
        while True:
            try:
                opc: str = interfaz.mostrar_menu()

                if opc == "1": #Opcion de ver el catalogo.
                    if not mercado:
                        print("\n[!] El catálogo está vacío.")
                    else:
                        print(f"Artículos disponibles: {len(mercado)}")
                        for p in mercado:
                            print(p)

                elif opc == "2": #Opcion de crear un producto para ponerlo a la venta
                    n, p, v_nom, cat = interfaz.pedir_datos_venta()
                    clase_v = random.choice([Desesperado, Normal, Tacanyo])
                    v = clase_v(v_nom)

                    if cat == "1":
                        nuevo = Electronica(mercado.contador_ids, n, p, v)
                    elif cat == "2":
                        nuevo = Ropa(mercado.contador_ids, n, p, v)
                    elif cat == "3":
                        nuevo = Hogar(mercado.contador_ids, n, p, v)
                    else:
                        nuevo = Deportes(mercado.contador_ids, n, p, v)

                    mercado.vender_producto(nuevo)
                    GestorDatos.guardar_inventario(mercado)

                    print("\n" + "!" * 40)
                    print("[AVISO] Revisa el fichero 'inventario.txt' en la carpeta 'almacen'.")
                    print("!" * 40)

                elif opc == "3": # Opcion para comprar un producto
                    try:
                        id_p_str = input("ID del producto: ")
                        id_p = int(id_p_str)

                        # Control de ID negativo al comprar
                        if id_p < 0:
                            print("\n[!] Error: El ID del producto no puede ser un número negativo.")
                            continue

                        prod = mercado.buscar_producto(id_p)
                        negociando: bool = True

                        while negociando: #Funcionamiento de las negociaciones
                            try:
                                oferta_str = input(f"Oferta por {prod.nombre} (0 para cancelar): ")
                                oferta = float(oferta_str)
                                if oferta == 0: break

                                # Control de oferta negativa
                                if oferta < 0:
                                    print("[!] Error: No puedes hacer una oferta económica negativa.")
                                    continue

                                res, val = prod.vendedor.negociar(prod.precio, oferta)
                                interfaz.mostrar_resultado_negociacion(res, val, prod)

                                if res == "ACEPTADA": #Respuesta para cuando es acertada la oferta
                                    mercado.comprar_final(id_p)
                                    GestorDatos.generar_factura(prod, val)
                                    GestorDatos.guardar_inventario(mercado)

                                    print("\n" + "!" * 40)
                                    print(
                                        f"[AVISO] Compra realizada. Se han creado las facturas en la carpeta 'almacen', revísalas al salir del programa junto con el historial de ventas y el inventario.")
                                    print("!" * 40)

                                    negociando = False
                            except ValueError:
                                print("[!] Error: Oferta no válida.")

                    except ProductoNoEncontradoError as e:
                        print(f"\n[ERROR] {e}")
                    except ValueError:
                        print("\n[!] Error: El ID introducido debe ser un número entero.")

                elif opc == "4":
                    # --- GESTIÓN DE PRODUCTOS CON VALIDACIÓN DE IDENTIDAD ---
                    print("\n--- GESTIÓN DE INVENTARIO ---")

                    try:
                        id_p = int(input("Introduce el ID del producto que quieres gestionar: "))

                        # Control de ID negativo
                        if id_p < 0:
                            print("\n[!] Error: El ID del producto no puede ser un número negativo.")
                            continue

                        prod = mercado.buscar_producto(id_p)  # Lanza excepcion si no existe

                        # --- NUEVO: CONTROL DE NOMBRE CON EL VENDEDOR ---
                        tu_nombre = input(f"Para gestionar '{prod.nombre}', introduce tu nombre de vendedor: ").strip()

                        if tu_nombre.lower() != prod.vendedor.nombre.lower():
                            print(
                                f"\n[!] ACCESO DENEGADO: Tú te llamas '{tu_nombre}', pero el dueño de este producto es '{prod.vendedor.nombre}'. No tienes permiso.")
                            continue

                        # Si pasa el control de nombre, se abren las opciones
                        print(f"\n[✓] Identidad confirmada, hola {prod.vendedor.nombre}.")
                        print("[1] Modificar precio del producto")
                        print("[2] Eliminar el producto por completo")
                        sub_opc = input("Selecciona una opción: ")

                        if sub_opc not in ["1", "2"]:
                            print("\n[!] Error: Opción de gestión fuera de rango. Selecciona 1 o 2.")
                            continue

                        if sub_opc == "1": #Opcion para modificar el precio de un producto.
                            nuevo_precio = float(input(f"Nuevo precio para {prod.nombre} (Actual: {prod.precio}€): "))

                            # Excepción para precios negativos
                            if nuevo_precio < 0:
                                print("\n[!] Error: El precio de venta no puede ser negativo.")
                                continue

                            prod.precio = nuevo_precio
                            GestorDatos.guardar_inventario(mercado)
                            print(f"\n[OK] Precio actualizado con éxito en memoria y en 'inventario.txt'.")

                        elif sub_opc == "2": #Opcion para eliminar el producto de venta
                            if hasattr(mercado, 'eliminar_producto'):
                                mercado.eliminar_producto(id_p)
                            else:
                                mercado.comprar_final(id_p)

                            GestorDatos.guardar_inventario(mercado)
                            print(f"\n[OK] Producto con ID {id_p} eliminado correctamente del sistema.")

                    except ProductoNoEncontradoError as e:
                        print(f"\n[ERROR] {e}")
                    except ValueError:
                        print(
                            "\n[!] Error: Tipo de dato no válido. Has introducido texto donde correspondía un número.")

                elif opc == "5": #Opcion para terminar la ejecucion del programa
                    break

                else:
                    print("\n[!] Error: Opción de menú fuera de rango. Selecciona un número del 1 al 5.")

            except Exception as e:
                print(f"\n[ERROR CRÍTICO CONTENIDO] {e}")

    except KeyboardInterrupt:
        print("\n\n[!] Ejecución finalizada por el usuario.")

    finally: #Mensaje final para cuando se termine la ejecucion.
        print("\n" + "=" * 45)
        print("   Sesión terminada. Los archivos se reiniciarán al iniciar de nuevo.")
        print("=" * 45)


if __name__ == "__main__":
    app()