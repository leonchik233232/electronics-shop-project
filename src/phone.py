class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_card_quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.sim_card_quantity = sim_card_quantity

    def __add__(self, other):
        if isinstance(other, (Phone, Item)):
            return self.quantity + other.quantity
        raise TypeError("Unsupported operand type for +: 'Phone' or 'Item' and '{}'".format(type(other)))
