import csv
import os
from src.item import Item, InstantiateCSVError


def test_instantiate_from_csv_success():
    Item.instantiate_from_csv()
    assert len(Item.all) == 3


def test_instantiate_from_csv_file_not_found():
    os.remove("items.csv")
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
    os.mknod("items.csv")


def test_instantiate_from_csv_damaged_file():
    with open("items.csv", "w") as csv_file:
        csv_file.write("name,price\n")
        csv_file.write("Apple,1.99")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
    os.remove("items.csv")


def test_instantiate_from_csv_extra_columns():
    with open("items.csv", "w") as csv_file:
        csv_file.write("name,price,quantity,extra_column\n")
        csv_file.write("Apple,1.99,10,extra_value")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
    os.remove("items.csv")


def test_instantiate_from_csv_missing_columns():
    with open("items.csv", "w") as csv_file:
        csv_file.write("name,price\n")
        csv_file.write("Apple,1.99")
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
    os.remove("items.csv")


def test_calculate_total_price():
    item = Item("Apple", 1.99, 10)
    assert item.calculate_total_price() == 19.90


def test_apply_discount():
    item = Item("Apple", 1.99, 10)
    item.apply_discount()
    assert item.price == 1.791
