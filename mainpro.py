from interfazcarp import interfaz
from logica.marketplace import Marketplace
from datos.desesperado import Desesperado
from datos.normal import Normal
from datos.tacanyo import Tacanyo
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
import random


def app(): #Funcion principal
    mercado = Marketplace()

    while True:
        opc = interfaz.mostrar_menu()

        if opc == "1":  # Si se selecciona la opcion 1 mostrar el catalogo.
            # --- AÑADIDO: VALIDACIÓN CATÁLOGO VACÍO ---
            if not mercado._inventario:
                print("\n[!] El catálogo está vacío. Prueba a vender un producto para luego poder comprarlo.") #Por si el catálogo está vacío
            else:
                for p in mercado._inventario: print(p)

        elif opc == "2": #Si se selecciona la opcion 2 se vende un producto.
            n, p, v_nom, cat = interfaz.pedir_datos_venta()
            # Seleccion de personalidad
            clase_v = random.choice([Desesperado, Normal, Tacanyo])
            v = clase_v(v_nom)
            print(f"*** Parece que el vendedor ha salido {clase_v.__name__} ***")

            if cat == "1": #En funcion de la opcion se crea un tipo u otro de producto
                nuevo = Electronica(mercado.contador_ids, n, p, v)
            elif cat == "2":
                nuevo = Ropa(mercado.contador_ids, n, p, v)
            elif cat == "3":
                nuevo = Hogar(mercado.contador_ids, n, p, v)
            else:
                nuevo = Deportes(mercado.contador_ids, n, p, v)

            mercado.vender_producto(nuevo)

        elif opc == "3": #Opcion 3 para comprar un producto ya subido.
            id_p = int(input("ID del producto a negociar: "))
            prod = mercado.buscar_producto(id_p)

            if prod:
                # Negociacion
                negociando = True #Negociacion con el vendedor por el producto hasta que se venda o cancele.
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

        elif opc == "4": #Opcion 4 para salir.
            break


if __name__ == "__main__":
    app()