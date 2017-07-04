class ShoppingCart(object):
    """
        A shopping cart class illustrating abstraction and encapsulation
    """

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if isinstance(quantity, int) and isinstance(price, int):
            self.items[item_name] = quantity
            self.total += (price * quantity)

    def remove_item(self, item_name, quantity, price):
        if isinstance(quantity, int) and isinstance(price, int):
            if item_name in self.items:
                if quantity >= self.items[item_name]:
                    if self.total >= (price * self.items[item_name]):
                        self.total -= (price * self.items[item_name])
                    del (self.items[item_name])
                else:
                    self.items[item_name] -= quantity
                    if self.total >= (price * quantity):
                        self.total -= (price * quantity)
                    else:
                        self.total -= (price * self.items[item_name])

    def checkout(self, cash_paid):
        if isinstance(cash_paid, int):
            if cash_paid >= self.total:
                return cash_paid - self.total
            else:
                return "Cash paid not enough"


class Shop(ShoppingCart):
    """
        A Shop sub class illustrating inheritance and polymorphism
    """

    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1
