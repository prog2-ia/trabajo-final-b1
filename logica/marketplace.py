from datos import Producto, Electronica, Ropa, Hogar, Tacanyo, Normal, Desesperado

class Marketplace:
    def __init__(self): #Creamos el inventario
        self._inventario = [] # Miembro protegido
        self.contador_ids = 1

        v1 = Tacanyo("Julián") #Vendedores creados por defecto
        v2 = Normal("Marta")
        v3 = Desesperado("Juan")

        self.vender_producto(Electronica(self.contador_ids, "iPhone 13", 600, v1)) #Productos creados por defectos
        self.vender_producto(Ropa(self.contador_ids, "Camiseta Vintage", 25, v2))
        self.vender_producto(Hogar(self.contador_ids, "Lámpara de pie", 45, v3))

    def vender_producto(self, producto: Producto): #Funcion para vender productos y añadirlos al catalogo.
        self._inventario.append(producto)
        self.contador_ids += 1
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