# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 00:55:36 2020

@author: dennis
"""

def mask_value(mask, value):
    value = [x for x in '{:036b}'.format(value)]
    value = [m if m.isdigit() else v for v, m in zip(value, mask)]
    return int(''.join(value), 2)

def mask_adress(mask, adress, value, memory):
    count = mask.count('X')
    adress = [x for x in '{:036b}'.format(adress)]
    adress = [a if m == '0' else m for a, m in zip(adress, mask)]
    for x in range(2**count):
        combination = bin(x)[2:].zfill(count)
        new_adress = ''.join(adress)
        for y in combination:
            new_adress = new_adress.replace('X', y, 1)
        new_adress = int(new_adress, 2)
        memory[new_adress] = value

instructions = open('data/14.txt').read().splitlines()

memory = dict()
memory2 = dict()
bitmask = 'X'*36
for instruction in instructions:
    instruction = instruction.split()
    if instruction[0].startswith('mem'):
        adress = int(instruction[0][4:-1])
        value = int(instruction[-1])
        memory[adress] = mask_value(bitmask, value)
        mask_adress(bitmask, adress, value, memory2)
    else:
        bitmask = instruction[-1]
print('Part 1:', sum(memory.values()))
print('Part 2:', sum(memory2.values()))
