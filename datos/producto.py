from abc import ABC, abstractmethod

class Producto(ABC): #Clase padre para todos los productos.
    def __init__(self, id_prod, nombre, precio, vendedor_obj):
        self.id_prod = id_prod
        self.nombre = nombre
        self.__precio = 0.0 # Miembro privado
        self.precio = precio # Llama al setter
        self.vendedor = vendedor_obj

    @property #Precio obligatorio pero privado
    def precio(self): return self.__precio

    @precio.setter #Funcion para seleccionar el precio.
    def precio(self, valor):
        self.__precio = round(float(valor), 1) if valor >= 0 else 0.0

    @abstractmethod
    def __str__(self): pass