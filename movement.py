import numpy as np
class Movement:
    def __init__(self):
        self.rng = np.random.default_rng()

    def move(self, curr_price,  status):
        if status:

            curr_price *= self._increase()
            return curr_price

        return None


    def _increase(self):
        return 0.995 + (self.rng.random() / 100)