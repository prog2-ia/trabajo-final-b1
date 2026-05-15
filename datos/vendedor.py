from abc import ABC, abstractmethod

class Vendedor(ABC): #Clase padre de todos los tipos de vendedores, especificamos atributos necesarios.
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.frases_negociao: list[str] = []

    @abstractmethod #Clase padre de negociar con sus atributos necesarios.
    def negociar(self, precio_original: float, oferta_comprador: float) -> tuple:
        pass