# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
The decimal number, 585 = 1001001001_(2) (binary), is 
palindromic in both bases.

Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base 2.
"""

def is_pal(seq):
    length = len(seq)
    for n, l in enumerate(seq):
        if l == seq[-(n + 1)]:
            continue
        else:
            return False
    return True

def to_bin(i):
    i = int(i)
    res = []
    c = 0
    q = 1
    rem = 0
    while q != 0:
        q = i // 2
        rem = i % 2
        res.append(rem)
        i = q
    return list(reversed(res))

def test():
    assert is_pal('12321')
    assert is_pal('123321')
    assert not is_pal('12345')
    assert to_bin(2) == [1,0]
    assert to_bin(16) == [1,0,0,0,0]
    assert to_bin(21) == [1,0,1,0,1]

def solve():
    s = sum(i for i in xrange(999999) if is_pal(str(i)) and is_pal(to_bin(i)))
   #for i in xrange(129):
   #    if is_pal(str(i)):
   #        if is_pal(to_bin(i)):
   #            s += i
   #            print i, to_bin(i)
    print "Answer:", s

test()
solve()
