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
        
"""
Sample output for 
matrix: 2 x 2   size: 4   paths: 2       len: 3 ppc: 0
matrix: 3 x 3   size: 9   paths: 6       len: 5 ppc: 0
matrix: 4 x 4   size: 16  paths: 20      len: 7 ppc: 1
matrix: 5 x 5   size: 25  paths: 70      len: 9 ppc: 2
matrix: 6 x 6   size: 36  paths: 252     len: 11 ppc: 7
matrix: 7 x 7   size: 49  paths: 924     len: 13 ppc: 18
matrix: 8 x 8   size: 64  paths: 3432    len: 15 ppc: 53
matrix: 9 x 9   size: 81  paths: 12870   len: 17 ppc: 158
matrix: 10 x 10 size: 100 paths: 48620   len: 19 ppc: 486
matrix: 11 x 11 size: 121 paths: 184756  len: 21 ppc: 1526
matrix: 12 x 12 size: 144 paths: 705432  len: 23 ppc: 4898
matrix: 13 x 13 size: 169 paths: 2704156 len: 25 ppc: 16000
"""
