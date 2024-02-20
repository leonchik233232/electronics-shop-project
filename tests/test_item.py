"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item, InstantiateCSVError

import pytest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def test_calculate_total_price(price=10000, quantity=20):
    assert price * quantity == 200000


def test_apply_discount(price=10000, pay_rate=0.8):
    assert price * pay_rate == 8000


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_():
    item = Item('Телефон', 25000, 3)
    item.name = 'Суперсмартфон'
    assert item.name == 'Суперсмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test___repr__():
    item1 = Item("Ноутбук", 50000, 2)
    assert repr(item1) == "Item('Ноутбук', 50000, 2)"
    assert str(item1) == 'Ноутбук'


def test___str__():
    item1 = Item("Ноутбук", 50000, 2)
    assert str(item1) == 'Ноутбук'


def test_instantiate_from_csv_invalid():
    invalid_file_path = BASE_DIR.joinpath('src', 'items_error.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(invalid_file_path)


def test_instantiate_from_csv():
    file_path = BASE_DIR.joinpath('src', 'items.csv')
    Item.instantiate_from_csv(file_path)