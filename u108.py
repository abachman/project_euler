"""
2007-12-14

In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8  = 1/4

What is the least value of n for which the number of distinct
solutions exceeds one-thousand?

NOTE: This problem is an easier version of problem 110; it is strongly
advised that you solve this one first.

factors, number
128      83160
144      110880
160      166320
168      221760
180      277200
192      332640
200      498960
216      554400
224      665280
240      720720
256      1081080
288      1441440
320      2162160
336      2882880
360      3603600
384      4324320
400      6486480
432      7207200
448      8648640
480      10810800
504      14414400
512      17297280
576      21621600
600      32432400
640      36756720
672      43243200
720      61261200
768      73513440
800      110270160
864      122522400
896      147026880
960      183783600
1008     245044800

"""

from fast_prime import factors, isprime, count_factors, factorial, primes_in_range
#from numpy import mod
import psyco
psyco.full()

def lcm(a, b):
    na = a
    nb = b
    while b != 0:
         t = b
         b = a % b
         a = t
    return na * nb / a

def psolutions(n):
    ## find solutions to 1/x + 1/y = 1/n
    i = n
    m = n * 2
    count = 0
    ## count up to n*2
    while i <= m:
        ## get LCM
        a = i
        b = n
        while b != 0:
             t = b
             b = a % b
             a = t
        l = i * n / a
        ## find top value of left side
        topL = (l / i)
        ## find top value of right side
        topR = (l / n)
        #print '1/%i + 1/%i = 1/%i' % (i, l, n)
        if topL + 1 == topR:
            yield i, l, n
            count += 1
        i += 1
    return 

def solutions(n):
    ## find solutions to 1/x + 1/y = 1/n
    #if n % 1000 == 0: print 'solving for', n
    i = n
    m = n * 2
    count = 0
    ## count up to n*2
    while i <= m:
        ## get LCM
        a = i
        b = n
        while b != 0:
             t = b
             b = a % b
             a = t
        l = i * n / a
        ## find top value of left side
        topL = (l / i)
        ## find top value of right side
        topR = (l / n)
        if topL + 1 == topR:
            #print i, l, n
            #print '  1/%i + 1/%i = 1/%i' % (i, l, n)
            count += 1
        i += 1
    return count

def solve(m=1000):
    count = 0
    c = 0
    n = 245044800
    step = -2520
    vals = []
    highest = (0,1)
    while count < m: 
        c = count_factors(n) #solutions(n)
#        if c > highest[0]:
#            highest = (c, n)
        if c > 1000:
            print "%i\t%i" % (c, n)# highest
        #if count % 10==0: print n, 
        n += step
        count += 1
    return vals

def factor_search(m=1000):
    c = 0
    n = 1
    highest = (1, 1)
    while c < m:
        c = count_factors(n)
        n += 10
        if c > highest[0]: 
            highest = (c, n)
    print n-1

if __name__=="__main__":
##    for s in solutions(4):
##        print '1/%i + 1/%i = 1/%i' % s
    assert solutions(4) == 3
    
    if 0:
        import cProfile
        cProfile.run('solve()')
    elif 0:
        f = factorial(12)
        f2 = factorial(13)
        print f, f2
        print f2 - f
        print len([n for n in primes_in_range(f+1, f+10000)])
    elif 0:
        factor_search(50)
    elif 1:
        solve(1000000)
    elif 0:
        import time
        def cfs():
            c = 1
            vals = []
            while c < 10000:
                vals.append(count_factors(c))
                c += 1
            return vals
        def sols():
            c = 1
            vals = []
            while c < 10000:
                vals.append(solutions(c))
                c += 1
            return vals
        s = time.time()
        sols()
        print "solutions in", time.time() - s

        s = time.time()
        cfs()
        print "count factors in", time.time() - s
    else:
        m = 10000
        v = dict((n, solutions(n)) for n in range(1, m+1))
        v2 = dict((n, count_factors(n)) for n in range(1,m+1))
        for i in v:
            if v[i] != v2[i]:
                print '%-4i: %-3i%i' % (i, v[i], v2[i])
                print '  ', ','.join(map(str, [f for f in factors(i)]))
                print '  ', ','.join(map(str, [f for f in psolutions(i)]))

