# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:55:49 2020

@author: dennis
"""

numbers = [1, 20, 8, 12, 0, 14]

used = {v: [i+1] for i, v in enumerate(numbers)}
used[0].append(len(numbers) + 1)
turn = len(numbers) + 2
spoken = 0
while turn <= 30000000:
    if spoken in used:
        if len(used[spoken]) >= 2:
            difference = used[spoken][-1] - used[spoken][-2]
            spoken = difference
        else:
            spoken = 0
    else:
        spoken = 0
    if spoken in used:
        used[spoken].append(turn)
    else:
        used[spoken] = [turn]
    if turn == 2020:
        print('Part 1:', spoken)
    turn += 1
print('Part 2:', spoken)
