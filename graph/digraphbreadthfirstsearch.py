"""
Breadth first search algorithm
"""

from digraph import get_populated_graph
from breadthfirstsearch import BreadthFirstSearchPaths


if __name__ == '__main__':
    g = get_populated_graph()
    path = BreadthFirstSearchPaths(g, 0)
    print "Has path to: %s" % path.has_path_to(5)
    print "Path: %s" % path.path_to(5)
