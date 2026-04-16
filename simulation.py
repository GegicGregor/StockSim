from stock import Stock
myStock = Stock()


class Simulation:
    def __init__(self):
        pass

    def for_loop(self, loops):
        for i in range(loops):
            myStock.std_update()
