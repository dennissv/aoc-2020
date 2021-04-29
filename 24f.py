# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:14:55 2020

@author: dennis
"""

EMPTY = {'e': None, 'w': None, 'se': None, 'nw': None, 'ne': None, 'sw': None}
OPPOSITES = {'e': 'w', 'w': 'e', 'se': 'nw', 'nw': 'se', 'ne': 'sw', 'sw': 'ne'}
N_DICT = {'w': ('se', 'ne'), 'e': ('nw', 'sw')}

class Tile:
    
    def __init__(self, id_, neighbours):
        self.id = id_
        self.neighbours = neighbours.copy()
        self.flipped = False
    
    def flip(self):
        self.flipped = not self.flipped
    
    def search_neighbours(self):
        for direction, neighbour in self.neighbours.items():
            if neighbour:
                pass

class Grid:
    
    def __init__(self):
        self.tiles = [Tile(0, EMPTY)]
        self.current = self.tiles[0]
    
    def reset(self):
        self.current = self.tiles[0]
    
    def move(self, direction):
        if self.current.neighbours[direction]:
            self.current = self.current.neighbours[direction]
        else:
            neighbours = EMPTY.copy()
            neighbours[OPPOSITES[direction]] = self.current
            self.tiles.append(Tile(len(self.tiles), neighbours))
            self.current = self.tiles[-1]
        self.current.search_neighbours()

def parse(l):
    instructions = []
    tmp = ''
    for x in l:
        tmp += x
        if x in OPPOSITES:
            instructions.append(tmp)
            tmp = ''
    return instructions

grid = Grid()

lines = open('data/24t.txt').read().splitlines()
for line in lines:
    instructions = parse(line)
    for instruction in instructions:
        grid.move(instruction)
    grid.current.flip()
    grid.reset()
print('Part 1:', sum(tile.flipped for tile in grid.tiles))
