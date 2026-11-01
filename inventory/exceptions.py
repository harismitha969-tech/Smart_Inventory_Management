
class InventoryError(Exception):
    """Base exception for inventory errors."""
    pass


class InvalidProductError(InventoryError):
    """Raised when product information is invalid."""
    pass


class ProductNotFoundError(InventoryError):
    """Raised when a product does not exist."""
    pass


class InsufficientStockError(InventoryError):
    """Raised when available stock is insufficient."""
    pass
