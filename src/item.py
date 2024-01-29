def __init__(self, name: str, price: float, quantity: int) -> None:
    """
    Создание экземпляра класса item.
    """
    self.name = name
    self.price = price
    self.quantity = quantity
    self.all.append(self)
    self.code = code


def calculate_total_price(self) -> float:
    """
    Рассчитывает общую стоимость конкретного товара в магазине.

    :return: Общая стоимость товара.
    """
    return self.price * self.quantity


def apply_discount(self) -> None:
    """
    Применяет установленную скидку для конкретного товара.
    """
    self.price = self.price * self.pay_rate

def __repr__(self):
    return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

def __str__(self):
    return f"Item: {self.name}, Price: {self.price}, Quantity: {self.quantity}"