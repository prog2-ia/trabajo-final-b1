from abc import ABC, abstractmethod
from datos.vendedor import Vendedor
from logica.excepciones import ErrorValidacionPrecio

class Producto(ABC):
    def __init__(self, id_prod: int, nombre: str, precio: float, vendedor_obj: Vendedor):
        self.id_prod: int = id_prod
        self.nombre: str = nombre
        self.__precio: float = 0.0
        self.precio = precio  # Usa el setter
        self.vendedor: "Vendedor" = vendedor_obj

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            valor_float = float(valor)
            if valor_float <= 0:
                raise ErrorValidacionPrecio("El precio debe ser mayor que cero.")
            self.__precio = round(valor_float, 1)
        except ValueError:
            raise ErrorValidacionPrecio("El precio debe ser un valor numérico.")

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __len__(self) -> int:
        return len(self.nombre)