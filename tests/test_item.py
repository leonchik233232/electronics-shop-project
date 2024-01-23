"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000

def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0

def test_all_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert Item.all == [item1, item2]
