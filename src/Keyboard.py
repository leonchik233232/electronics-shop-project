from abc import ABC, abstractmethod
from typing import Union

class LanguageMixin(ABC):
    """
    Mixin class for managing language (keyboard layout).
    """

    _language: str = "EN"

    @property
    def language(self) -> str:
        """
        Current language (keyboard layout).
        """
        return self._language

    @language.setter
    def language(self, value: str):
        """
        Change the language (keyboard layout).
        """
        if value not in ["EN", "RU"]:
            raise ValueError("Invalid language")
        self._language = value

    def change_lang(self):
        """
        Change the language (keyboard layout) to the other supported language.
        """
        self._language = "EN" if self._language == "RU" else "RU"


class Keyboard(Item, LanguageMixin):
    """
    Class representing a keyboard product.
    """

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

