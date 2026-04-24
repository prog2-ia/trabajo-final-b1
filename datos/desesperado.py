from datos.vendedor import Vendedor

class Desesperado(Vendedor): #Subclase 1º de vendedores
    def __init__(self, nombre):
        super().__init__(nombre)
        self.frases_negociao = ["¡Necesito comer porfa!", "Uff, lo necesito vender ya...", "Acepta esto, es mi última esperanza."]

    def negociar(self, precio_original: float, oferta_comprador: float) -> tuple:
        if oferta_comprador >= precio_original * 0.70:
            return "ACEPTADA", round(oferta_comprador, 1)
        return "RECHAZADA", 0.0