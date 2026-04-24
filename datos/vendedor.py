from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.frases_negociao: list[str] = []

    @abstractmethod
    def negociar(self, precio_original: float, oferta_comprador: float) -> tuple:
        pass