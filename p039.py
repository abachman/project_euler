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


def is_triple(a,b,c):
    return a ** 2 + b ** 2 == c ** 2

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
            if is_triple(*parms) and not (parms in seen):
                seen[parms] = True
                trips.append(parms)
            b += 1
            c = p - (a + b)
        a += 1
        b = 4
        c = p - (a + b)
    return trips

def scaled_triples(trip):
    count = 2
    a, b, c = trip
    while a + b + c < 1000:
        # scale up a, b, c
        a, b, c = map(lambda n: n * count, [a,b,c])
        if not (a, b, c) in seen:
            if (a + b + c <= 1000):
                yield a, b, c
                seen[(a, b, c)] = True
            else:
                break
        count += 1

def explore((p, results, lock)):
    results = {}
    for trip in triples_from_perimeter(p):
        s = sum(trip)
        if s in results:
            results[s] += 1
        else:
            results[s] = 1
        for s_trip in scaled_triples(trip):
            s = sum(trip)
            if s in results:
                results[s] += 1
            else:
                results[s] = 1
    print results

pool = Pool(processes=4)
primitives = pool.map(triples_from_perimeter, range(12, 500))
pr = []
for p in primitives:
    pr.extend(p)
primitives = [(sum(p), p) for p in pr]

for p in sorted(primitives):
    print p

#ordered = reversed(sorted([(results[k], k) for k in results]))
#print '\n'.join(["%-5i:\t%i" % (b, a) for a, b in ordered][:10])

def triples_from(m):
    n = 1
    while n < m:
        # first pass
        _a = m**2 - n**2
        _b = 2 * m * n
        _c = m**2 + n**2
        _a, _b, _c = sorted((_a, _b, _c))
        if not (_a,_b,_c) in seen and is_triple(_a, _b, _c) and _a + _b + _c <= 1000:
            # we know _a, _b, _c is a pythagorean triple and may be primitive
            if gcf_list(_a, _b, _c) == 1:
                print "PRIMITIVE:", (_a, _b, _c), (m, n)
            else:
                n += 1
                continue
            yield _a, _b, _c
            count = 2
            a,b,c = _a, _b, _c
            while a + b + c < 1000:
                # scale up a, b, c
                a,b,c = map(lambda n: n * count, [a,b,c])
                if not (a,b,c) in seen:
                    if (a + b + c <= 1000):
                        # print 'scaled', (a,b,c)
                        yield a, b, c
                        seen[(a,b,c)] = True
                    else:
                        break
                count += 1
            seen[(_a, _b, _c)] = True
        n += 1

#MAXOUT = 500
#perimeters = {}
#for n in range(MAXOUT):
#    for trip in triples_from(n):
#        a, b, c = trip
#        s = sum(trip)
#        if sum(trip) in perimeters:
#            perimeters[s].append(trip)
#        else:
#            perimeters[s] = [trip]
#
#perms_by_count = map(lambda t: (t[1], t[0]), sorted([(len(perimeters[k]), k) for k in perimeters]))
#for result in perms_by_count:
#    print "%-5i: %i" % result




