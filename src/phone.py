class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_card_quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.sim_card_quantity = sim_card_quantity

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            raise TypeError("Unsupported operand type for +: 'Phone' and 'Item'")
        else:
            raise TypeError("Unsupported operand type for +: 'Phone' and '{}'".format(type(other)))
