# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:29:26 2020

@author: dennis
"""

from itertools import combinations

l = [int(x) for x in open('data/9.txt').read().splitlines()]

def is_sum(p, x):
    if x in {sum(comb) for comb in combinations(p, 2)}:
        return True
    return False

ans1 = [l[i] for i in range(25, len(l)) if not is_sum(l[i-25:i], l[i])][0]
print('Part 1:', ans1)

def part2():
    for length in range(2, len(l)):
        for i in range(len(l) - length):
            if sum(l[i:i+length]) == ans1:
                return min(l[i:i+length]) + max(l[i:i+length])
print('Part 2:', part2())
