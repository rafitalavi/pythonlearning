from collections import defaultdict
from queue import PriorityQueue


class Graph:
    def __init__(self, directed): 
        """Parametrized constructor of class Graph 
        which takes True if Graph is directed otherwise it takes False"""
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        """Add Edges between two nodes along 
        with weight as Algorithm is of UCS"""
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        """It takes starting node and 
        goal node as parameters then it returns 
        a path using Uniform Cost Search Algorithm"""
        visited = []  
        queue = PriorityQueue()
        queue.put((0, current_node))
        
        while not queue.empty():
            item = queue.get()
            current_node =  item[1]
            
            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                    
                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))


if __name__ == "__main__":
    directed_input = input("Is the graph directed? (y/n): ")
    directed = directed_input.lower() == 'y'
    g = Graph(directed)

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter edge (source destination weight): ").split()
        g.add_edge(u, v, int(weight))

    start_node = input("Enter the starting node: ")
    goal_node = input("Enter the goal node: ")

    g.ucs(start_node, goal_node)

