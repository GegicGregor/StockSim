from stock import Stock
from movement import Movement
myStock = Stock()
movement = Movement()
while myStock.price <= 150:
    print(myStock.price)
    myStock.set_price(movement.move(myStock.price, True))

print(myStock.price)