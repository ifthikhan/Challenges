"""
A representation of graph data structure
"""


from collections import OrderedDict


class Graph(object):
    """
    Comprises of nodes and their connections
    """

    #TODO: Support argument unpacking
    def __init__(self, vertices):
        self.g = self.__construct(vertices)
        self.__num_edges = 0
        self.__vertices = vertices

    def __construct(self, vertices):
        g = OrderedDict()
        for v in vertices:
            g[v] = []
        return g

    def add_edge(self, v, w):
        """
        Adds an edge connecting the two vertices
        """
        self.g[v].append(w)
        #self.g[w].append(v)
        self.__num_edges += 1

    def adjacent(self, v):
        """
        Returns a list of adjacent vertices to the given vertex
        """
        return tuple(self.g[v])

    @property
    def vertices(self):
        """Returns all the vertices in the graph."""
        return self.__vertices

    @property
    def num_vertices(self):
        return len(self.g)

    @property
    def num_edges(self):
        return self.__num_edges

    def __len__(self):
        return self.num_vertices

    def __str__(self):
        s = []
        for v, adjs in self.g.items():
            s.append("{} -> {}".format(v, str(adjs)))
        return "\n".join(s)


def degree(graph, v):
    """Returns the degree for the given vertices."""
    assert isinstance(g, Graph)
    return len(graph.adjacent_nodes(v))


if __name__ == '__main__':
    g = Graph(range(13))
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 6)
    g.add_edge(0, 5)
    g.add_edge(6, 4)
    g.add_edge(5, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(7, 8)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(9, 12)
    g.add_edge(11, 12)
    print "Num vertices: %d" % g.num_vertices
    print "Num edges: %d" % g.num_edges
    print "Graph: %s" % g
