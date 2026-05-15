from interfazcarp import interfaz
from logica.marketplace import Marketplace
from datos.desesperado import Desesperado
from datos.normal import Normal
from datos.tacanyo import Tacanyo
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
from logica.excepciones import ProductoNoEncontradoError, ErrorValidacionPrecio
from logica.persistencias import GestorDatos
import random


def app() -> None:
    # --- LÓGICA DE REINICIO (Sustituir archivos de 0) ---
    # Abrimos los archivos en modo 'w' y cerramos al instante.
    # Esto los vacía completamente antes de empezar la lógica del programa.
    with open("almacen/inventario.txt", "w", encoding="utf-8") as f:
        pass
    with open("almacen/historial_ventas.txt", "w", encoding="utf-8") as f:
        pass

    print("[SISTEMA] Archivos de la carpeta 'almacen' reiniciados para esta sesión.")

    mercado: Marketplace = Marketplace()

    # Intentamos cargar (aunque en este caso estarán vacíos por el reset de arriba)
    GestorDatos.cargar_inventario(mercado)

    try:
        while True:
            try:
                opc: str = interfaz.mostrar_menu()

                if opc == "1":
                    if not mercado:
                        print("\n[!] El catálogo está vacío.")
                    else:
                        print(f"Artículos disponibles: {len(mercado)}")
                        for p in mercado:
                            print(p)

                elif opc == "2":
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

                    # AVISO QUE PEDISTE
                    print("\n" + "!" * 40)
                    print("[AVISO] Revisa el fichero 'inventario.txt' en la carpeta 'almacen'.")
                    print("!" * 40)


                elif opc == "3":
                    try:
                        id_p_str = input("ID del producto: ")
                        id_p = int(id_p_str)
                        prod = mercado.buscar_producto(id_p)
                        negociando: bool = True

                        while negociando:
                            try:
                                oferta_str = input(f"Oferta por {prod.nombre} (0 para cancelar): ")
                                oferta = float(oferta_str)
                                if oferta == 0: break

                                res, val = prod.vendedor.negociar(prod.precio, oferta)
                                interfaz.mostrar_resultado_negociacion(res, val, prod)

                                if res == "ACEPTADA":
                                    mercado.comprar_final(id_p)
                                    GestorDatos.generar_factura(prod, val)
                                    GestorDatos.guardar_inventario(mercado)

                                    # AVISO QUE PEDISTE
                                    print("\n" + "!" * 40)
                                    print(f"[AVISO] Compra realizada. Revisa la factura y el historial en 'almacen'.")
                                    print("!" * 40)

                                    negociando = False
                            except ValueError:
                                print("[!] Error: Oferta no válida.")

                    except ProductoNoEncontradoError as e:
                        print(f"\n[ERROR] {e}")

                elif opc == "4":
                    # ... (Lógica de gestión igual que antes) ...
                    # No olvides llamar a GestorDatos.guardar_inventario(mercado) tras cambios
                    pass

                elif opc == "5":
                    break

            except Exception as e:
                print(f"\n[ERROR CRÍTICO] {e}")

    except KeyboardInterrupt:
        print("\n\n[!] Ejecución finalizada.")

    finally:
        print("\n" + "=" * 45)
        print("   Sesión terminada. Los archivos se borrarán al iniciar de nuevo.")
        print("=" * 45)


if __name__ == "__main__":
    app()