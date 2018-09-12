from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, coor):
        return self.edges[coor]

    def get_cost(self, from_coor, to_coor):
        return self.weights[(from_coor + to_coor)]

def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, coor = queue.get()
        if coor not in visited:
            visited.add(coor)

            if coor == goal:
                return
            for i in up,down,left,right:
                if i not in visited:
                    total_cost = cost + min(direction)
                    path = 
                    queue.put((total_cost, i))

coor1 = Graph()
coor1.neighbors(2)

