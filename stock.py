class Stock:
    def __init__(self):
        self.name = "Test"
        self.price = 100
        self.history = []

    def set_price(self, new_price):
        self.history.append(self.price)
        self.price = new_price