#!/usr/bin/env python
"""
Calculating fibonacci numbers using memoization
"""

def fib(n):
    if n in fib.cache.keys():
        return fib.cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fib(n-2) + fib(n - 1)
    fib.cache[n] = result
    return result
fib.cache = {}

l = []
for i in range(1, 30):
    l.append(fib(i))

print l
