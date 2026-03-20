from abc import ABC, abstractmethod

class Vendedor(ABC): #Creamos la clase padre para los vendedores
    def __init__(self, nombre):
        self.nombre = nombre
        self.frases_negociao = []

    @abstractmethod #Necesario para todas las clases.
    def negociar(self, precio_original, oferta_comprador):
        pass
