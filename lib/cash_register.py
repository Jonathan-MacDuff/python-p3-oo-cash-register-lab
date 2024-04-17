#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, item, price, quantity=1):
        for _ in range(quantity):
            self.items.append(item)
        self.total += price * quantity
        self.last_transaction_total = price * quantity
    
    def apply_discount(self):
        if (self.discount != 0):
            self.total = self.total - (self.total * (self.discount / 100))
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        self.items.remove(self.items[-1])
        self.total = self.total - self.last_transaction_total

