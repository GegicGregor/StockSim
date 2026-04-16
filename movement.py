import numpy as np
class Movement:
    def __init__(self):
        self.rng = np.random.default_rng()

    def move(self, curr_price):
        return curr_price * self._increase()

    def _increase(self):
        mu, sigma = 1.00021, 0.007
        return self.rng.normal(mu, sigma)