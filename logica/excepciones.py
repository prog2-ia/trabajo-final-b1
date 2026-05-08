class MarketplaceError(Exception):
    """Clase base para excepciones del marketplace."""
    pass

class ProductoNoEncontradoError(MarketplaceError):
    """Se lanza cuando se busca un ID que no existe."""
    pass

class ErrorValidacionPrecio(MarketplaceError):
    """Se lanza cuando el precio no es un número positivo válido."""
    pass

class CategoriaInvalidaError(MarketplaceError):
    """Se lanza cuando la categoría seleccionada no existe."""
    pass