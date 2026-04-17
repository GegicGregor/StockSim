import plotly.express as px

class Visualization:
    def __init__(self):
        pass
    def line_graph(self, data):
        fig = px.line(x=None, y=data)
        fig.show()

    def update_graph(self):
        pass

