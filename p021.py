# -*- coding: utf-8 -*-
"""
2008-01-24

Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n). If d(a) = b and d(b) = a, where
a ≠ b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from fast_prime import factors

sumd = {}

for n in range(10000):
    s = sum(factors(n)) - n
    sumd[n] = s

s = set()

for k in sumd:
    if k in sumd and sumd[k] in sumd and k == sumd[sumd[k]] and k != sumd[k]:
        s.add(k)
        s.add(sumd[k])

print s
print sum(s)
        
    



