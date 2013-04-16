"""
Depth first search algorithm implementation.
"""

from collections import OrderedDict

from graph import Graph


class DepthFirstSearchPaths(object):

    def __init__(self, graph, s):
        assert isinstance(graph, Graph)
        self.graph = graph
        self.s = s
        self.marked = OrderedDict.fromkeys(self.graph.vertices, value=False)
        self.edge_to = OrderedDict.fromkeys(self.graph.vertices, value=None)
        self.__dfs(s)

    def __dfs(self, v):
        self.marked[v] = True
        for w in self.graph.adjacent(v):
            if self.marked[w]:
                continue
            self.__dfs(w)
            self.edge_to[w] = v

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if self.has_path_to(v) is False:
            return []
        path = []
        w = v
        while True:
            path.append(w)
            w = self.edge_to[w]
            if w is None:
                break
        return path


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

    path = DepthFirstSearchPaths(g, 0)
    print "Has path to: %s" % path.has_path_to(5)
    print "Path: %s" % path.path_to(5)
