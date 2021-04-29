# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:48:22 2020

@author: dennis
"""

import re

lines = open('data/7.txt').read().splitlines()
rules = dict()
for line in lines:
    bags = re.findall(r'\d \w+ \w+', line)
    bag = re.match(r'\w+ \w+', line).group()
    rules[bag] = {b[2:]: int(b[0]) for b in bags}

ans = set(['shiny gold'])
new = 1
while new:
    new = set()
    for bag, contains in rules.items():
        for a in ans:
            if a in contains and bag not in ans:
                new.add(bag)
    for n in new:
        ans.add(n)
print('Part 1:', len(ans) - 1)

size = 0
bags = rules['shiny gold']
while bags:
    new = []
    for bag, quantity in bags.items():
        size += quantity
        new.append((rules[bag], quantity))
    bags = dict()
    for n in new:
        for bag, q in n[0].items():
            if bag not in bags:
                bags[bag] = q * n[1]
            else:
                bags[bag] += q * n[1]
print('Part 2:', size)
