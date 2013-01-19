#!/usr/bin/env python

"""
Print a pyramid for the given height
"""

import sys


def pyramid(rows):
    previous = 0
    for i in range(1, rows + 1):
        yield " " * (rows - i) + "*" * (i + previous)
        previous = i


if __name__ == "__main__":
    try:
        rows = int(sys.argv[1])
    except (IndexError, ValueError):
        rows = 8
        print ">> Printing 8 rows as the default pyramid"

    for line in pyramid(rows):
        print line
