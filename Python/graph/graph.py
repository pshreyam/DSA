class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Vertex: <{self.data}>'


class Edge:
    ''' Edges with two vertices and the corresponding weight '''
    def __init__(self, vertex_1, vertex_2, weight):
        self.start = vertex_1
        self.end = vertex_2
        self.weight = weight

    def __repr__(self):
        return f'Edge: {self.start} -> {self.end}'


class Graph:
    def __init__(self):
        self.edges_list = []
    
    def add_edges(self, *edges):
        for edge in edges:
            self.edges_list.append(edge)

    def show_graph(self):
        for edge in self.edges_list:
            print(f'({edge.start.data}) -- {edge.weight} --> ({edge.end.data})')


if __name__ == '__main__':
    g = Graph()
    
    v1 = Vertex('Kathmandu')
    v2 = Vertex('Nepalgunj')
    v3 = Vertex('Biratnagar')

    e1 = Edge(v1, v2, 521)
    e2 = Edge(v2, v3, 761)
    e3 = Edge(v3, v1, 377)

    g.add_edges(e1, e2, e3)

    g.show_graph()