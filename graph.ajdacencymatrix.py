class Graph:
    def __init__(self, size):
        self.dic = {"s": 0, "sa": 1, "k": 2, "p": 3, "r": 4, "v": 5}
        self.graph = [[0] * size for i in range(size)]

    def insert(self, u, v):
        row, col = self.dic[u], self.dic[v]
        self.graph[row][col] = 1
        self.graph[col][row] = 1


obj = Graph(6)
obj.insert("s", "sa")
obj.insert("s", "r")
obj.insert("s", "p")
obj.insert("s", "k")
obj.insert("sa", "k")
obj.insert("r", "v")
obj.insert("sa", "p")

for i in range(6):
    print(obj.graph[i])
