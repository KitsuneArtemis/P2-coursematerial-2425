class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, (int, float)):
            return NotImplemented
        return Money(self.amount * multiplier, self.currency)

    def __repr__(self):
        return f'Money({self.amount}, "{self.currency}")'
