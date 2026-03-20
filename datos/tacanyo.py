from datos.vendedor import Vendedor

class Tacanyo(Vendedor): #Subclase 3º de vendedor.
    def __init__(self, nombre):
        super().__init__(nombre)
        self.frases_negociao = ["¿Te crees que el dinero crece en los árboles?", "Por ese precio no te doy ni las gracias.", "Si no tienes dinero, no compres."]

    def negociar(self, precio_original, oferta_comprador):
        if oferta_comprador >= precio_original * 0.95:
            return "ACEPTADA", round(oferta_comprador, 1)
        contra = round(random.uniform(precio_original * 0.98, precio_original), 1)
        return "CONTRAOFERTA", contra