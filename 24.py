# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:14:55 2020

@author: dennis
"""

import numpy as np

def parse(l):
    instructions = []
    tmp = ''
    for x in l:
        tmp += x
        if x in vectors:
            instructions.append(tmp)
            tmp = ''
    return instructions

grid_size = 250
grid = np.zeros((grid_size, grid_size))
pos = np.array([grid_size // 2, grid_size // 2])
vectors = {'w': [-2, 0], 'e': [2, 0], 'nw': [-1, -1], 'sw': [-1, 1], 'ne': [1, -1], 'se': [1, 1]}
vectors = {key: np.array(value) for key, value in vectors.items()}

lines = open('data/24.txt').read().splitlines()
for line in lines:
    instructions = parse(line)
    for instruction in instructions:
        pos += vectors[instruction]
    grid[pos[1], pos[0]] = int(not grid[pos[1], pos[0]])
    pos = np.array([grid_size // 2, grid_size // 2])
print('Part 1:', np.sum(grid, dtype=int))

for day in range(100):
    ng = np.int32(grid.copy())
    sums = np.zeros((grid.shape[0], grid.shape[1]), dtype=np.int32)
    w = np.where(grid == 1)
    for y, x in zip(w[0], w[1]):
        pos = np.int32([x, y])
        for vector in vectors.values():
            dx, dy = pos + vector
            sums[dy, dx] += 1
    for y in range(sums.shape[0]):
        for x in range(sums.shape[1]):
            v = grid[y, x]
            s = sums[y, x]
            if v and ((not s) or  (s > 2)):
                ng[y, x] = 0
            elif not v and s == 2:
                ng[y, x] = 1
    grid = ng.copy()
print('Part 2:', np.sum(grid, dtype=int))
