# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:04:49 2020

@author: dennis
"""

import re

valid_p1 = 0
valid_p2 = 0
with open('data/day2.txt') as f:
    for line in f.readlines():
        i1, i2, letter, _, password = re.split('[ :-]', line.strip())
        if password.count(letter) in range(int(i1), int(i2) + 1):
            valid_p1 += 1
        if (password[int(i1) - 1] == letter) ^ (password[int(i2) - 1] == letter):
            valid_p2 += 1
print(f'Part 1: {valid_p1}')
print(f'Part 2: {valid_p2}')
