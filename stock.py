from operator import index
from movement import Movement

movement = Movement()

class Stock:
    def __init__(self):
        self.name = "Test"
        self.price = self.start_price = 100
        self.history = []

    def set_price(self, new_price):
        self.history.append(self.price)
        self.price = new_price

    def avg_price(self):
        avg = 0
        for i, value in enumerate(self.history):
            avg += value
        return avg/(len(self.history)+1)

    def std_update(self):
        self.set_price(movement.move(self.price))