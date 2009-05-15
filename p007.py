"""
2007-12-16
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import psyco
psyco.full()
from fast_prime import isprime

c = 0
n = 1
while c < 10001:
    if isprime(n):
        c += 1
    n += 1
print n-1
