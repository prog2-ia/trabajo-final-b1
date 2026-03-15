import random

def mostrar_menu():
    print("\n--- Marketplace ---")
    print("1. Ver catalogo\n2. Vender producto\n3. Negociar/Comprar\n4. Salir")
    return input("Selección: ")

def pedir_datos_venta(): #Datos necesarios para publicar un producto
    print("\n--- PUBLICAR ---")
    n = input("Nombre: ")
    p = float(input("Precio: "))
    v = input("Tu nombre: ")
    print("Categoria: 1. Electronica | 2. Ropa | 3. Hogar | 4. Deportes")
    c = input("Opcion: ")
    return n, p, v, c

def mostrar_resultado_negociacion(estado, valor, producto): #Al negociar definimos las 3 respuestas.

    frase = random.choice(producto.vendedor.frases_negociao)
    if estado == "ACEPTADA": #Si se acepta se muestra una frase de aceptación del vendedor y el mensaje de la compra
        print(f"\n¡TRATO HECHO! {producto.vendedor.nombre} dice: '{frase}'")
        print(f"Has comprado {producto.nombre} por {valor}€.")

    elif estado == "CONTRAOFERTA": #Se debate el frase con una contraoferta y una frase.
        print(f"\n{producto.vendedor.nombre} dice: '{frase}'")
        print(f"Me parece poco... ¿Qué tal {valor}€?")

    elif estado == "RECHAZADA": #Se rechaza la compra y acaba la compra con otra frase.
        print(f"\n{producto.vendedor.nombre} dice: '{frase}'")
        print("Oferta rechazada. Intenta subir el precio.")