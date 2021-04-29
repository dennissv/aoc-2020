# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 20:31:04 2020

@author: dennis
"""

class Match():
    
    def __init__(self, instructions):
        pass

# def parse(i):
#     if not rules[i].isdigit():
#         pass
#     else:
#         return rules[i]

lines = open('data/19.txt').read().splitlines()
# rules = dict()
# for line in lines[:lines.index('')]:
#     line = line.split()
#     rule_nr = int(line[0][:-1])
#     if len(line) == 2:
#         try:
#             rules[rule_nr] = int(line[1])
#         except:
#             rules[rule_nr] = line[1].strip('"')
#     elif len(line) == 3:
#         rules[rule_nr] = (((int(line[1]), int(line[2]))))
#     elif len(line) == 4:
#         rules[rule_nr] = ((int(line[1])), (int(line[3])))
#     elif len(line) == 6:
#         rules[rule_nr] = ((int(line[1]), int(line[2])), (int(line[4]), int(line[5])))

