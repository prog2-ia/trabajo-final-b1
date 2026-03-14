from abc import ABC, abstractmethod
import random

# --- JERARQUÍA DE VENDEDORES ---
class Vendedor(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.frases_negociao = []

    @abstractmethod
    def negociar(self, precio_original, oferta_comprador):
        pass

class Desesperado(Vendedor):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.frases_negociao = ["¡Necesito comer porfa!", "Uff, lo necesito vender ya...", "Acepta esto, es mi última esperanza."]

    def negociar(self, precio_original, oferta_comprador):
        if oferta_comprador >= precio_original * 0.70:
            return "ACEPTADA", round(oferta_comprador, 1)
        return "RECHAZADA", 0

class Normal(Vendedor):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.frases_negociao = ["Creo que el precio es justo.", "Podemos llegar a un acuerdo.", "Ni para ti ni para mí."]

    def negociar(self, precio_original, oferta_comprador):
        if oferta_comprador >= precio_original * 0.85:
            return "ACEPTADA", round(oferta_comprador, 1)
        elif oferta_comprador >= precio_original * 0.75:
            contra = round(random.uniform(oferta_comprador, precio_original * 0.95), 1)
            return "CONTRAOFERTA", contra
        return "RECHAZADA", 0

class Tacanyo(Vendedor):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.frases_negociao = ["¿Te crees que el dinero crece en los árboles?", "Por ese precio no te doy ni las gracias.", "Si no tienes dinero, no compres."]

    def negociar(self, precio_original, oferta_comprador):
        if oferta_comprador >= precio_original * 0.95:
            return "ACEPTADA", round(oferta_comprador, 1)
        contra = round(random.uniform(precio_original * 0.98, precio_original), 1)
        return "CONTRAOFERTA", contra

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