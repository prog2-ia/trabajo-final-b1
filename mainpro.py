from interfazcarp import interfaz
from logica.marketplace import Marketplace
from datos.desesperado import Desesperado
from datos.normal import Normal
from datos.tacanyo import Tacanyo
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
from logica.excepciones import MarketplaceError, ProductoNoEncontradoError
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
                    try:
                        n, p, v_nom, cat = interfaz.pedir_datos_venta()
                        # El tipo de vendedor se elige al azar para el nuevo producto
                        clase_v = random.choice([Desesperado, Normal, Tacanyo])
                        v = clase_v(v_nom)

                        if cat == "1":
                            nuevo = Electronica(mercado.contador_ids, n, p, v)
                        elif cat == "2":
                            nuevo = Ropa(mercado.contador_ids, n, p, v)
                        elif cat == "3":
                            nuevo = Hogar(mercado.contador_ids, n, p, v)
                        elif cat == "4":
                            nuevo = Deportes(mercado.contador_ids, n, p, v)
                        else:
                            # Lanzamos excepción si el usuario pone algo como "9"
                            raise MarketplaceError(f"La categoría '{cat}' no existe.")

                        mercado.vender_producto(nuevo)
                        print("\n[OK] Producto publicado con éxito.")

                    except (ValueError, MarketplaceError) as e:
                        print(f"\n[ERROR de datos] {e}")


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

                                # --- NUEVA VALIDACIÓN DE VACILE ---

                                if oferta < 0:
                                    print("\n[!] ¿Me estás vacilando? Que significa un número negativo...")

                                    continue  # Salta el resto del bucle y vuelve a pedir la oferta

                                if oferta == 0:
                                    break

                                # Si la oferta es positiva, procedemos con la lógica normal

                                res, val = prod.vendedor.negociar(prod.precio, oferta)

                                interfaz.mostrar_resultado_negociacion(res, val, prod)

                                if res == "ACEPTADA":
                                    mercado.comprar_final(id_p)

                                    negociando = False


                            except ValueError:

                                print("[!] Error: La oferta debe ser un número (ej: 12.5).")


                    except (ValueError, ProductoNoEncontradoError) as e:

                        print(f"\n[ERROR] {e}")

                elif opc == "4":
                    # Salida controlada del bucle
                    break

                else:
                    # VALIDACIÓN DE OPCIÓN DE MENÚ
                    print(f"\n[!] '{opc}' no es una opción válida del menú. Intenta con 1, 2, 3 o 4.")

            except Exception as e:
                # Captura de cualquier error no previsto para que el programa no "pete"
                print(f"\n[ERROR CRÍTICO INESPERADO] {e}")

    finally:
        # El bloque finally se ejecuta tanto si haces "break" como si hay un error fatal
        print("\n" + "=" * 45)
        print("   Gracias por usar nuestra plataforma.")
        print("   ¡Esperamos verte pronto por aquí!")
        print("=" * 45)


if __name__ == "__main__":
    app()