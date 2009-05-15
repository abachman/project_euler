# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from fast_prime import factorial

facts = dict((n, factorial(n)) for n in range(10))

def solve():
    s = 0
    for n in xrange(3, 100000):
        if sum((facts[int(d)] for d in str(n))) == n:
            s+=n
            print n
        if n % 1000000 == 0: 
            print n
    print "Answer: ", s

#test() 
solve()

