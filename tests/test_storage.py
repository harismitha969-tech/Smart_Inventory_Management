
import pytest

from inventory.product import Product
from inventory.storage import InventoryStorage
from inventory.exceptions import InvalidProductError


def test_save_and_load_json(tmp_path):
    products = [
        Product("P101", "Laptop", 45000, 5),
        Product("P102", "Mouse", 500, 10)
    ]

    file_path = tmp_path / "products.json"

    InventoryStorage.save_json(products, file_path)
    loaded = InventoryStorage.load_json(file_path)

    assert len(loaded) == 2
    assert loaded[0].name == "Laptop"
    assert loaded[1].quantity == 10


def test_save_and_load_csv(tmp_path):
    products = [
        Product("P103", "Keyboard", 1000, 5),
        Product("P104", "Monitor", 12000, 3)
    ]

    file_path = tmp_path / "products.csv"

    InventoryStorage.save_csv(products, file_path)
    loaded = InventoryStorage.load_csv(file_path)

    assert len(loaded) == 2
    assert loaded[0].name == "Keyboard"
    assert loaded[1].price == 12000


def test_load_missing_json(tmp_path):
    file_path = tmp_path / "missing.json"

    loaded = InventoryStorage.load_json(file_path)

    assert loaded == []


def test_load_missing_csv(tmp_path):
    file_path = tmp_path / "missing.csv"

    loaded = InventoryStorage.load_csv(file_path)

    assert loaded == []


def test_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(InvalidProductError):
        InventoryStorage.load_json(file_path)


def test_invalid_csv(tmp_path):
    file_path = tmp_path / "invalid.csv"
    file_path.write_text("wrong,columns\n1,2\n", encoding="utf-8")

    with pytest.raises(InvalidProductError):
        InventoryStorage.load_csv(file_path)


def test_invalid_product_data_in_json(tmp_path):
    file_path = tmp_path / "bad_product.json"
    file_path.write_text(
        '[{"item_id": "P1", "name": "Laptop", "price": -100, "quantity": 5}]',
        encoding="utf-8"
    )

    with pytest.raises(InvalidProductError):
        InventoryStorage.load_json(file_path)
