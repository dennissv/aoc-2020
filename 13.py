# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:09:11 2020

@author: dennis
"""

with open('data/13.txt') as f:
    earliest = int(f.readline())
    buses = [x for x in f.readline().strip().split(',')]

p1 = [int(x) for x in buses if x.isdigit()]
arrivals = [(earliest // x) * x + x for x in p1]
print('Part 1:', p1[arrivals.index(min(arrivals))] * (min(arrivals) - earliest))

p2 = [(int(x), i) for i, x in enumerate(buses) if x.isdigit()]
step = p2[0][0]
start = p2[0][1]
for v, offset in p2[1:]:
    x = start
    t = []
    while 1:
        x += step
        if not ((x+offset) % v):
            t.append(x)
        if len(t) == 2:
            break
    start, step = t
    step -= start
print('Part 2:', start)
