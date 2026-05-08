from interfazcarp import interfaz
from logica.marketplace import Marketplace
from datos.desesperado import Desesperado
from datos.normal import Normal
from datos.tacanyo import Tacanyo
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
from logica.excepciones import ProductoNoEncontradoError
import random


def app() -> None:
    mercado: Marketplace = Marketplace()

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
                    print(f"\n[OK] {nuevo.nombre} publicado con éxito.")


                elif opc == "3":

                    try:

                        id_p_str = input("ID del producto: ")
                        # Intentamos convertir a número
                        id_p = int(id_p_str)
                        # Si llega aquí, es que es un número. Buscamos el producto.
                        prod = mercado.buscar_producto(id_p)
                        negociando: bool = True

                        while negociando:
                            try:
                                oferta_str = input(f"Oferta por {prod.nombre} (0 para cancelar): ")
                                oferta = float(oferta_str)

                                if oferta < 0:
                                    print("\n[!] ¿Me estás vacilando? Introduce una mejor oferta...")
                                    continue

                                if oferta == 0: break
                                res, val = prod.vendedor.negociar(prod.precio, oferta)
                                interfaz.mostrar_resultado_negociacion(res, val, prod)

                                if res == "ACEPTADA":
                                    mercado.comprar_final(id_p)
                                    negociando = False


                            except ValueError:
                                # Este error salta si pones letras en la OFERTA
                                print("[!] Error: Por favor, introduce un número válido para la oferta.")


                    except ValueError:
                        # Este error salta si pones letras en el ID de la compra
                        print("\n[!] Error: El ID del producto debe ser un número válido.")

                    except ProductoNoEncontradoError as e:
                        print(f"\n[ERROR] {e}")



                elif opc == "4":

                    try:
                        id_p_str = input("ID del producto a gestionar: ")
                        id_p = int(id_p_str)
                        prod = mercado.buscar_producto(id_p)

                        # --- VALIDACIÓN DE DUEÑO ---

                        vendedor_auth = input("Introduce tu nombre de vendedor para identificarte: ")

                        if vendedor_auth.lower() != prod.vendedor.nombre.lower():
                            print(f"\n[!] ACCESO DENEGADO: Solo {prod.vendedor.nombre} puede gestionar este producto.")
                            continue  # Volver al menú principal

                        # Si el nombre coincide, mostramos el submenú

                        sub_opc = interfaz.mostrar_submenu_gestion()

                        if sub_opc == "1":
                            print(f"\nModificando: {prod.nombre} (Vendedor: {prod.vendedor.nombre})")
                            nuevo_nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
                            nuevo_precio_str = input("Nuevo precio (deja vacío para no cambiar): ")

                            if nuevo_nombre:
                                prod.nombre = nuevo_nombre

                            if nuevo_precio_str:
                                try:

                                    p_float = float(nuevo_precio_str)
                                    # Esto disparará el setter de Producto que ya tiene su propia excepción
                                    prod.precio = p_float
                                    print("[*] Precio actualizado.")

                                except (ValueError, ErrorValidacionPrecio) as e:
                                    print(f"[!] Error al cambiar precio: {e}")
                            print("\n[OK] Características actualizadas con éxito.")


                        elif sub_opc == "2":
                            confirmar = input(f"¿Seguro que quieres eliminar '{prod.nombre}'? (s/n): ")

                            if confirmar.lower() == 's':
                                mercado.comprar_final(id_p)
                                print("\n[OK] Producto eliminado correctamente.")

                            else:
                                print("\nEliminación cancelada.")


                        elif sub_opc == "3":
                            continue


                    except ValueError:
                        print("\n[!] Error: El ID debe ser un número válido.")

                    except ProductoNoEncontradoError as e:
                        print(f"\n[ERROR] {e}")

                elif opc == "5":  # Ahora Salir es la opción 5
                    break

                else:
                    print(f"\n[!] '{opc}' no es una opción válida (1-5).")

            except Exception as e:
                print(f"\n[ERROR CRÍTICO INESPERADO] {e}")

    except KeyboardInterrupt:
        # Capturamos el "botón rojo" o Ctrl+C
        print("\n\n[!] Interrupción detectada: Has cerrado el programa de forma repentina.")

    finally:
        # Este mensaje saldrá SIEMPRE, ya sea por opción 4, error o interrupción
        print("\n" + "=" * 45)
        print("   Gracias por usar nuestra plataforma.")
        print("   ¡Esperamos verte pronto por aquí!")
        print("=" * 45)


if __name__ == "__main__":
    app()