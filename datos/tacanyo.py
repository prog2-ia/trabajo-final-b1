from datos.vendedor import Vendedor
import random


class Tacanyo(Vendedor):  # Subclase de vendedor.
    def __init__(self, nombre: str):  #Tipo simple str
        super().__init__(nombre)
        self.frases_negociao: list[str] = ["¿Te crees que el dinero crece en los árboles?",
                                           "Por ese precio no te doy ni las gracias.",
                                           "Si no tienes dinero, no compres."]

    def negociar(self, precio_original: float,
                 oferta_comprador: float) -> tuple:  #Parámetros float y retorno de tupla
        if oferta_comprador >= precio_original * 0.95:
            return "ACEPTADA", round(oferta_comprador, 1)

        # P04: Variable local tipada como float
        contra: float = round(random.uniform(precio_original * 0.98, precio_original), 1)
        return "CONTRAOFERTA", contra