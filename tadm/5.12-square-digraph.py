#!/usr/bin/env python
# encoding: utf-8

"""
Square a digraph. squaring when using adjacency list to the adjacent vertices.
"""

from collections import OrderedDict, defaultdict
import unittest


class DiGraph(object):

    def __init__(self, size):
        self.size = size
        self.g = OrderedDict()
        for i in range(size):
            self.g[i] = []

    def add_edge(self, s, d):
        if self.connected(s, d):
            return
        self.g[s].append(d)

    def connected(self, s, d):
        for v in self.vertices(s):
            if d == v:
                return True
        return False

    def vertices(self, v):
        return self.g[v]

    def __str__(self):
        out = []
        for k, children in self.g.iteritems():
            out.append("{} -> {}".format(k, children))
        return "\n".join(out)

    def __iter__(self):
        for k, v in self.g.iteritems():
            yield k, v


def square_digraph(graph, root):
    # Stores the adjacent vertices as key and its incoming edges as a list
    # since a single adjacent vertex can have multiple incoming edges.
    incoming_edges = defaultdict(list)
    stack = [root]
    while len(stack):
        current_vertex = stack.pop(0)
        adjacent_vertices = graph.vertices(current_vertex)
        if incoming_edges.has_key(current_vertex) and adjacent_vertices:
            # A child can have multiple parent vertices
            second_level_ancestors = incoming_edges.pop(current_vertex)
            for sla in second_level_ancestors:
                for adjacent_vertex in adjacent_vertices:
                    graph.add_edge(sla, adjacent_vertex)
        if adjacent_vertices:
            for adjacent_vertex in adjacent_vertices:
                incoming_edges[adjacent_vertex].append(current_vertex)
            stack += adjacent_vertices


class TestSquareDigraph(unittest.TestCase):

    def test_square_digraph(self):
        graph = DiGraph(8)
        edges = [(1, 2,), (1, 7,), (2, 3,), (2, 4,), (3, 5,), (3, 4,),
                 (4, 7,), (4, 6,), (6, 5,), (7, 6,)]
        expected_result = {0: [],
                           1: [2, 7, 3, 4, 6],
                           2: [3, 4, 5, 7, 6],
                           3: [5, 4, 7, 6],
                           4: [7, 6, 5],
                           5: [],
                           6: [5],
                           7: [6, 5]}
        for s, d in edges:
            graph.add_edge(s, d)
        square_digraph(graph, 1)
        for v, adjacents in graph:
            if sorted(adjacents) != sorted(expected_result[v]):
                assert False
        assert True


if __name__ == '__main__':
    unittest.main()
