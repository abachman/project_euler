"""
2007-12-17

The following iterative sequence is defined for the set of positive
integers:

n n/2 (n is even)
n 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:

13 40 20 10 5 16 8 4 2 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one
million.
"""
import psyco
psyco.full()

def collatz(n):
    count = 1
##    print n, '=>',
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
##        print n, '=>',
        count += 1
##    print n
    return count

if __name__=="__main__":
    m = (0, 0)
    ## print collatz(13)
    n = 1
    while n < 1000000:
        c = collatz(n)
        if c > m[0]:
            m = (c, n)

        if n % 333 == 0:
            print n, m
        n += 2
        
##    from pylab import *
##    plot([collatz(n) for n in xrange(1000)])
##    show()
