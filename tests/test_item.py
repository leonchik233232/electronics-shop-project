def test_calculate_total_price():
    item = Item("Телевизор", 15000, 10)
    assert item.calculate_total_price() == 150000

def test_apply_discount():
    item = Item("Телевизор", 15000, 10)
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 13500.0

def test_calculate_total_price_with_zero_quantity():
    item = Item("Книга", 500, 0)
    assert item.calculate_total_price() == 0

def test_apply_discount_with_zero_price():
    item = Item("Книга", 500, 0)
    Item.pay_rate = 0.7
    item.apply_discount()
    assert item.price == 0.0

def test_calculate_total_price_with_negative_price():
    item = Item("Компьютер", -50000, 5)
    assert item.calculate_total_price() == 0

def test_apply_discount_with_negative_price():
    item = Item("Компьютер", -50000, 5)
    Item.pay_rate = 0.85
    item.apply_discount()
    assert item.price == 0.0

def test_calculate_total_price_with_negative_quantity():
    item = Item("Наушники", 3000, -3)
    assert item.calculate_total_price() == 0

def test_apply_discount_with_negative_quantity():
    item = Item("Наушники", 3000, -3)
    Item.pay_rate = 0.95
    item.apply_discount()
    assert item.price == 0.0

def test_item_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item(name=Смартфон, price=10000, quantity=20)"

def test_item_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == "Item: Смартфон, Price: 10000, Quantity: 20"

def test_add_different_types():
    item1 = Item("Телевизор", 15000, 10)
    phone = Phone("Смартфон", 10000, 20, 2)
    with pytest.raises(TypeError):
        item1 + phone
