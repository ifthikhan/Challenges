#!/usr/bin/env python

from random import shuffle


def merge_sort(items):
    if len(items) == 1:
        return items

    mid = len(items) / 2
    s1 = merge_sort(items[:mid])
    s2 = merge_sort(items[mid:])
    merged = _merge(s1, s2)
    return merged


def _merge(ls1, ls2):
    merged = []
    i, j = 0, 0
    while True:
        if ls1[i] <= ls2[j]:
            merged.append(ls1.pop(i))
        else:
            merged.append(ls2.pop(j))
        if not len(ls1) or not len(ls2):
            break
    if not len(ls1):
        merged += ls2
    elif not len(ls2):
        merged += ls1
    return merged


if __name__ == '__main__':
    ls = range(2000000)
    shuffle(ls)
    #print "Before sorting: %s" % ls
    merged = merge_sort(ls)
    #print "After sorting: %s" % merged
