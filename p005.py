"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the 
numbers from 1 to 20?
"""

import psyco
psyco.full()

def lcm(a, b):
    na = a
    nb = b
    while b != 0:
         t = b
         b = a % b
         a = t
    return na * nb / a

n = 1
for i in range(1,21):
    n = lcm(i, n)
print n
    
# 232792560
