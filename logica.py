from datos import Producto

class Marketplace:
    def __init__(self):
        self._inventario = [] # Miembro protegido
        self.contador_ids = 1

    def vender_producto(self, producto: Producto):
        self._inventario.append(producto)
        self.contador_ids += 1
        return True

    def comprar_final(self, id_prod):
        for p in self._inventario:
            if p.id_prod == id_prod:
                self._inventario.remove(p)
                return p
        return None

    def buscar_producto(self, id_p):
        for p in self._inventario:
            if p.id_prod == id_p: return p
        return None