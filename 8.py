# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:47:55 2020

@author: dennis
"""

lines = open('data/8.txt').read().splitlines()

def execute(code):
    visited = set()
    pointer, acc = 0, 0
    while pointer not in visited:
        visited.add(pointer)
        if code[pointer][:3] == 'jmp':
            pointer += int(code[pointer][4:]) - 1
        elif code[pointer][:3] == 'acc':
            acc += int(code[pointer][4:])
        pointer += 1
        if pointer == len(code):
            return acc, 0 # acc value, no loop detected
    return acc, 1 # acc value, loop detected

def modify(code, line):
    modified_code = code.copy()    
    if code[line].startswith('jmp'):
        modified_code[line] = 'nop' + code[line][3:]
    elif code[line].startswith('nop'):
        modified_code[line] = 'jmp' + code[line][3:]
    return modified_code

acc, _ = execute(lines)
print('Part 1:', acc)

for i in range(len(lines)):
    acc, loop = execute(modify(lines, i))
    if not loop:
        print('Part 2:', acc)
        break
