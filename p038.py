# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
2009-05-15

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import psyco
psyco.full()

def has_all(s):
    return all(map( lambda i: i in s, '123456789' ))

def solve():
    for n in range(200000):
        out = ''
        for x in range(1,12):
           out += str(n * x) 
           if len(out) == 9:
               if has_all(out):
                   print "%i:\t%s\t" % (n, out)
               break

if __name__ == "__main__":
    #    assert has_all('123456789')
    #    assert not has_all('1234')
    solve()

