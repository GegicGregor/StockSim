from stock import Stock
from movement import Movement
from visualization import Visualization
import time


visualization = Visualization()
myStock = Stock()
movement = Movement()
#while myStock.price <= 200:
#    if myStock.price <= 10:
#        myStock.set_price(100)
#        input()
#
#    print(myStock.price)
#    myStock.set_price(movement.move(myStock.price, True))

for i in range(365):
    myStock.set_price(movement.move(myStock.price))


#visualization.start_graph(myStock.history)

print(myStock.price)
#print(myStock.history)
print(f"Mean price={myStock.avg_price()}")
print(f"Growth: {(myStock.price/myStock.start_price)}")