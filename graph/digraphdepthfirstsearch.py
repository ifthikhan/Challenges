"""
Depth first search algorithm implementation.
"""

from digraph import DiGraph, get_populated_graph
from depthfirstsearch import DepthFirstSearchPaths


if __name__ == '__main__':
    g = get_populated_graph()
    path = DepthFirstSearchPaths(g, 0)
    print "Has path to: %s" % path.has_path_to(5)
    print "Path: %s" % path.path_to(5)
