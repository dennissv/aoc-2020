# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:22:45 2020

@author: dennis
"""

import numpy as np

def adjacent(g, x, y):
    sum_ = 0
    for i in range(max(0, y-1), min(g.shape[0], y+2)):
        for j in range(max(0, x-1), min(g.shape[1], x+2)):
            if i == y and j == x:
                continue
            symbol = g[i][j]
            if symbol == 1:
                sum_ += 1
    return sum_

def score_line(l):
    for x in l:
        if x == 1:
            return 1
        if x == 0:
            return 0
    return 0

def visible(g, x, y):
    sum_ = 0
    sum_ += score_line(g[y, x+1:])
    sum_ += score_line(g[y, :x][::-1])
    
    sum_ += score_line(g[y+1:, x])
    sum_ += score_line(g[:y, x][::-1])
    
    # diag1 = g.diagonal(x-y)
    # return diag1
    # diag2 = np.fliplr(g).diagonal((g.shape[1]-x)-y)
    # oh no
    
    i = x-1
    j = y-1
    while i >= 0 and j >= 0:
        if g[j, i] == 1:
            sum_ += 1
            break
        elif not g[j, i]:
            break
        i -= 1
        j -= 1
    
    i = x+1
    j = y+1
    while i < g.shape[1] and j < g.shape[0]:
        if g[j, i] == 1:
            sum_ += 1
            break
        elif not g[j, i]:
            break
        i += 1
        j += 1
        
    i = x+1
    j = y-1
    while i < g.shape[1] and j >= 0:
        if g[j, i] == 1:
            sum_ += 1
            break
        elif not g[j, i]:
            break
        i += 1
        j -= 1
    
    i = x-1
    j = y+1
    while i >= 0 and j < g.shape[0]:
        if g[j, i] == 1:
            sum_ += 1
            break
        elif not g[j, i]:
            break
        i -= 1
        j += 1

    return sum_

def simulate(grid, part):
    pass

lines = open('data/11.txt').read().splitlines()
np_dict = {'.': -1, 'L': 0, '#': 1}

grid = np.array([[np_dict[x] for x in row] for row in lines])
c = 0
while 1:
    c += 1
    old_grid = grid.copy()
    new_grid = []
    for y in range(grid.shape[0]):
        new_row = []
        for x in range(grid.shape[1]):
            symbol = grid[y][x]
            score = adjacent(grid, x, y)
            if symbol == 0 and score == 0:
                new_row.append(1)
            elif symbol == 1 and score >= 4:
                new_row.append(0)
            else:
                new_row.append(symbol)
        new_grid.append(new_row)
    new_grid = np.array(new_grid)
    grid = new_grid.copy()
    if np.array_equal(old_grid, new_grid):
        break
print(sum(sum(1 if x == 1 else 0 for x in row) for row in grid))

grid = np.array([[np_dict[x] for x in row] for row in lines])
c = 0
while 1:
    c += 1
    old_grid = grid.copy()
    new_grid = []
    for y in range(grid.shape[0]):
        new_row = []
        for x in range(grid.shape[1]):
            symbol = grid[y][x]
            score = visible(grid, x, y)
            if symbol == 0 and score == 0:
                new_row.append(1)
            elif symbol == 1 and score >= 5:
                new_row.append(0)
            else:
                new_row.append(symbol)
        new_grid.append(new_row)
    new_grid = np.array(new_grid)
    grid = new_grid.copy()
    if np.array_equal(old_grid, new_grid):
        break
print(sum(sum(1 if x == 1 else 0 for x in row) for row in grid))
