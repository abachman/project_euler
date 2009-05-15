# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
The number, 197, is called a circular prime because all 
rotations of the digits: 197, 971, and 719, are themselves 
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from fast_prime import primes_in_range, isprime

def rots(n):
    _n = [l for l in str(n)]
    ln = len(_n)
    c = 1
    while c < ln: 
        a = _n.pop(0)
        _n.append(a)
        yield int(''.join(_n))
        c += 1

def test():
    assert [n for n in rots(152)] == [521, 215]

def solve():
    c = 0
    for n in primes_in_range(2, 1000000, 1):
        flag = True
        for r in rots(n):
            if not isprime(r):
                flag = False
                break
        if flag:
            c += 1
            print "%i (%i)" % (n, c)

test()
solve()


