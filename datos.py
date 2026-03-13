class Producto(ABC):
    def __init__(self, id_prod, nombre, precio, vendedor_obj):
        self.id_prod = id_prod
        self.nombre = nombre
        self.__precio = 0.0 # Miembro privado
        self.precio = precio # Llama al setter
        self.vendedor = vendedor_obj

    @property
    def precio(self): return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = round(float(valor), 1) if valor >= 0 else 0.0

@abstractmethod
    def __str__(self): pass

class Electronica(Producto):
    def __str__(self): return f"[{self.id_prod}] {self.nombre} (Electrónica) - {self.precio}€"

class Ropa(Producto):
    def __str__(self): return f"[{self.id_prod}] {self.nombre} (Ropa) - {self.precio}€"

class Hogar(Producto):
    def __str__(self): return f"[{self.id_prod}] {self.nombre} (Hogar) - {self.precio}€"

class Deportes(Producto):
    def __str__(self): return f"[{self.id_prod}] {self.nombre} (Deportes) - {self.precio}€"