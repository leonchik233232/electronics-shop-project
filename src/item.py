class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # уровень цен с учетом скидки
    all = []  # список для хранения созданных экземпляров класса

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

        pass

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity
        pass

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        pass
