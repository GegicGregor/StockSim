import plotly.express as px
from stock import Stock

myStock = Stock()

class Visualization:
    def __init__(self):
        pass
    def start_graph(self, data):
        fig = px.line(x=None, y=data)
        fig.show()

    def update_graph(self):
        pass

