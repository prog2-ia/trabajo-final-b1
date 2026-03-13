from datos import Producto

class Marketplace:
    def __init__(self):
        self._inventario = [] # Miembro protegido
        self.contador_ids = 1

    def vender_producto(self, producto: Producto):
        self._inventario.append(producto)
        self.contador_ids += 1
        return True