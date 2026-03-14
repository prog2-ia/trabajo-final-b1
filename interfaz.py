import random

def mostrar_menu():
    print("\n--- Marketplace ---")
    print("1. Ver catalogo\n 2. Vender producto\n 3. Negociar/Comprar\n 4. Salir")
    return input("Selección: ")

def pedir_datos_venta():
    print("\n--- PUBLICAR ---")
    n = input("Nombre: ")
    p = float(input("Precio: "))
    v = input("Tu nombre: ")
    print("Categoria: 1. Electronica | 2. Ropa | 3. Hogar | 4. Deportes")
    c = input("Opcion: ")
    return n, p, v, c

def mostrar_resultado_negociacion(estado, valor, producto):

    frase = random.choice(producto.vendedor.frases_negociao)
    if estado == "ACEPTADA":
        print(f"\n¡TRATO HECHO! {producto.vendedor.nombre} dice: '{frase}'")
        print(f"Has comprado {producto.nombre} por {valor}€.")

    elif estado == "CONTRAOFERTA":
        print(f"\n{producto.vendedor.nombre} dice: '{frase}'")
        print(f"Me parece poco... ¿Qué tal {valor}€?")

    elif estado == "RECHAZADA":
        print(f"\n{producto.vendedor.nombre} dice: '{frase}'")
        print("Oferta rechazada. Intenta subir el precio.")