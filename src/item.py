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
#HOMEWORK_2
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        """
        Возвращает наименование товара.

        :return: Наименование товара.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Устанавливает наименование товара.

        :param value: Новое наименование товара.
        """
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

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

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv.
        """
        import csv
        with open('src/items.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                cls.all.append(item)

    @staticmethod
    def string_to_number(string: str) -> float:
        """
        Статический метод, возвращающий число из числа-строки.

        :param string: Число-строка.
        :return: Число.
        """
        return float(string)
