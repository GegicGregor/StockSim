class Simulation:
    def __init__(self, stock):
        self.myStock = stock

    def for_loop(self, loops):
        for i in range(loops):
            self.myStock.std_update()

    def high_price(self, high, low):
        while self.myStock.price <= high:
            if self.myStock.price <= low:
                break
            self.myStock.std_update()



