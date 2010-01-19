# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
2010-01-17

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import psyco
psyco.full()

from fast_prime import m_isprime

nums = list('123456789')
def is_pan(s):
  if sorted(s) == nums[0:len(s)]:
    return True
  else:
    return False

def permutations(li):
  """ Return all permutations of a given list.  This funtion assumes
  every element of the list is unique. (from p024.py)"""
  if len(li) <= 1:
    yield li
  else:
    for el in li:
      for p in permutations([e for e in li if not e == el]):
        yield [el] + p

def solve():
    # only check prime pandigitals 
    current = ''
    last = 0
    # Turns out we only need 1 through 7 to find the correct answer.
    # This is good, since adding 8 and 9 would add 400000 potential 
    # permutations to search through
    for digit in '1234567':
        current += digit
        for _perm in permutations(current):
            if _perm[-1] in '2468': continue
            perm = ''.join(_perm)
            if m_isprime(int(perm)) and is_pan(perm):
                last = perm
    print last

solve()

