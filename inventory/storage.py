
import json
import csv
from pathlib import Path

from inventory.product import Product
from inventory.exceptions import InvalidProductError


class InventoryStorage:

    @staticmethod
    def save_json(products, filename):
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)

        data = [
            {
                "item_id": p.item_id,
                "name": p.name,
                "price": p.price,
                "quantity": p.quantity
            }
            for p in products
        ]

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_json(filename):
        path = Path(filename)

        if not path.exists():
            return []

        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON must contain a list.")

            return [
                Product(
                    item["item_id"],
                    item["name"],
                    item["price"],
                    item["quantity"]
                )
                for item in data
            ]

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            raise InvalidProductError(f"Invalid JSON data: {error}") from error

    @staticmethod
    def save_csv(products, filename):
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["item_id", "name", "price", "quantity"])

            for product in products:
                writer.writerow([
                    product.item_id,
                    product.name,
                    product.price,
                    product.quantity
                ])

    @staticmethod
    def load_csv(filename):
        path = Path(filename)

        if not path.exists():
            return []

        products = []

        try:
            with path.open("r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                required = {"item_id", "name", "price", "quantity"}

                if not reader.fieldnames or not required.issubset(reader.fieldnames):
                    raise ValueError("CSV is missing required columns.")

                for row in reader:
                    products.append(
                        Product(
                            row["item_id"],
                            row["name"],
                            float(row["price"]),
                            int(row["quantity"])
                        )
                    )

            return products

        except (KeyError, TypeError, ValueError, csv.Error) as error:
            raise InvalidProductError(f"Invalid CSV data: {error}") from error
