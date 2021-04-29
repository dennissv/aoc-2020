# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:01:46 2020

@author: dennis
"""

def evaluate(expression):
    opening = expression[0].count('(')
    closening = expression[-1].count(')')
    sum_ = int(expression[0].lstrip('('))
    for i in range((len(expression) - 1) // 2):
        symbol = expression[i*2 + 1]
        value = int(expression[i*2 + 2].strip(')'))
        if symbol == '*':
            sum_ *= value
        elif symbol == '+':
            sum_ += value
        else:
            print('wtf')
    return '('*(opening - 1) + str(sum_) + ')' * (closening - 1)

def evaluate_advanced(expression):
    opening = expression[0].count('(')
    closening = expression[-1].count(')')
    expression[0] = expression[0].lstrip('(')
    expression[-1] = expression[-1].strip(')')
    while '+' in expression:
        i = expression.index('+')
        expression = expression[:i-1] + [str(int(expression[i-1]) + int(expression[i+1]))] + expression[i+2:]
    while '*' in expression:
        i = expression.index('*')
        expression = expression[:i-1] + [str(int(expression[i-1]) * int(expression[i+1]))] + expression[i+2:]
    sum_ = int(expression[0].strip('(').strip(')'))
    return '('*(opening - 1) + str(sum_) + ')' * (closening - 1)

lines = open('data/18.txt').read().splitlines()
answers = []
for line in lines:
    line = line.split()
    while 1:
        end = 0
        start = 0
        for i, v in enumerate(line):
            if ')' in v:
                end = i + 1
                break
        for i, v in enumerate(line[:end][::-1]):
            if '(' in v:
                start = end - i - 1
                break
        if not end:
            break
        line = line[:start] + [evaluate(line[start:end])] + line[end:]
    answers.append(int(evaluate(line)))
print('Part 1:', sum(answers))

answers2 = []
for line in lines:
    line = line.split()
    while 1:
        end = 0
        start = 0
        for i, v in enumerate(line):
            if ')' in v:
                end = i + 1
                break
        for i, v in enumerate(line[:end][::-1]):
            if '(' in v:
                start = end - i - 1
                break
        if not end:
            break
        line = line[:start] + [evaluate_advanced(line[start:end])] + line[end:]
    answers2.append(int(evaluate_advanced(line)))
print('Part 2:', sum(answers2))
