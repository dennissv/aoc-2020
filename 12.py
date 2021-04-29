# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:32:39 2020

@author: dennis
"""

import numpy as np

class Position:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Position(self.x * scalar, self.y * scalar)

class Ship:

    def __init__(self, waypoint=None):
        self.waypoint = waypoint
        self.waypoint_quadrant = 0
        self.direction = 90
        self.position = Position(0, 0)
        self.direction_dict = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
        self.position_dict = {0: Position(0, 1), 180: Position(0, -1), 
                              90: Position(1, 0), 270: Position(-1, 0)}

    def process_instruction(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])

        if not self.waypoint:
            if action == 'L':
                self.direction -= value
                self.direction %= 360
            elif action == 'R':
                self.direction += value
                self.direction %= 360
            elif action == 'F':
                self._move(self.direction, value)
            else:
                self._move(self.direction_dict[action], value)
        
        elif self.waypoint:
            if action in 'LR':
                self._rotate_waypoint(action, value)
            elif action == 'F':
                self._move(self.direction, value)
            else:
                self._move_waypoint(self.direction_dict[action], value)

    def _move(self, direction, value):
        if not self.waypoint:
            self.position += self.position_dict[direction] * value
        else:
            self.position += self.waypoint * value

    def _move_waypoint(self, direction, value):
        self.waypoint += self.position_dict[direction] * value
    
    def _rotate_waypoint(self, direction, value):
        if direction == 'R':
            value = 360 - value
        angle = np.deg2rad(value)
        x = self.waypoint.x
        y = self.waypoint.y
        self.waypoint.x = int(round(x*np.cos(angle) - y*np.sin(angle)))
        self.waypoint.y = int(round(x*np.sin(angle) + y*np.cos(angle)))

instructions = open('data/12.txt').read().splitlines()

ship = Ship()
for instruction in instructions:
    ship.process_instruction(instruction)
print('Part 1:', abs(ship.position.x)+abs(ship.position.y))

ship = Ship(waypoint=Position(10, 1))
for instruction in instructions:
    ship.process_instruction(instruction)
print('Part 2:', abs(ship.position.x)+abs(ship.position.y))
