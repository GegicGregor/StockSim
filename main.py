from simulation import Simulation
from visualization import Visualization
from stock import Stock


visualization = Visualization()
myStock = Stock()
simulation = Simulation(myStock)

simulation.for_loop(200)

visualization.start_graph(myStock.history)

print(myStock.price)
print(myStock.history)
print(f"Mean price={myStock.avg_price()}")
print(f"Growth: {(myStock.price/myStock.start_price)}")