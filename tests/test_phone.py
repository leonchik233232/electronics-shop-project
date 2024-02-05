def test_phone_addition():
    phone1 = Phone("Phone 1", 500, 10, 2)
    phone2 = Phone("Phone 2", 600, 5, 1)
    item = Item("Item", 100, 20)

    assert phone1 + phone2 == 15  # Сложение двух экземпляров класса Phone
    assert phone1 + item == 30  # Сложение экземпляра класса Phone и Item

