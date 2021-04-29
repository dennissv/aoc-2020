# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:00:06 2020

@author: dennis
"""

import math

l = [int(x) for x in open('data/10.txt').read().splitlines()]
l = l + [0, max(l) + 3]
l.sort()
differences = [l[i] - l[i-1] for i in range(1, len(l))]
print('Part 1:', differences.count(1) * differences.count(3))

products = []
i = 0
sequence = {1: 1, 2: 2, 3: 4, 4: 7}
while i < len(differences) - 1:
    for j in range(i + 2, len(differences) + 1):
        if not sum(differences[i:j]) == j - i:
            n = j - i - 1
            products.append(sequence[n])
            i = j - 1
            break
print('Part 2:', math.prod(products))
