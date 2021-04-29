# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:31:45 2020

@author: dennis
"""

l = ' '.join(open('data/6.txt').read().splitlines()).split('  ')
print(sum(len(set(a.replace(' ', ''))) for a in l))
print(sum(len(set.intersection(*[set(x) for x in a.split()])) for a in l))
