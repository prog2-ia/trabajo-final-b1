from abc import ABC, abstractmethod
from datos.vendedor import Vendedor

class Producto(ABC): #Clase padre para todos los productos.
    def __init__(self, id_prod, nombre, precio, vendedor_obj):
        self.id_prod = id_prod
        self.nombre = nombre
        self.__precio = 0.0 # Miembro privado
        self.precio = precio # Llama al setter
        self.vendedor: 'Vendedor' = vendedor_obj # Tipo entre comillas para evitar errores

    @property #Precio obligatorio pero privado
    def precio(self) -> float: #Indica que devuelve un float
        return self.__precio

    @precio.setter #Funcion para seleccionar el precio.
    def precio(self, valor: float) -> None: #No devuelve nada (None)
        self.__precio = round(float(valor), 1) if valor >= 0 else 0.0

    @abstractmethod
    def __str__(self) -> str: #Metodo especial para representar el objeto como texto
        pass

    def __len__(self) -> int: #Devuelve la longitud del nombre del producto
        return len(self.nombre)