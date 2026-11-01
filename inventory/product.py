
from inventory.base import BaseItem


class Product(BaseItem):
    """Represents a product in the inventory."""

    def __init__(self, item_id, name, price, quantity):
        super().__init__(item_id, name)

        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("Product ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")

        if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.__price = float(price)
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def update_quantity(self, new_quantity):
        if isinstance(new_quantity, bool) or not isinstance(new_quantity, int):
            raise ValueError("Quantity must be an integer.")

        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.__quantity = new_quantity

    def display_details(self):
        return (
            f"ID: {self.item_id}, "
            f"Name: {self.name}, "
            f"Price: Rs.{self.price:.2f}, "
            f"Quantity: {self.quantity}"
        )
