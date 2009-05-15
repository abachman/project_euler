# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigitial.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
"""

nums = list('123456789')
def is_pan(s):
  if sorted(s) == nums:
    return True
  else:
    return False

def comb(*n):
  return ''.join(map(str, n))

def solve():
  result = 0
  pairs = set()
  a = 1
  r = range(2000)
  while a < 2000:
    for b in r:
      p = a * b
      s = comb(a,b,p)
      if len(s) == 9:
        if is_pan(s) and not p in pairs:
          result += p
          pairs.add(p)
          print 'found one:', a, b, p
      elif len(s) > 9:
        break
    a += 1
  print result

def test():
  assert is_pan('123654987'), "Should be pandigital"
  assert not is_pan('12345678'), "Should not be pandigital"
  assert comb(1,2,3,4) == '1234', "(1,2,3,4) should combine to '1234'"
  assert is_pan(comb(123, 456, 789)), "(123,456,789) should combine to pandigital '123456789'"
  assert is_pan(comb(39, 186, 7254)), "(39, 186, 7254) is pandigital"

test()
solve()
