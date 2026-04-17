from movement import Movement

movement = Movement()

class Stock:
    def __init__(self, start_price):
        self.name = "Test"
        self.price = self.start_price = start_price
        self.history = []

    def set_price(self, new_price):
        self.price = new_price

    def update_price(self, new_price):
        self.append_history(new_price)
        self.set_price(new_price)

    def set_history(self, history):
        self.history = history

    def append_history(self, value):
        self.history.append(value)

    def std_update(self):
        self.update_price(movement.move(self.price))

    def reset(self):
        self.set_price(self.start_price)
        self.history = []