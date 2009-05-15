"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit
fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""

'''
Solve using modular arithmetic http://en.wikipedia.org/wiki/Modular_arithmetic
and multiplicative order.  http://en.wikipedia.org/wiki/Multiplicative_order

In the expression "10^k is congruent to 1 (mod n)", n represents the
denominator, and 1 represents the numerator.  Where n and 10 are
relatively prime, the value of k represents the length of the
repeating portion of the decimal expansion.  Since I know n, all I
have to do is test various values of k until I find my answer.
'''

from fast_prime import isprime

def check(n):
  if not isprime(n): return 1
  c = 1
  while (((10 ** c) - 1) % n) != 0 and c < n:
    c += 1
  return c

m = [0,0]
for n in range(5, 1000):
  if isprime(n):
    val = check(n)
    print n, val
    if val > m[1]:
      m = (n, val)      
print m

def decimal_expand(denom):
  "Produce the decimal expansion of 1 / denom"
  numer = 1
  v = int(numer) / int(denom)
  r = int(numer) % int(denom)
  while r > 0:
    numer = r * 10
    v = int(numer) / int(denom)
    r = int(numer) % int(denom)
    yield int(v)
