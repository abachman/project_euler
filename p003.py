"""
2007-12-14

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 317584931803?

    >>> for x in factors(13195):
    ...     if isprime(x):
    ...         print '%i,'%x , 

    5, 7, 13, 29,

"""

from fast_prime import factors, isprime

for x in factors(317584931803):
    if isprime(x):
        print '%i,'%x ,
# 1, 67, 829, 1459, 3919


