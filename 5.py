# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:50:42 2020

@author: dennis
"""

lines = open('data/day5.txt').read().splitlines()
ids = {int(''.join('0' if x in 'LF' else '1' for x in line), 2) for line in lines}
print('Part 1:', max(ids))
print('Part 2:', *[x for x in range(min(ids), max(ids)) if x not in ids])
