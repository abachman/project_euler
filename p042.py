# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""
The n^(th) term of the sequence of triangle numbers is 
given by, t_(n) = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding 
to its alphabetical position and adding these values we form a 
word value. For example, the word value for SKY is 
19 + 11 + 25 = 55 = t_(10). If the word value is a triangle 
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 
16K text file containing nearly two-thousand common English words,
how many are triangle words?

"""
import psyco
psyco.full()

def tri(n):
    return int((float(n) / 2) * (n + 1))
tnums = dict((tri(n), 0) for n in range(1000))
letters = dict((l.upper(),n+1) for n, l in enumerate('abcdefghijklmnopqrstuvwxyz'))

def test():
    
    l = 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    for x in range(1, 11):
        assert l[x-1] == tri(x)
    assert all(n in tnums for n in l)
    assert sum(letters[l] for l in 'SKY') in tnums
#test() 
def solve():
    c = 0
    words = file('p042_words.txt').read().split(',')
    words = [w.strip('"') for w in words]
    print len(words), "words..."
    for w in words:
        if sum(letters[l] for l in w) in tnums:
            c += 1
            print w
    print "Answer: ", c
solve()
