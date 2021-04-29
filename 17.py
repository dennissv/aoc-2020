# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:07:36 2020

@author: dennis
"""

import numpy as np

def neighbours_3d(g, x, y, z):
    sum_ = 0
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if not dz and not dy and not dx:
                    continue
                try:
                    sum_ += g[z+dz, y+dy, x+dx]
                except:
                    pass
    return sum_

def neighbours_4d(g, x, y, z, w):
    sum_ = 0
    for dw in range(-1, 2):
        for dz in range(-1, 2):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if not dz and not dy and not dx and not dw:
                        continue
                    try:
                        sum_ += g[w+dw, z+dz, y+dy, x+dx]
                    except:
                        pass
    return sum_

l = [[1 if x == '#' else 0 for x in l] for l in open('data/17.txt').read().splitlines()]
grid = np.uint8([[[0]*len(l)]*(len(l)), l, [[0]*len(l)]*(len(l))])

for cycle in range(6):
    grid = np.pad(grid, ((1,1),(1,1),(1,1)))
    new_grid = grid.copy()
    for z in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            for x in range(grid.shape[2]):
                v = grid[z, y, x]
                n = neighbours_3d(grid, x, y, z)
                if v and not (n == 2 or n == 3):
                    new_grid[z, y, x] = 0
                elif not v and n == 3:
                    new_grid[z, y, x] = 1
    grid = new_grid.copy()
print(np.sum(grid))

l = [[1 if x == '#' else 0 for x in l] for l in open('data/17.txt').read().splitlines()]
grid = np.uint8([[[0]*len(l)]*(len(l)), l, [[0]*len(l)]*(len(l))])
fourth = np.uint8([[[0]*len(l)]*(len(l)), [[0]*len(l)]*(len(l)), [[0]*len(l)]*(len(l))])
grid = np.stack((fourth, grid, fourth))

for cycle in range(6):
    grid = np.pad(grid, ((1,1),(1,1),(1,1),(1,1)))
    new_grid = grid.copy()
    for w in range(grid.shape[0]):
        for z in range(grid.shape[1]):
            for y in range(grid.shape[2]):
                for x in range(grid.shape[3]):
                    v = grid[w, z, y, x]
                    n = neighbours_4d(grid, x, y, z, w)
                    if v and not (n == 2 or n == 3):
                        new_grid[w, z, y, x] = 0
                    elif not v and n == 3:
                        new_grid[w, z, y, x] = 1
    grid = new_grid.copy()
print(np.sum(grid))
