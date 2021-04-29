# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:11:35 2020

@author: dennis
"""

from collections import deque

def game(d1, d2):
    seen = set()
    while d1 and d2:
        s = ','.join(str(x) for x in d1) + '|' + ','.join(str(x) for x in d2)
        if s in seen:
            return 1, d1, d2
        seen.add(s)
        c1 = d1.popleft()
        c2 = d2.popleft()
        if (len(d1) >= c1) and (len(d2) >= c2):
            nd1 = deque(list(d1.copy())[:c1])
            nd2 = deque(list(d2.copy())[:c2])
            winner, _, _ = game(nd1, nd2)
        elif c1 > c2:
            winner = 1
        elif c1 < c2:
            winner = 2
        if winner == 1:
            d1 += [c1, c2]
        elif winner == 2:
            d2 += [c2, c1]
    if d1:
        return 1, d1, d2
    elif d2:
        return 2, d1, d2

def parse_input():
    player1 = deque([])
    player2 = deque([])
    lines = open('data/22.txt').read().splitlines()
    for line in lines[1:lines.index('')]:
        player1.append(int(line))
    for line in lines[lines.index('')+2:]:
        player2.append(int(line))
    return player1, player2

player1, player2 = parse_input()
r = 0
while player1 and player2:
    c1 = player1.popleft()
    c2 = player2.popleft()
    if c1 > c2:
        player1 += [c1, c2]
    elif c1 < c2:
        player2 += [c2, c1]
    r += 1
if player1:
    print('Part 1:', sum(player1[-i]*i for i in range(1, len(player1)+1)))
else:
    print('Part 1:', sum(player2[-i]*i for i in range(1, len(player2)+1)))

player1, player2 = parse_input()
winner, player1, player2 = game(player1, player2)
if player1:
    print('Part 1:', sum(player1[-i]*i for i in range(1, len(player1)+1)))
else:
    print('Part 1:', sum(player2[-i]*i for i in range(1, len(player2)+1)))
