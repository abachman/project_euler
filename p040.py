# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
2010-01-17

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
"""

import psyco
psyco.full()

flags = [10 ** n for n in range(7)]

print "flags at", flags

chars = 0
digits = []
endit = False
for _n in xrange(1, 320000):
    n = str(_n)
    
    # if we'll pass a flag
    if chars + len(n) >= flags[0]:
        # find out which digit is the flag'd
        for i in xrange(len(n)):
            if chars + i + 1 == flags[0]:
                # keep the digit, get rid of the flag
                digits.append(n[i])
                out = flags.pop(0)
                print out, "was", n[i]
                if out == 1000000:
                    endit = True
                break
                
    chars += len(n)

    if endit: break

def product(l):
    p = 1
    for n in l:
        p *= n
    return p

print "done: "
print " * ".join(digits), "=", product(map(int, digits))

