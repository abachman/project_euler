# -*- coding: cp1252 -*-
"""
A Pythagorean triplet is a set of three natural numbers, abc, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import psyco
psyco.full()

import numpy
##for i in xrange(1000000):
##    if numpy.sqrt(i) % 1 == 0:
##        print i, numpy.sqrt(i)
##

## which perfect squares are the sum of two perfect squares? (brute force)
psqrs = {}
nums = []

for i in range(1, 500):
    nums.append((i*i, i))
    psqrs[i*i] = []

for n in nums:
    matched = {}
    for o in nums:
        if o[0] > n[0] or o[1] + n[1] > 1000 or o[0] in matched:
            break
        elif n[0] - o[0] in psqrs:
            #print '%i + %i = %i' % (o[0], n[0]-o[0], n[0])
            matched[o[0]]=0
            matched[n[0]-o[0]]=0
            psqrs[n[0]].append((o[0], n[0]-o[0]))  

for k in sorted(psqrs.keys()):
    for p in psqrs[k]:
        a = p[0]
        b = p[1]
        a, b, c = numpy.sqrt(a), numpy.sqrt(b), numpy.sqrt(k)
        if a+b+c == 1000:
            print '**************** BINGO'
            print '%-5i %-5i %i' % (a, b, c)
            print 'solution = %i' % (a*b*c)
            print '**************** BINGO'#print psqrs

# 31875000
