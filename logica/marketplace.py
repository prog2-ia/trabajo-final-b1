from datos.producto import Producto
from datos.subproductos import Electronica, Ropa, Hogar, Deportes
from datos.tacanyo import Tacanyo
from datos.normal import Normal
from datos.desesperado import Desesperado

class Marketplace:
    def __init__(self) -> None: #Creamos el inventario
        self._inventario: list['Producto'] = [] # Miembro protegido
        self.contador_ids: int = 1

        v1: 'Tacanyo' = Tacanyo("Julián") #Vendedores creados por defecto
        v2: 'Normal' = Normal("Marta")
        v3: 'Desesperado' = Desesperado("Juan")

        #Uso del nuevo operador += definido abajo
        self += Electronica(self.contador_ids, "iPhone 13", 600, v1)
        self += Ropa(self.contador_ids, "Camiseta Vintage", 25, v2)
        self += Hogar(self.contador_ids, "Lámpara de pie", 45, v3)

    #Sobrecarga de += para añadir productos al inventario directamente
    def __iadd__(self, producto: 'Producto') -> 'Marketplace':
        if isinstance(producto, Producto):
            self._inventario.append(producto)
            self.contador_ids += 1
        return self

    #Permite usar len(mercado) para saber cuántos productos hay
    def __len__(self) -> int:
         return len(self._inventario)

    #Permite acceder a productos por índice: mercado[0]
    def __getitem__(self, index: int) -> 'Producto':
        return self._inventario[index]

    #   Determina si el mercado tiene existencias en un contexto booleano
    def __bool__(self) -> bool:
        return len(self._inventario) > 0

    def vender_producto(self, producto: 'Producto') -> bool:
        self += producto  # Reutiliza el operador __iadd__
        return True
    def comprar_final(self, id_prod: int) -> 'Producto': #Funcion para comprar y eliminarlo del inventario.
        for p in self._inventario:
            if p.id_prod == id_prod:
                self._inventario.remove(p)
                return p
        return None

    # Funcion para buscar y comprar un producto.
    def buscar_producto(self, id_p: int) -> 'Producto':
        for p in self._inventario:
            if p.id_prod == id_p:
                return p
        return None