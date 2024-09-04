#What is Graph? - Graph is collection of nodes(Vertices) And Edges that connect Pairs of Nodes

# Graph are used to represent relationships and connections between entities making them incredibly versitile for modeling real world application
# Vertices - Each Vertex reprresent Data point
# Edges - Connection or link between the vertex(Data point)

# Directed vs. Undirected graph
# - Directed => In directed graph, Edges have direction
# - Undirected => In undirected graph, edges do not have direction, You can travel between vertex in bidirectional way

# Weighted vs. Unweighted
# - Weighted  - Edges have costs or weights associated with it
# - Unweighted - Edges are considered Equal and there is no weights or cost associated with it  

#Adjacency Matrix vs. Adjacency List
# Adjacency Matrix - A 2D array where each cell (i, j) represents a presence or absence of edge between vetex i and vertex j
# Adjacency List - A collection of list where each list corresponds to vertex and contain a list of its adjecnt vertices

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        #Check if vertex is graph, if not , add vertex to graph as an empty lis
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add the vertex to graph if there is no vertex
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        
        #Connect the vertices
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex} => {self.graph[vertex]}")

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# g.display()




#Graph Represantion using Adjacency Matrix
class matrix_graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    def add_Edges(self, v, u, directed=False):

        if u >= self.num_nodes or v >= self.num_nodes:
            raise ValueError("Node index out of range")
        if not directed:
            self.matrix[v][u] = 1
        self.matrix[u][v] = 1
    
    def display(self):
        for row in self.matrix:
            print(row)

grm = matrix_graph(5)
grm.add_Edges(0, 1)
grm.add_Edges(0, 2)
grm.add_Edges(1, 2)
grm.add_Edges(1, 3)
grm.add_Edges(2, 4)
grm.add_Edges(3, 4)
grm.display()