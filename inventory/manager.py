
from inventory.product import Product
from inventory.exceptions import (
    InvalidProductError,
    ProductNotFoundError,
    InsufficientStockError
)


class InventoryManager:
    """Manages all inventory products."""

    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        if not isinstance(product, Product):
            raise InvalidProductError("Invalid product object.")

        if product.item_id in self.__products:
            raise InvalidProductError("Product ID already exists.")

        self.__products[product.item_id] = product
        return "Product added successfully."

    def get_product(self, item_id):
        if item_id not in self.__products:
            raise ProductNotFoundError("Product not found.")

        return self.__products[item_id]

    def get_all_products(self):
        return list(self.__products.values())

    def update_quantity(self, item_id, quantity):
        product = self.get_product(item_id)

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise InvalidProductError("Quantity must be an integer.")

        if quantity < 0:
            raise InvalidProductError("Quantity cannot be negative.")

        product.update_quantity(quantity)
        return "Quantity updated successfully."

    def sell_product(self, item_id, quantity):
        product = self.get_product(item_id)

        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise InvalidProductError("Sale quantity must be a positive integer.")

        if quantity > product.quantity:
            raise InsufficientStockError("Not enough stock available.")

        product.update_quantity(product.quantity - quantity)
        return "Product sold successfully."

    def delete_product(self, item_id):
        if item_id not in self.__products:
            raise ProductNotFoundError("Product not found.")

        del self.__products[item_id]
        return "Product deleted successfully."