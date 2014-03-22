"""
4-4. Assume that we are given n pairs of items as input, where the first item
is a number and the second item is one of three colors (red, blue, or yellow).
Further assume that the items are sorted by number. Give an O(n) algorithm to
sort the items by color (all reds before all blues before all yellows) such
that the numbers for identical colors stay sorted. For example: (1,blue), (3,red), (4,blue), (6,yellow), (9,red) should become (3,red), (9,red),
(1,blue), (4,blue), (6,yellow).
"""
from collections import namedtuple

Pair = namedtuple("Pair", ["num", "color"])

data = [(1,"blue"), (3,"red"), (4,"blue"), (6,"yellow"), (9,"red")]
# Transform the data into a tuple of namedtuples to make the code readable
data = [Pair(d[0], d[1]) for d in data]

order = {"red": 1, "blue": 2, "yellow": 3}

print data
low = 0
high = len(data) - 1

while low < high:
    dl = data[low]
    dh = data[high]
    if order[dl.color] > order[dh.color]:
        data[low] = dh
        data[high] = dl
    if order[data[low].color] in [2, 1]:
        low += 1
    if order[data[high].color] == 4:
        high -= 1

print data
