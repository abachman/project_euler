"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below one million.
"""
from time import time
import psyco
psyco.full()
from fast_prime import isprime

def solve():
    n = 1
    s = 0
    start = time()
    while n < 1000000:
#        if n % 10000 == 0: print n,
        if n%2 == 0 or n%3 == 0:
            n+=1
            continue
        if isprime(n):
            print n
            s += n
        n+=1
    print s
    print 'finished in %f seconds' % (time() - start)


solve()
# 37550402023
