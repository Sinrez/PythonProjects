class Graph:
    def set_data(self,data):
        self.data = data
        
    def draw(self):
        LIMIT_Y = [0, 10]
        print(*[d for d in self.data if LIMIT_Y[0]<=d<=LIMIT_Y[1]])
        
graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()