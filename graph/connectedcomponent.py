"""
Algorithm to query whether two vertices are connected. The connection check can
be performed in constant time.

The algorithm works by creating equivalence relations of all the vertices
which are connected to each other.
"""

from collections import OrderedDict

from graph import Graph


class ConnectedComponents(object):

    def __init__(self, graph):
        assert isinstance(graph, Graph)
        self.graph = graph
        self.count = 0
        self.marked = OrderedDict.fromkeys(self.graph.vertices, False)
        self.connections = OrderedDict.fromkeys(self.graph.vertices, None)

        for v in self.graph.vertices:
            if self.marked[v] is True:
                continue
            self.__dfs(v)
            self.count += 1

    def __dfs(self, v):
        self.marked[v] = True
        for adj in self.graph.adjacent(v):
            if self.marked[adj] is True:
                continue
            self.__dfs(adj)
        self.connections[v] = self.count

    def connected(self, v, w):
        return True if self.connections[v] == self.connections[w] else False

    @property
    def num_components(self):
        """
        Returns the number of components in the equivalence relations.
        """
        return self.count

    def component_id(self, v):
        """
        Returns the equivalence relation component id for a given vertices
        """
        return self.connections[v]


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

    cc = ConnectedComponents(g)

    print "Is 0 and 3 connected: %s" % cc.connected(0, 3)
    print "The connected component of 0: %d" % cc.component_id(0)
    print "The connected component of 3: %d" % cc.component_id(3)

    print "Is 0 and 12 connected: %s" % cc.connected(0, 12)
    print "The connected component of 0: %d" % cc.component_id(0)
    print "The connected component of 12: %d" % cc.component_id(12)
