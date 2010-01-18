# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
2009-05-15

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

""" 
Generate triples: 
    ( m^2 – n^2 )^2 + (2 m n)^2 = ( m^2 + n^2 )^2
"""
from fast_prime import gcf_list

import psyco
psyco.full()

from multiprocessing import Pool, Lock, Manager

seen = {}
def triples_from_perimeter(p):
    # return primitive triples. 
    # BRUTE FORCE
    a = 3
    b = 4
    c = p - (a + b)

    trips = []
    while a <= p:
        while b <= (p - a) and c > b:
            parms = tuple(sorted((a,b,c)))
            if parms[0] ** 2 + parms[1] ** 2 == parms[2] ** 2 and not (parms in seen):
                seen[parms] = True
                trips.append(parms)
            b += 1
            c = p - (a + b)
        a += 1
        b = 4
        c = p - (a + b)
    return trips

pool = Pool(processes=2)
primitives = pool.map(triples_from_perimeter, range(12, 1000))
pr = []
for p in primitives:
    pr.extend(p)
primitives = [(sum(p), p) for p in pr]

for p in sorted(primitives):
    print p

result = {}
max_count = 0
max_perim = 0
for p in sorted(primitives):
    val = p[0]
    if val in result:
        result[val] += 1
    else:
        result[val] = 1

    if result[val] > max_count:
        max_perim = val
        max_count = result[val]

print "%i has the most triples (%i)" % (max_perim, max_count)

