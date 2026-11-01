# Smart Inventory Management System

**Developed by:** HARISMITHA D G

## Project Overview

The Smart Inventory Management System is a Python-based application designed to manage product information, stock quantities, and inventory records.

It uses Object-Oriented Programming concepts and supports JSON and CSV file storage.

## Features

- Add new products.
- View all available products.
- Update product quantities.
- Sell products and manage stock.
- Delete products.
- Save and load inventory using JSON.
- Save and load inventory using CSV.
- Handle invalid inputs using custom exceptions.

## Technologies Used

- Python 3.12
- Object-Oriented Programming
- JSON
- CSV
- Pytest
- Pytest Coverage

## OOP Concepts Implemented

1. **Inheritance:** Product inherits from BaseItem.
2. **Encapsulation:** Private attributes protect product data.
3. **Polymorphism:** Product implements the display_details method.
4. **Abstraction:** BaseItem defines an abstract method.

## Project Structure

```text
Smart_Inventory_Management/
│
├── inventory/
│   ├── __init__.py
│   ├── base.py
│   ├── product.py
│   ├── manager.py
│   ├── exceptions.py
│   └── storage.py
│
├── tests/
│   ├── __init__.py
│   ├── test_product.py
│   ├── test_manager.py
│   └── test_storage.py
│
├── main.py
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

## Run Unit Tests

```bash
python -m pytest -v
```

## Check Test Coverage

```bash
python -m pytest --cov=inventory --cov-report=term-missing
```

## Expected Outcome

The application provides a simple way to manage inventory records while demonstrating Python OOP, exception handling, file handling, and unit testing.

## Author

HARISMITHA D G
