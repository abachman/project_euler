"""
2007-12-20
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

import psyco
psyco.full()

s = 0
for i in xrange(1,1001):
    s += pow(i,i)
print s
print str(s)[-10:]
