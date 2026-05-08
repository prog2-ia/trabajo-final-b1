import random
from datos.producto import Producto

def mostrar_menu() -> str:
    print("\n--- Marketplace ---")
    print("1. Ver catalogo\n2. Vender producto\n3. Negociar/Comprar\n4. Salir")
    return input("Selección: ")


def pedir_datos_venta() -> tuple:
    print("\n--- PUBLICAR ---")
    n: str = input("Nombre del producto: ")

    # Bucle para el PRECIO (Validación instantánea)
    while True:
        try:
            p_input = input("Precio: ")
            p: float = float(p_input)
            if p <= 0:
                print("[!] Error: El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("[!] Error: Introduce un valor numérico válido.")

    v: str = input("Tu nombre (Vendedor): ")

    # Bucle para la CATEGORÍA (Validación instantánea)
    while True:
        print("Categoría: 1. Electrónica | 2. Ropa | 3. Hogar | 4. Deportes")
        c: str = input("Selecciona una opción (1-4): ")

        if c in ["1", "2", "3", "4"]:
            break  # Opción válida, salimos del bucle
        else:
            print(f"[!] '{c}' no es una opción válida. Por favor, elige un número del 1 al 4.")

    return n, p, v, c

def mostrar_resultado_negociacion(estado: str, valor: float, producto: 'Producto') -> None: #Al negociar definimos las 3 respuestas.

    frase: str = random.choice(producto.vendedor.frases_negociao)
    if estado == "ACEPTADA": #Si se acepta se muestra una frase de aceptación del vendedor y el mensaje de la compra
        print(f"\n¡TRATO HECHO! {producto.vendedor.nombre} dice: '{frase}'")
        print(f"Has comprado {producto.nombre} por {valor}€.")

    elif estado == "CONTRAOFERTA": #Se debate el frase con una contraoferta y una frase.
        print(f"\n{producto.vendedor.nombre} dice: '{frase}'")
        print(f"Me parece poco... ¿Qué tal {valor}€?")

    elif estado == "RECHAZADA": #Se rechaza la compra y acaba la compra con otra frase.
        print(f"\n{producto.vendedor.nombre} dice: '{frase}'")
        print("Oferta rechazada. Intenta subir el precio.")