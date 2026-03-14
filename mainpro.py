from datos import *
from logica import Marketplace
import interfaz
import random


def app():
    mercado = Marketplace()

    while True:
        opc = interfaz.mostrar_menu()

        if opc == "1":
            for p in mercado._inventario: print(p)

        elif opc == "2":
            n, p, v_nom, cat = interfaz.pedir_datos_venta()
            # Seleccion de personalidad
            clase_v = random.choice([Desesperado, Normal, Tacanyo])
            v = clase_v(v_nom)
            print(f"*** Parece que el vendedor ha salido {clase_v.__name__} ***")

            if cat == "1":
                nuevo = Electronica(mercado.contador_ids, n, p, v)
            elif cat == "2":
                nuevo = Ropa(mercado.contador_ids, n, p, v)
            elif cat == "3":
                nuevo = Hogar(mercado.contador_ids, n, p, v)
            else:
                nuevo = Deportes(mercado.contador_ids, n, p, v)

            mercado.vender_producto(nuevo)

        elif opc == "3":
            id_p = int(input("ID del producto a negociar: "))
            prod = mercado.buscar_producto(id_p)

            if prod:
                # Negociacion
                negociando = True
                while negociando:
                    oferta = float(input(f"Introduce tu oferta para {prod.nombre} (0 para cancelar): "))
                    if oferta == 0:
                        negociando = False
                        continue

                    res, val = prod.vendedor.negociar(prod.precio, oferta)
                    interfaz.mostrar_resultado_negociacion(res, val, prod)

                    if res == "ACEPTADA":
                        mercado.comprar_final(id_p)
                        negociando = False
            else:
                print("ID no encontrado.")

        elif opc == "4":
            break


if __name__ == "__main__":
    app()