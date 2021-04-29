# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:05:14 2020

@author: dennis
"""

import numpy as np

grid = open('data/day3.txt').read().splitlines()
print(sum([grid[i][i*3%len(grid[0])] == '#' for i in range(1, len(grid))]))
print(np.prod([sum([grid[slope[1]*i][slope[0]*i%len(grid[0])] == '#' for i in range(slope[1], len(grid)//slope[1])]) for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]))
