"""
2007-12-20
n! means n  (n  1)  ...  3  2  1

Find the sum of the digits in the number 100!
"""

import psyco
psyco.full()
from fast_prime import factorial

print sum(map(int, [l for l in str(factorial(100))]))


# 648
