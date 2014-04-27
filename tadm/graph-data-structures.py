#!/usr/bin/env python
# encoding: utf-8

"""
5-8. Present correct and efficient algorithms to convert an undirected graph G
between the following graph data structures. You must give the time complexity
of each algorithm, assuming n vertices and m edges.
Convert from an adjacency matrix to adjacency lists.
Convert from an adjacency list to an incidence matrix. An incidence matrix M
has a row for each vertex and a column for each edge, such that M[i,j] = 1 if
vertex i is part of edge j, otherwise M[i,j] = 0.
Convert from an incidence matrix to adjacency lists.
"""

import unittest
from collections import defaultdict


def adjacency_matrix_to_adjacency_list(matrix):
    """Return an adjancency list by converting an adjacency matrix in
    n*(n+1)/2 time.

    :param matrix: Adjacency matrix
    :return: dict of list --  Adjacency list.
    """
    adjacency_list = defaultdict(list)
    row_len = len(matrix[0])
    nums_cols_to_iter = row_len
    for row_index, row in enumerate(matrix):
        start_from_col = row_len - nums_cols_to_iter
        for col_index, col_val in enumerate(row[start_from_col:],
                                            start_from_col):
            if row_index == col_index:
                continue
            if col_val:
                adjacency_list[row_index].append(col_index)
                adjacency_list[col_index].append(row_index)
        nums_cols_to_iter -= 1
    return dict(adjacency_list)


def adjacency_list_to_incident_matrix(adjacency_list):
    """Convert an adjacency list to incident matrix
    http://en.wikipedia.org/wiki/Incidence_matrix

    :param adjacency_list: A dict of lists
    :type adjacency_list: dictc
    :returns: list -- incident_matrix (list of lists)
    """
    list_len = len(adjacency_list)
    # Calculate the max number of edges in a graph of n vertices n*(n-1)/2
    max_edges = (list_len * (list_len - 1)) / 2
    incident_matrix = [[0] * list_len for _ in xrange(max_edges)]
    current_row = 0
    for parent_vertex, vertices in adjacency_list.iteritems():
        for child_vertex in vertices:
            # Since the graph is undirected we can ignore duplicating the edge.
            if child_vertex < parent_vertex:
                continue
            incident_matrix[current_row][parent_vertex] = 1
            incident_matrix[current_row][child_vertex] = 1
            current_row += 1
    return incident_matrix


def incident_matrix_to_adjacency_list(matrix):
    adjacency_list = defaultdict(list)
    def add_edge(x, y):
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    for vertices in matrix:
        pairs = []
        for index, v in enumerate(vertices):
            if v:
                pairs.append(index)
        add_edge(*pairs)
    return dict(adjacency_list)


class TestConversion(unittest.TestCase):

    def test_adjacenecy_matrix_to_adjacency_list(self):
       matrix = []
       matrix.append([0, 1, 1, 1, 1, 1])
       matrix.append([1, 0, 1, 1, 1, 1])
       matrix.append([1, 1, 0, 1, 1, 1])
       matrix.append([1, 1, 1, 0, 1, 1])
       matrix.append([1, 1, 1, 1, 0, 1])
       matrix.append([1, 1, 1, 1, 1, 0])

       r = adjacency_matrix_to_adjacency_list(matrix)
       expected_result = {0: [1, 2, 3, 4, 5],
                          1: [0, 2, 3, 4, 5],
                          2: [0, 1, 3, 4, 5],
                          3: [0, 1, 2, 4, 5],
                          4: [0, 1, 2, 3, 5],
                          5: [0, 1, 2, 3, 4]}
       self.assertEqual(r, expected_result)

    def test_adjacency_list_to_incident_matrix(self):
       adj_matrix = {0: [1, 2, 3, 4, 5],
                     1: [0, 2, 3, 4, 5],
                     2: [0, 1, 3, 4, 5],
                     3: [0, 1, 2, 4, 5],
                     4: [0, 1, 2, 3, 5],
                     5: [0, 1, 2, 3, 4]}
       expected_result = [[1, 1, 0, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0],
                          [1, 0, 0, 1, 0, 0],
                          [1, 0, 0, 0, 1, 0],
                          [1, 0, 0, 0, 0, 1],
                          [0, 1, 1, 0, 0, 0],
                          [0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 1],
                          [0, 0, 1, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0],
                          [0, 0, 1, 0, 0, 1],
                          [0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 1, 0, 1],
                          [0, 0, 0, 0, 1, 1]]
       self.assertEqual(expected_result,
                        adjacency_list_to_incident_matrix(adj_matrix))
       import pprint; pprint.pprint(adjacency_list_to_incident_matrix(adj_matrix))

    def test_incident_matrix_to_adjacency_list(self):
       incident_matrix = [[1, 1, 0, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0],
                          [1, 0, 0, 1, 0, 0],
                          [1, 0, 0, 0, 1, 0],
                          [1, 0, 0, 0, 0, 1],
                          [0, 1, 1, 0, 0, 0],
                          [0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 1],
                          [0, 0, 1, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0],
                          [0, 0, 1, 0, 0, 1],
                          [0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 1, 0, 1],
                          [0, 0, 0, 0, 1, 1]]
       expected_result = {0: [1, 2, 3, 4, 5],
                          1: [0, 2, 3, 4, 5],
                          2: [0, 1, 3, 4, 5],
                          3: [0, 1, 2, 4, 5],
                          4: [0, 1, 2, 3, 5],
                          5: [0, 1, 2, 3, 4]}
       r = incident_matrix_to_adjacency_list(incident_matrix)
       import pprint; pprint.pprint(r)
       self.assertEqual(expected_result, r)


if __name__ == '__main__':
    unittest.main()
