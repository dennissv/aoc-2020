# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:55:13 2020

@author: dennis
"""

import math

possible = set()
tickets = []
ranges = []
with open('data/16.txt') as f:
    line = f.readline().strip()
    while line:
        line = line.split()
        one = line[-3].split('-')
        for x in range(int(one[0]), int(one[1]) + 1):
            possible.add(x)
        two = line[-1].split('-')
        for x in range(int(two[0]), int(two[1]) + 1):
            possible.add(x)
        name = line[0]
        ranges.append((range(int(one[0]), int(one[1]) + 1),
                       range(int(two[0]), int(two[1]) + 1)))
        line = f.readline().strip()
    _ = f.readline()
    line = f.readline().strip().split(',')
    my_ticket = [int(x) for x in line]
    _ = f.readline()
    _ = f.readline()
    for line in f.readlines():
        tickets.append([int(x) for x in line.strip().split(',')])

ans = 0
valid_tickets = []
for ticket in tickets:
    valid = True
    for x in ticket:
        if x not in possible:
            ans += x
            valid = False
    if valid:
        valid_tickets.append(ticket)
print('Part 1:', ans)

p = []
for r in ranges:
    r1 = r[0]
    r2 = r[1]
    tmp = set()
    for i in range(20):
        sum_ = 0
        for ticket in valid_tickets:
            if (ticket[i] in r1) or (ticket[i] in r2):
                sum_ += 1
        if sum_ == len(valid_tickets):
            tmp.add(i)
    p.append(tmp)

d = dict()
while len(d) < len(p):
    for i, s in enumerate(p):
        if len(s) == 1:
            v = s.pop()
            d[i] = v
            for x in p:
                if v in x:
                    x.remove(v)
            break

print('Part 2:', math.prod(my_ticket[d[i]] for i in range(6)))
