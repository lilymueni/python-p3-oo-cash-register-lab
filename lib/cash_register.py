class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.last_transaction_amount = 0
        self.discount = discount
        self.items = []

    def add_item(self, item_name, quantity, item_price):  # Added item_price parameter
        total_price = quantity * item_price
        self.total += total_price
        self.last_transaction_amount = total_price
        self.items.append((item_name, quantity, item_price))

    def apply_discount(self):
        discount_amount = self.total * (self.discount / 100.0)
        self.total -= discount_amount
        self.last_transaction_amount = -discount_amount  # Negative amount for discount

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            last_item_price = last_item[1] * last_item[2]  # quantity * price_per_item
            self.total -= last_item_price
            self.last_transaction_amount = -last_item_price
        else:
            print("No items to void")

# Example usage:
register = CashRegister(10)  # Initialize with a 10% discount
register.add_item("Apple", 3, 2)  # Add 3 apples at $2 each
register.add_item("Banana", 2, 1.5)  # Add 2 bananas at $1.5 each
print(register.total)  # Should print 9.0 (3*2 + 2*1.5 = 6 + 3)
register.apply_discount()
print(register.total)  # Should print 8.1 (assuming a 10% discount)
register.void_last_transaction()
print(register.total)  # Should print 9.0 (voiding the last transaction)
