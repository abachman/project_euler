"""
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the
consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 =
40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 +
41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| 1000 and |b| 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
import psyco; psyco.full()

from fast_prime import isprime

##for n in range(80):
##  res = n**2 + (-1000 * n) - 999
##  print n, res, isprime(abs(res))

result = ((0, 0),0)
rng = 1000
for a in range(-rng,rng):
  for b in range(-rng,rng):
    n = 0
    while isprime(abs(n**2 + (a * n) + b)):
      n += 1
    if n > result[1]:
      result = (a, b), n
  if a % 50 == 0: print a, result
print
print '==== FINAL ===='
print result

##  ==== FINAL ====
##  ((-61, 971), 71)
