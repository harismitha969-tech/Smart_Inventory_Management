
from abc import ABC, abstractmethod


class BaseItem(ABC):
    """Parent class for all inventory items."""

    def __init__(self, item_id, name):
        self._item_id = item_id
        self._name = name

    @property
    def item_id(self):
        return self._item_id

    @property
    def name(self):
        return self._name

    @abstractmethod
    def display_details(self):
        """Display item information."""
        pass
