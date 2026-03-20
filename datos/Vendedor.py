# --- JERARQUÍA DE VENDEDORES ---
class Vendedor(ABC): #Creamos la clase padre para los vendedores
    def __init__(self, nombre):
        self.nombre = nombre
        self.frases_negociao = []

    @abstractmethod #Necesario para todas las clases.
    def negociar(self, precio_original, oferta_comprador):
        pass

class Desesperado(Vendedor): #Subclase 1º de vendedores
    def __init__(self, nombre):
        super().__init__(nombre)
        self.frases_negociao = ["¡Necesito comer porfa!", "Uff, lo necesito vender ya...", "Acepta esto, es mi última esperanza."]

    def negociar(self, precio_original, oferta_comprador): #Cada clase tiene una forma de negociar en función de su situación.
        if oferta_comprador >= precio_original * 0.70:
            return "ACEPTADA", round(oferta_comprador, 1)
        return "RECHAZADA", 0

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

class Tacanyo(Vendedor): #Subclase 3º de vendedor.
    def __init__(self, nombre):
        super().__init__(nombre)
        self.frases_negociao = ["¿Te crees que el dinero crece en los árboles?", "Por ese precio no te doy ni las gracias.", "Si no tienes dinero, no compres."]

    def negociar(self, precio_original, oferta_comprador):
        if oferta_comprador >= precio_original * 0.95:
            return "ACEPTADA", round(oferta_comprador, 1)
        contra = round(random.uniform(precio_original * 0.98, precio_original), 1)
        return "CONTRAOFERTA", contra