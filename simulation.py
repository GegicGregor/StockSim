from visualization import myStock


class Simulation:
    def __init__(self, stock):
        self.myStock = stock

    def for_loop(self, loops):
        for i in range(loops):
            self.myStock.std_update()

    def high_price(self, target, low):
        while self.myStock.price <= target:
            if self.myStock.price <= low:
                break
            self.myStock.std_update()



