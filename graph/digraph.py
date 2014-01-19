"""
A representation of digraph data structure
"""


from collections import OrderedDict


class DiGraph(object):
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
        Adds an edge connecting the two vertices. The connection is made only
        1 way from v to w.
        """
        self.g[v].append(w)
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

    @property
    def reverse(self):
        """
        Returns a reversed version of the edges of the graph.
        """
        g = DiGraph(self.vertices)
        for v in self.vertices:
            for adj in self.adjacent(v):
                g.add_edge(adj, v)
        return g

    def __len__(self):
        return self.num_vertices

    def __str__(self):
        s = []
        for v, adjs in self.g.items():
            s.append("{} -> {}".format(v, str(adjs)))
        return "\n".join(s)


def degree(graph, v):
    """Returns the degree for the given vertices."""
    assert isinstance(g, DiGraph)
    return len(graph.adjacent_nodes(v))


def get_populated_graph():
    g = DiGraph(range(13))
    g.add_edge(0, 5)
    g.add_edge(0, 1)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(3, 2)
    g.add_edge(4, 3)
    g.add_edge(4, 2)
    g.add_edge(5, 4)
    g.add_edge(6, 9)
    g.add_edge(6, 4)
    g.add_edge(6, 8)
    g.add_edge(6, 0)
    g.add_edge(7, 6)
    g.add_edge(7, 9)
    g.add_edge(8, 6)
    g.add_edge(9, 11)
    g.add_edge(9, 10)
    g.add_edge(10, 12)
    g.add_edge(11, 4)
    g.add_edge(11, 12)
    g.add_edge(12, 9)
    return g

if __name__ == '__main__':
    g = get_populated_graph()
    print "Num vertices: %d" % g.num_vertices
    print "Num edges: %d" % g.num_edges
    print "Graph: \n %s" % g
    print "Reversed: \n %s" % g.reverse
