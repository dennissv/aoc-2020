# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 01:50:36 2020

@author: dennis
"""

from copy import deepcopy

ing = set()
a = set()
d = dict()
ingre = []
with open('data/21.txt') as f:
    for line in f.readlines():
        ingredients = line[:line.index('(')].split()
        ingre += ingredients
        ingredients = set(ingredients)
        ing = ing | ingredients
        allergens = {x.strip(',') for x in line[line.index('(')+1:-2].split()[1:]}
        for allergen in allergens:
            if allergen not in d:
                d[allergen] = [ingredients]
            else:
                d[allergen].append(ingredients)

for a, v in d.items():
    d[a] = set.intersection(*v)

old = dict()
while old != d:
    old = deepcopy(d)
    to_remove = set()
    for a, v in d.items():
        if len(v) == 1:
            to_remove.add(v.copy().pop())
    for x in to_remove:
        for a, v in d.items():
            if len(v) > 1 and x in v:
                v.remove(x)

unsafe = to_remove
ans = 0
for x in ingre:
    if x not in unsafe:
        ans += 1
print(ans)
print(','.join(list(d[x])[0] for x in sorted(list(d.keys()))))
