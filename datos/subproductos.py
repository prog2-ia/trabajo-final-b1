from datos.producto import Producto

class Electronica(Producto): #Clases derivadas de productos y como se muestran.
    def __str__(self) -> str:
        return f"[{self.id_prod}] {self.nombre} (Electrónica) - {self.precio}€"

class Ropa(Producto):
    def __str__(self) -> str:
        return f"[{self.id_prod}] {self.nombre} (Ropa) - {self.precio}€"

class Hogar(Producto):
    def __str__(self) -> str:
        return f"[{self.id_prod}] {self.nombre} (Hogar) - {self.precio}€"

class Deportes(Producto):
    def __str__(self) -> str:
        return f"[{self  .id_prod}] {self.nombre} (Deportes) - {self.precio}€"