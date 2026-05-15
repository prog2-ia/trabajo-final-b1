from datos.producto import Producto

class Electronica(Producto): #Clases derivadas de productos y como se muestran.
    def __str__(self) -> str:
        return f"[{self.id_prod}] {self.nombre} (Electrónica) - {self.precio}€"

class Ropa(Producto): #Subclase numero 1
    def __str__(self) -> str:
        return f"[{self.id_prod}] {self.nombre} (Ropa) - {self.precio}€"

class Hogar(Producto): #Subclase numero 2
    def __str__(self) -> str:
        return f"[{self.id_prod}] {self.nombre} (Hogar) - {self.precio}€"

class Deportes(Producto): #Subclase numero 3
    def __str__(self) -> str:
        return f"[{self  .id_prod}] {self.nombre} (Deportes) - {self.precio}€"