from datos.vendedor import Vendedor

class Normal(Vendedor): #Subclase 2º de vendedor.
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
