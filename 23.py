# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:18:18 2020

@author: dennis
"""

from collections import deque

cups = [int(x) for x in '247819356']
# cups = [int(x) for x in '389125467']
for i in range(100):
    # print('Move:', i+1)
    i %= len(cups)
    current = cups[i]
    # print('Current:', current)
    # print(cups)
    if i < 6:
        pickup = cups[i+1:i+4]
    else:
        pickup = cups[i+1:]
        pickup += cups[:3-len(pickup)]
    for x in pickup:
        cups.remove(x)
    for j in range(1, 9):
        destination = (current - j) % 10
        if destination in cups:
            # print(pickup)
            # print(destination)
            destination = cups.index(destination)
            cups = cups[:destination+1] + pickup + cups[destination+1:]
            cups = deque(cups)
            while cups[i] != current:
                cups.rotate(1)
            cups = list(cups)
            break
    # print()
print('Part 1:', ''.join(str(x) for x in cups[cups.index(1)+1:]) + ''.join(str(x) for x in cups[:cups.index(1)]))
