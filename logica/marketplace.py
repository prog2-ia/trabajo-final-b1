from datos.producto import Producto
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
from datos.tacanyo import Tacanyo
from datos.normal import Normal
from datos.desesperado import Desesperado

class Marketplace:
    def __init__(self): #Creamos el inventario
        self._inventario = [] # Miembro protegido
        self.contador_ids = 1

        v1 = Tacanyo("Julián") #Vendedores creados por defecto
        v2 = Normal("Marta")
        v3 = Desesperado("Juan")

        # Uso del nuevo operador += definido abajo
        self += Electronica(self.contador_ids, "iPhone 13", 600, v1)
        self += Ropa(self.contador_ids, "Camiseta Vintage", 25, v2)
        self += Hogar(self.contador_ids, "Lámpara de pie", 45, v3)

    # T08: Sobrecarga de += para añadir productos al inventario directamente [cite: 306, 312]
    def __iadd__(self, producto):
        if isinstance(producto, Producto):
            self._inventario.append(producto)
            self.contador_ids += 1
        return self

    # T07: Permite usar len(mercado) para saber cuántos productos hay [cite: 20, 82]
    def __len__(self):
         return len(self._inventario)

    # T08: Permite acceder a productos por índice: mercado[0]
    def __getitem__(self, index):
        return self._inventario[index]

    # T07: Determina si el mercado tiene existencias en un contexto booleano
    def __bool__(self):
        return len(self._inventario) > 0

    def vender_producto(self, producto):
        self += producto  # Reutiliza el operador __iadd__
        return True
    def comprar_final(self, id_prod): #Funcion para comprar y eliminarlo del inventario.
        for p in self._inventario:
            if p.id_prod == id_prod:
                self._inventario.remove(p)
                return p
        return None

    def buscar_producto(self, id_p): #Funcion para buscar y comprar un producto.
        for p in self._inventario:
            if p.id_prod == id_p: return p
        return None