# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:43:45 2020

@author: dennis
"""

from itertools import permutations

with open('data/day1.txt') as f:
    report = [int(x) for x in f.readlines()]

for perm in permutations(report, 2):
    if sum(perm) == 2020:
        break
print(f'Part 1: {perm[0] * perm[1]}')

for perm in permutations(report, 3):
    if sum(perm) == 2020:
        break
print(f'Part 1: {perm[0] * perm[1] * perm[2]}')
