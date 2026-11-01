
import pytest

from inventory.product import Product
from inventory.manager import InventoryManager
from inventory.exceptions import (
    InvalidProductError,
    ProductNotFoundError,
    InsufficientStockError
)


def test_add_product():
    manager = InventoryManager()
    product = Product("P101", "Laptop", 45000, 5)

    result = manager.add_product(product)

    assert result == "Product added successfully."
    assert manager.get_product("P101") == product


def test_duplicate_product():
    manager = InventoryManager()
    product = Product("P102", "Mouse", 500, 10)

    manager.add_product(product)

    with pytest.raises(InvalidProductError):
        manager.add_product(product)


def test_invalid_product():
    manager = InventoryManager()

    with pytest.raises(InvalidProductError):
        manager.add_product("Laptop")


def test_get_all_products():
    manager = InventoryManager()

    manager.add_product(Product("P103", "Keyboard", 1000, 5))
    manager.add_product(Product("P104", "Monitor", 12000, 3))

    assert len(manager.get_all_products()) == 2


def test_product_not_found():
    manager = InventoryManager()

    with pytest.raises(ProductNotFoundError):
        manager.get_product("P999")


def test_update_quantity():
    manager = InventoryManager()
    manager.add_product(Product("P105", "Phone", 15000, 5))

    manager.update_quantity("P105", 10)

    assert manager.get_product("P105").quantity == 10


def test_sell_product():
    manager = InventoryManager()
    manager.add_product(Product("P106", "Tablet", 12000, 10))

    manager.sell_product("P106", 3)

    assert manager.get_product("P106").quantity == 7


def test_insufficient_stock():
    manager = InventoryManager()
    manager.add_product(Product("P107", "Camera", 25000, 2))

    with pytest.raises(InsufficientStockError):
        manager.sell_product("P107", 5)


def test_invalid_sale_quantity():
    manager = InventoryManager()
    manager.add_product(Product("P108", "Speaker", 2000, 5))

    with pytest.raises(InvalidProductError):
        manager.sell_product("P108", 0)


def test_delete_product():
    manager = InventoryManager()
    manager.add_product(Product("P109", "Printer", 8000, 4))

    manager.delete_product("P109")

    with pytest.raises(ProductNotFoundError):
        manager.get_product("P109")


def test_delete_missing_product():
    manager = InventoryManager()

    with pytest.raises(ProductNotFoundError):
        manager.delete_product("P999")
