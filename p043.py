# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
2010-01-18

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note 
the following:

d_2 d_3 d_4  = 406 is divisible by 2
d_3 d_4 d_5  = 063 is divisible by 3
d_4 d_5 d_6  = 635 is divisible by 5
d_5 d_6 d_7  = 357 is divisible by 7
d_6 d_7 d_8  = 572 is divisible by 11
d_7 d_8 d_9  = 728 is divisible by 13
d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import psyco
psyco.full()

# using a combinations-generator for larger permutations
def xcombinations(items, n):
    if n == 0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i] + items[i+1:], n-1):
                yield [items[i]] + cc

def xpermutations(items):
    """permutations are just a special case of combinations"""
    return xcombinations(items, len(items))

#def permutations(li):
#  """ Return all permutations of a given list.  This funtion assumes
#  every element of the list is unique. (from p024.py)"""
#  if len(li) <= 1:
#    yield li
#  else:
#    for el in li:
#      for p in permutations([e for e in li if not e == el]):
#        yield [el] + p

def check(n):
    n = ''.join(n)
    if int(n[1:4]) % 2 == 0 and \
        int(n[2:5]) % 3 == 0 and \
        int(n[3:6]) % 5 == 0 and \
        int(n[4:7]) % 7 == 0 and \
        int(n[5:8]) % 11 == 0 and \
        int(n[6:9]) % 13 == 0 and \
        int(n[7:]) % 17 == 0:
        return True
    else:
        return False

def solve():
    count = 0
    sum = 0
    for p in xpermutations('0123456789'):
        if check(p):
            print "found:", p
            sum += int(''.join(p))
        if count % 100000 == 0 : 
            print count
        count += 1
    print "TOTAL:", sum

solve()


