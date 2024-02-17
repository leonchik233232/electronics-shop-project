import os

class Item:
    all: List["Item"] = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Create an instance of the Item class.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        """
        Create a list of Item objects from a CSV file.

        :raises FileNotFoundError: if the CSV file is not found.
        :raises InstantiateCSVError: if the CSV file is damaged or missing required columns.
        """
        if not os.path.exists("items.csv"):
            raise FileNotFoundError("File items.csv not found")

        try:
            with open("items.csv", "r") as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # Skip the header row
                for row in reader:
                    if len(row) != 3:
                        raise InstantiateCSVError("CSV file is damaged or missing required columns")
                    name, price, quantity = row
                    Item(name, float(price), int(quantity))
        except FileNotFoundError:
            raise FileNotFoundError("File items.csv not found")

    def calculate_total_price(self) -> float:
        """
        Calculate the total price of this item in the store.

        :return: The total price of the item.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Apply the store's discount to this item.
        """
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __str__(self):
        return f"Item: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
