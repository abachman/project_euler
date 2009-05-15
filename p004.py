"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from fast_prime import isprime, factors

print 'number will be in range', 100*100, '< x <', 999*999

'''
counting down from 999*999, check whether a number is a palindrome
(if not, skip it), whether it is a prime (if so, skip it), and finally
whether it has any three digit factors.
'''
def ispalindrome(n):
    return str(n) == ''.join(reversed(str(n)))

def solve():
    for n in xrange(999*999, 1, -1):
##        if n < 9000:
##            break
        if ispalindrome(n) and not isprime(n):
#            print 'checking',n
            for x in factors(n):
                if x <= 999 and x >= 100 and n / x > 100 and n / x < 999:
                    print n, ':', x, '*', n / x
                    break

def solve_twodigit():
    for n in xrange(99*99, 1, -1):
##        if n < 9000:
##            break
        if ispalindrome(n) and not isprime(n):
#            print 'checking',n
            for x in factors(n):
                if x <= 99 and x >= 10 and n / x > 10 and n / x < 99:
                    print n, ':', x, '*', n / x
                    break
      
#solve_twodigit()      
solve()    
