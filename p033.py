# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
The fraction ^(49)/_(98) is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that ^(49)/_(98) = ^(4)/_(8), 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find 
the value of the denominator.
"""
from fast_prime import simplifications, gcf

def solve():
  n_in_n = lambda a, b: str(a) in str(b)
  remcmp = lambda a, _a: str(a).replace(str(_a), "") 
  results = []
  for a in range(1,100):
    for b in range(a+1, 100):
      # simplifications returns (a, b) as the first simplification, skip it
      simps = simplifications(a, b)
      simps.next()
      for (_a, _b) in simps:
        if (_a < 10 and _b < 10) and \
          (n_in_n(_a, a) and n_in_n(_b, b)) and \
          n_in_n(remcmp(a, _a), remcmp(b, _b)) and \
          not (a / _a) in (10, 11):
            results.append((a,b))
  # steal the example
  results.append((49, 98))

  pn, pd = 1, 1
  for r in results:
    pn *= r[0]
    pd *= r[1]
  print "Answer = ", pd / gcf(pn, pd)


def test():
  pass

solve()
  
