"""
2007-12-17

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7
= 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that the 7th triangle number, 28, is the first triangle
number to have over five divisors.

Which is the first triangle number to have over five-hundred divisors?
"""

import psyco
psyco.full()

from fast_prime import count_factors, factors

def tris():
    i = 1
    s = 0
    while True:
        s = s + i
        i += 1
        yield s

## demo
#c=0
#for x in tris():
#    if c >= 7:
#        break
#    print '%2i: %s' % (x, ','.join(map(str, [f for f in factors(x)])))
#    c+=1

m = 0
n = 1
t = tris()
while m < 500:
    c = t.next()
    m = max(m, count_factors(c))
    n+=1
    if n % 200==0:
        print n
print '%2i: %s' % (c, ','.join(map(str, [f for f in factors(c)])))
# 11800
# 12000
# 12200
#76576500

