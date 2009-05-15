# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
The number 3797 has an interesting property. Being 
prime itself, it is possible to continuously remove 
digits from left to right, and remain prime at 
each stage: 3797, 797, 97, and 7. Similarly we can 
work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both 
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be 
truncatable primes.
"""
import psyco
psyco.full()
from fast_prime import isprime, primes_in_range
import re

def truncr(s):
    l = len(s)
    for i in range(1,l):
        yield s[0:-i]

def truncl(s):
    l = len(s)
    for i in range(1,l):
        yield s[i:l]

def test():
    t = truncl("asdf")
    t1 = t.next()
    assert t1 == 'sdf', "step 1 failed: " + t1
    t1 = t.next()
    assert t1 == 'df', "step 2 failed: " + t1
    t1 = t.next()
    assert t1 == 'f', "step 3 failed: " + t1
    t = truncr("asdf")
    t1 = t.next()
    assert t1 == 'asd', "step 1 failed: " + t1
    t1 = t.next()
    assert t1 == 'as', "step 2 failed: " + t1
    t1 = t.next()
    assert t1 == 'a', "step 3 failed: " + t1
    try:
        t.next() 
    except StopIteration:
        assert True
    else:
        assert False
    

test()

checkpoints = range(1, 2000000, 10000)

def solve():
    even_char = re.compile("0|2|4|6|8")
    sum_all = 0
    count = 0
    for i in primes_in_range(9,1000000,2):
        s = str(i)
        if '0' in s:
            continue
#       if even_char.search(s):
#           continue
#       else:
        flag = True
        for sub in truncl(s):
            if not isprime(int(sub)):
                flag = False
                break
        if flag:
            for sub in truncr(s):
                if not isprime(int(sub)):
                    flag = False
                    break
        if flag: 
            count += 1
            sum_all += i
            print '*** PING ***   ', i
    print "Answer: first %i primes add up to %i" % (count, sum_all)

solve()
