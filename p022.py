# -*- coding: cp1252 -*-
"""
2008-01-24

Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for
each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

names = file('names.txt').read()
names = [n.strip('"').lower() for n in names.split(',')]
names.sort()

#print names

def nval(n):
    v = 'abcdefghijklmnopqrstuvwxyz'
    s = 0
    for l in n:
        s += v.index(l) + 1
    return s

s = 0
c = 1
for n in names:
    s += nval(n) * c
    c += 1
print s
    
    
