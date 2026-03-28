from stock import Stock
from movement import Movement
from visualization import Visualization
import time


visualization = Visualization()
myStock = Stock()
movement = Movement()
while myStock.price <= 200:
    if myStock.price <= 10:
        myStock.set_price(100)
        input()

    print(myStock.price)
    myStock.set_price(movement.move(myStock.price, True))
visualization.start_graph(myStock.history)

print(myStock.price)
print(myStock.history)