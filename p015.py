"""
2007-12-18
Starting in the top left corner of a 2 x 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 2020 grid?

(pascal!)
"""

import psyco
psyco.full()

def pascal(n):
    " return the nth row of pascal's triangle "
    if n == 0:
        return []
    p = [1]
    if n == 1:
        return p
    while n > 1:
        l = [1]
        i = 1
        while len(l) < len(p):
            l.append(p[i-1] + p[i])
            i += 1
        l.append(1)
        p = l
        n -= 1
    return p

def square_routes(n):
    " number of routes through an n x n grid "
    p = pascal((2 * n) + 1)
    return p[ (len(p) / 2) ]

##print pascal(1)
##print pascal(2)
##print pascal(3)
##print pascal(4)
##print pascal(20)

print square_routes(1)
print square_routes(2)
print square_routes(3)
print square_routes(4)
print square_routes(5)
print square_routes(20)

# 137846528820
