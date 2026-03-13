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