# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:28:11 2020

@author: dennis
"""

import math

card_public, door_public = [int(x) for x in open('data/25.txt').read().splitlines()]
card_loop_size = 0
door_loop_size = 0

loop_size = 1
while not card_loop_size and not door_loop_size:
    value = pow(7, loop_size, 20201227)
    if value == card_public:
        card_loop_size = loop_size
        print('Found card loop size')
    if value == door_public:
        door_loop_size = loop_size
        print('Found door loop size')
    loop_size += 1

if card_loop_size:
    encryption = pow(door_public, card_loop_size, 20201227)
elif door_loop_size:
    encryption = pow(card_public, door_loop_size, 20201227)
print('Encryption key:', encryption)
