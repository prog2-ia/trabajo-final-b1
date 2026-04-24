from interfazcarp import interfaz
from logica.marketplace import Marketplace
from datos.desesperado import Desesperado
from datos.normal import Normal
from datos.tacanyo import Tacanyo
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
import random


def app() -> None:
    mercado: Marketplace = Marketplace()

    while True:
        opc: str = interfaz.mostrar_menu()

        if opc == "1":
            if not mercado:  # T07: Uso de __bool__
                print("\n[!] El catálogo está vacío.")
            else:
                print(f"Artículos disponibles: {len(mercado)}")  # T07: Uso de __len__
                for p in mercado:  # T08: Uso de __getitem__
                    print(p)  # T07: Uso de __str__

        elif opc == "2":
            n, p, v_nom, cat = interfaz.pedir_datos_venta()
            clase_v = random.choice([Desesperado, Normal, Tacanyo])
            v = clase_v(v_nom)

            # Creación de producto según categoría
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
            id_p: int = int(input("ID del producto: "))
            prod = mercado.buscar_producto(id_p)

            if prod:
                negociando: bool = True
                while negociando:
                    oferta: float = float(input(f"Oferta por {prod.nombre} (0 para cancelar): "))
                    if oferta == 0: break

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