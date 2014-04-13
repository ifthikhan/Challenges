#!/usr/bin/env python

"""
Give an efficient algorithm to find the second-largest key among n keys. You
can do better than 2n − 3 comparisons.
"""

def _generate_tournament_table(ls):
    """Return the tourname table for a given list.

    :returns: list
    """
    if len(ls) == 1:
        return [ls]
    result = []
    for i in range(len(ls))[::2]:
        if i == len(ls) - 1:
            result.append(ls[i])
        elif ls[i] < ls[i+1]:
            result.append(ls[i])
        else:
            result.append(ls[i+1])
    s = _generate_tournament_table(result)
    s.append(result)
    return s


def find_second_largest(ls):
    t_table = _generate_tournament_table(ls)
    t_table.pop(0)


if __name__ == "__main__":
    ls = [3, 2, 5, 1, 4, 7, 9, 6]
    ls = [2, 14, 15, 13, 1, 8, 17, 10, 6, 12, 9, 4, 11, 15, 3]
    l2 = _generate_tournament_table(ls)
    l2.pop(0)
    print l2
    mini = None
    left, right = None, None
    for l in l2:
        if mini is None:
            mini = l[0]
        elif len(l) == 2:
            if l[0] == mini:
                left = True
            else:
                right = True

