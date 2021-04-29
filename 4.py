# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:47:10 2020

@author: dennis
"""

def is_valid(c, v):
    if c == 'byr': return 1920 <= int(v) <= 2002
    elif c == 'iyr': return 2010 <= int(v) <= 2020
    elif c == 'eyr': return 2020 <= int(v) <= 2030
    elif c == 'hcl': return (v[0] == '#') and (sum(x in '0123456789abcdef' for x in v) == 6)
    elif c == 'ecl': return v in 'amb, blu, brn, gry, grn, hzl, oth'
    elif c == 'pid': return ((len(v) == 9) and (sum(x.isdigit() for x in v) == 9))
    
    elif c == 'hgt':
        try:
            if v[-2:] == 'in':
                if 59 <= int(v[:2]) <= 76: return True
            elif v[-2:] == 'cm':
                if 150 <= int(v[:3]) <= 193: return True
        except:
            return False
        return False
    
    else: return False

passports = ' '.join(open('data/day4.txt').read().splitlines()).split('  ')
codes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
print(sum(sum(code in passport for code in codes) == 7 for passport in passports))

valid = 0
for passport in passports:
    score = 0
    for entry in passport.split():
        c, v= entry.split(':')
        score += is_valid(c, v)
    valid += score == 7
print(valid)
