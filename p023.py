"""
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors 
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
number. 

A number whose proper divisors are less than the number is called 
deficient and a number whose proper divisors exceed the number is called 
abundant. 

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers 
greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even 
though it is known that the greatest number that cannot be expressed as 
the sum of two abundant numbers is less than this limit. 

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers. 
"""

import psyco
psyco.full()

import fast_prime as fp

mrange = 28124
abunds = {}
for i in range(1, mrange):
    fs = [f for f in fp.factors(i)][:-1]
    s = sum(fs)
    if s > i:
        abunds[i] = 0
nsum = []
for n in range(1, mrange):
    found = False
    for k in abunds:
        if n - k in abunds:
            found = True
            break
    if not found:
        nsum.append(n)
print len(nsum), sum(nsum)

# 1456 abundants, sum = 4179871