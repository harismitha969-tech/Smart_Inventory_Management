
import pytest

from inventory.product import Product


def test_create_product():
    product = Product("P101", "Laptop", 45000, 5)

    assert product.item_id == "P101"
    assert product.name == "Laptop"
    assert product.price == 45000
    assert product.quantity == 5


def test_display_details():
    product = Product("P102", "Mouse", 500, 10)

    result = product.display_details()

    assert "P102" in result
    assert "Mouse" in result
    assert "500.00" in result


def test_update_quantity():
    product = Product("P103", "Keyboard", 1000, 5)

    product.update_quantity(8)

    assert product.quantity == 8


def test_negative_price():
    with pytest.raises(ValueError):
        Product("P104", "Monitor", -100, 5)


def test_negative_quantity():
    with pytest.raises(ValueError):
        Product("P105", "Phone", 15000, -2)


def test_empty_product_name():
    with pytest.raises(ValueError):
        Product("P106", "", 1000, 5)


def test_negative_updated_quantity():
    product = Product("P107", "Tablet", 12000, 4)

    with pytest.raises(ValueError):
        product.update_quantity(-1)
