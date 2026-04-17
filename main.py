from simulation import Simulation
from visualization import Visualization
from stock import Stock
from statistics import Statistics


visualization = Visualization()
myStock = Stock(100)
simulation = Simulation(myStock)
statistics = Statistics(myStock, simulation)

simulation.for_loop(265)

#visualization.line_graph(myStock.history)

print(myStock.price)
#print(myStock.history)
print(f"Mean price = {statistics.avg_price()}")
print(f"Growth: {statistics.growth()}")
print(f"Average growth over n tries: {statistics.avg_growth_over_n(10, 265)}")