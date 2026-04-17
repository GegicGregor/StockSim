class Statistics:
    def __init__(self, stock, sim):
        self.myStock = stock
        self.simulation = sim

    def avg_price(self):
        avg = 0
        for i, value in enumerate(self.myStock.history):
            avg += value
        return avg / (len(self.myStock.history) + 1)

    def growth(self):
        return self.myStock.history[-1]/self.myStock.history[0]


    def avg_growth_over_n(self, n, updates):
        avg = 0
        for i in range(n):
            self.simulation.for_loop(updates)
            avg += self.growth()
            print(self.growth())
            self.myStock.reset()
        return avg/n

