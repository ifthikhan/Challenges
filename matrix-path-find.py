#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple, OrderedDict

"""
Find all the possible paths from a beginning cell to the end cell in a matrix.

This is a brute force technique to check the rate of growth of number of paths
against the size of the matrix.
"""


def generate_matrix(num_rows, num_cols):
    """ Return a matrix which contains the matrix.

    :param num_rows: The number of rows.
    :type num_rows: int
    :param num_cols: The number of cols.
    :type num_cols: int
    :returns: list
    """
    size = num_rows * num_cols
    matrix = []
    for r in xrange(num_rows):
        start = r * num_cols
        stop = (r + 1) * num_cols
        ls = range(start, stop)
        matrix.append(ls)
    Matrix = namedtuple("Matrix", ["size", "rows", "cols", "matrix"])
    return Matrix(size=size, rows=num_rows, cols=num_cols, matrix=matrix)


def encode_to_flat_array_index(row, column, matrix):
    """ Encode the row, column value of a matrix cell into a flattened array.

    The row and column values are 0 indexed.

    :param row: The row number.
    :type row: int
    :param column: The column number.
    :type column: int
    :param matrix: The matrix object.
    :type matrix: object
    :returns: int -- index value of the flat array
    """
    return row * matrix.cols + column


def decode_to_matrix_cell(index, matrix):
    """Return the row and column for the given flattened array index

    :param index: The index number. (0 indexed)
    :type index: int
    :returns: tuple -- A tuple of row and col
    """
    row = index / matrix.cols
    col = index - (matrix.cols * row)
    return row, col,


def compute_neighbours(index, matrix):
    """Compute the neighbours for a given index in the matrix.

    The neighbours are the immediate cell to the right and below.

    :param index: The index number. (0 indexed)
    :type index: int
    :returns: tuple -- A tuple of left and below neighbour cells
    """
    row, col = decode_to_matrix_cell(index, matrix)
    n1 = index + 1
    if n1 >= matrix.size or col == matrix.cols - 1:
        n1 = None

    n2 = index + matrix.cols
    if n2 >= matrix.size or row == matrix.rows - 1:
        n2 = None
    return n1, n2,


def create_graph(matrix):
    """Return an ordered dict of graph.

    :param matrix: List of of lists.
    :type matrix: list
    :returns: OrderedDict
    """
    g = OrderedDict()
    for i in xrange(matrix.size):
        g[i] = []
        n1, n2 = compute_neighbours(i, matrix)
        if n1:
            g[i].append(n1)
        if n2:
            g[i].append(n2)
    return g


def find_all_paths(graph, start, end, path=[]):
    """Return a list of list of all paths

    :param graph:
    :type graph: OrderedDict
    :param start: Start index
    :type start: int
    :param end: end index
    :type end: int
    :param path: Path cells from start to end
    :type path: list
    :returns: List of lists
    """
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        newpaths = find_all_paths(graph, node, end, path)
        paths += newpaths
    return paths


def print_data(r, c):
    m = generate_matrix(r, c)
    g = create_graph(m)
    paths = find_all_paths(g, 0, m.size - 1)
    #import pprint; pprint.pprint(m.matrix)
    #import pprint; pprint.pprint(paths)
    output = """ \
matrix: {rows} x {cols} \
size: {size} \
paths: {num_paths} \
len: {each_path_len} \
ppc: {paths_per_cell}
""".format(rows=m.rows, cols=m.cols, size=m.size, num_paths=len(paths),
           each_path_len=len(paths[0]), paths_per_cell=len(paths)/m.size)
    print output


if __name__ == '__main__':
    for i in range(2, 14):
        print_data(i, i)
